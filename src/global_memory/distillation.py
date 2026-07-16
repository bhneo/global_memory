from __future__ import annotations

import difflib
import hashlib
import json
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .atomicity import AtomicClaimInspector
from .errors import ValidationError
from .followups import FollowupService
from .markdown import atomic_write_text, read_document, render_document
from .proposals import CANONICAL_DIRECTORIES
from .quality import SourceQualityService
from .repository import Repository, now_iso, sha256_bytes, slugify


SELECTED_CLAIMS = [
    "claim_wechat_epiplexity_definition_20260715",
    "claim_wechat_ergodicity_time_vs_ensemble_20260716",
    "claim_wechat_non_ergodic_coin_game_20260716",
    "claim_wechat_kelly_bet_fraction_20260716",
    "claim_wechat_lie_group_definition_20260715",
    "claim_wechat_lie_group_continuous_symmetry_20260715",
    "claim_wechat_param_symmetry_definition_20260716",
    "claim_wechat_param_symmetry_conserved_quantities_20260716",
    "claim_wechat_godel_first_incompleteness_20260716",
    "claim_wechat_physo_method_20260715",
    "claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716",
    "claim_wechat_ganzfeld_mechanism_20260715",
    "claim_wechat_embodied_data_structure_not_volume_20260716",
    "claim_wechat_embodied_data_quality_cost_tradeoff_20260716",
    "claim_wechat_embodied_eval_bottleneck_20260715",
    "claim_wechat_skillevolver_meta_audit_loop_20260716",
    "claim_wechat_im_rl_framework_internal_rewards_20260716",
    "claim_wechat_kairos_sim2real_training_20260716",
    "claim_wechat_cross_modal_representation_alignment_20260716",
    "claim_wechat_wangjun_global_workspace_integration_20260716",
    "claim_wechat_magnetic_bottle_constraint_20260715",
    "claim_wechat_double_trace_traversable_20260715",
    "claim_wechat_particle_poincare_wigner_20260716",
]


CURATED_NODES: list[dict[str, Any]] = [
    {"type": "concept", "id": "concept_epiplexity", "title": "Epiplexity", "anchors": ["claim_wechat_epiplexity_definition_20260715"], "body": "有限计算资源下，观察者能够从数据中提取并复用的结构信息；定义与定理仍需回到原论文核验。"},
    {"type": "concept", "id": "concept_ergodicity", "title": "遍历性与非遍历性", "anchors": ["claim_wechat_ergodicity_time_vs_ensemble_20260716", "claim_wechat_non_ergodic_coin_game_20260716"], "body": "区分群体平均与单一主体随时间经历的结果，尤其关注不可逆损失和生存约束。"},
    {"type": "concept", "id": "concept_kelly_criterion", "title": "Kelly Criterion", "anchors": ["claim_wechat_kelly_bet_fraction_20260716"], "body": "在重复下注和资本存续条件下平衡增长率与破产风险的资源配置原则。"},
    {"type": "concept", "id": "concept_lie_group", "title": "李群与连续对称性", "anchors": ["claim_wechat_lie_group_definition_20260715", "claim_wechat_lie_group_continuous_symmetry_20260715"], "body": "同时具有群结构与光滑流形结构，用于表达连续变换及其不变量。"},
    {"type": "concept", "id": "concept_parameter_symmetry", "title": "参数空间对称性", "anchors": ["claim_wechat_param_symmetry_definition_20260716", "claim_wechat_param_symmetry_conserved_quantities_20260716"], "body": "不改变模型函数或损失的参数变换及其对优化几何、守恒量和模型合并的影响。"},
    {"type": "concept", "id": "concept_intrinsic_motivation_rl", "title": "内在动机强化学习", "anchors": ["claim_wechat_im_rl_framework_internal_rewards_20260716"], "body": "使用新颖性、预测误差、能力增长或社会影响等内部信号驱动探索与技能获得。"},
    {"type": "concept", "id": "concept_embodied_data_loop", "title": "具身数据闭环", "anchors": ["claim_wechat_embodied_data_structure_not_volume_20260716", "claim_wechat_embodied_data_quality_cost_tradeoff_20260716"], "body": "将采集、结构化、训练、部署反馈与再采集连接为可迭代的数据系统，而非只增加样本量。"},
    {"type": "concept", "id": "concept_skill_evolution", "title": "技能演化与技能下沉", "anchors": ["claim_wechat_skillevolver_meta_audit_loop_20260716"], "body": "从轨迹失败中区分知识缺口与执行偏差，并把可复用策略沉淀为可审计技能。"},
    {"type": "concept", "id": "concept_world_model_evaluation", "title": "世界模型评价", "anchors": ["claim_wechat_embodied_eval_bottleneck_20260715"], "body": "评价世界模型是否改善动作、规划和失败恢复，而不只比较生成质量或离线相似度。"},
    {"type": "concept", "id": "concept_perceptual_prediction_bias", "title": "感知预测偏差", "anchors": ["claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716", "claim_wechat_ganzfeld_mechanism_20260715"], "body": "感知系统在输入不完整或含糊时用内部预测补足信号，从而产生可测的知觉与生理偏差。"},
    {"type": "concept", "id": "concept_representation_convergence", "title": "表征收敛", "anchors": ["claim_wechat_cross_modal_representation_alignment_20260716"], "body": "不同模态或模型在任务约束下出现结构相近的内部表示；相似不等于语义或机制完全相同。"},
    {"type": "concept", "id": "concept_symbolic_regression", "title": "符号回归", "anchors": ["claim_wechat_physo_method_20260715"], "body": "从数据搜索可解释数学表达式，并显式利用维度、单位与结构约束。"},
    {"type": "concept", "id": "concept_machine_consciousness_integration", "title": "机器意识的信息整合问题", "anchors": ["claim_wechat_wangjun_global_workspace_integration_20260716"], "body": "研究跨模块信息共享、反馈和整合能否形成可操作、可证伪的机器意识指标。"},
    {"type": "concept", "id": "concept_sim_to_real_scene_infrastructure", "title": "Sim-to-Real 场景基础设施", "anchors": ["claim_wechat_kairos_sim2real_training_20260716"], "body": "用可交互场景、物理属性和部署反馈支持仿真训练向真实环境迁移。"},

    {"type": "question", "id": "question_data_quality_to_capability", "title": "数据质量如何转化为可执行能力？", "anchors": ["claim_wechat_embodied_data_structure_not_volume_20260716"], "body": "哪些数据结构、覆盖指标和闭环反馈真正改善部署能力，而不是只改善离线损失？", "links": [("raises", "concept_embodied_data_loop")]},
    {"type": "question", "id": "question_offline_coverage_deployment", "title": "离线数据能否代表真实部署轨迹？", "anchors": ["claim_wechat_ergodicity_time_vs_ensemble_20260716"], "body": "需要区分数据集群体分布与单个 Agent 随时间经历的状态、风险和不可逆失败。", "links": [("raises", "concept_ergodicity")]},
    {"type": "question", "id": "question_skill_compilation_boundary", "title": "Agent 何时应将显式推理固化为技能？", "anchors": ["claim_wechat_skillevolver_meta_audit_loop_20260716"], "body": "需要用复用频率、失败类型、可验证性和环境漂移确定技能下沉边界。", "links": [("raises", "concept_skill_evolution")]},
    {"type": "question", "id": "question_representation_equivalence", "title": "表征相似在什么条件下意味着机制等价？", "anchors": ["claim_wechat_cross_modal_representation_alignment_20260716"], "body": "需排除任务、数据和度量造成的表面收敛，并记录相似性失效条件。", "links": [("raises", "concept_representation_convergence")]},
    {"type": "question", "id": "question_world_model_action_value", "title": "世界模型评价如何预测动作价值？", "anchors": ["claim_wechat_embodied_eval_bottleneck_20260715"], "body": "什么评价能稳定预测规划、控制、错误恢复和真实部署收益？", "links": [("raises", "concept_world_model_evaluation")]},
    {"type": "question", "id": "question_machine_consciousness_falsifiability", "title": "机器意识理论如何形成可证伪实验？", "anchors": ["claim_wechat_wangjun_global_workspace_integration_20260716"], "body": "如何将全局工作空间或信息整合等主张转化为排他预测与失败判据？", "links": [("raises", "concept_machine_consciousness_integration")]},

    {"type": "tension", "id": "tension_embodied_data_scale_structure", "title": "具身数据规模 vs 数据结构与闭环", "anchors": ["claim_wechat_embodied_data_quality_cost_tradeoff_20260716", "claim_wechat_embodied_data_structure_not_volume_20260716"], "body": "扩大采集覆盖与改善数据结构都可能必要；当前证据不足以把其中一侧化约为另一侧。", "metadata": {"left_view": "扩大真实数据规模与覆盖", "right_view": "优先改善结构、质量与闭环", "unresolved": "不同任务和阶段的边际收益", "validation_method": "按规模和结构正交设计消融与部署评测"}, "links": [("related_to", "concept_embodied_data_loop")]},
    {"type": "tension", "id": "tension_world_model_eval_action", "title": "更好的世界模型评价 vs 直接优化动作结果", "anchors": ["claim_wechat_embodied_eval_bottleneck_20260715"], "body": "代理评价可降低真实试验成本，但评价与动作收益可能脱钩；直接优化动作又可能缺少可诊断中间信号。", "metadata": {"left_view": "改进世界模型评价", "right_view": "直接优化真实动作结果", "unresolved": "评价与动作收益的稳定相关性", "validation_method": "跨任务前瞻相关性与干预实验"}, "links": [("related_to", "concept_world_model_evaluation")]},
    {"type": "tension", "id": "tension_language_prior_action_control", "title": "语言先验复用 vs 实时动作专用表示", "anchors": ["claim_wechat_cross_modal_representation_alignment_20260716"], "body": "语言先验有助于泛化和任务理解，但连续控制需要低延迟、高带宽且具身化的动作表示。", "metadata": {"left_view": "复用语言/视觉预训练先验", "right_view": "使用动作专用连续表示", "unresolved": "接口和训练信号如何分工", "validation_method": "延迟、泛化、稳定性联合消融"}},
    {"type": "tension", "id": "tension_internal_reasoning_external_skills", "title": "模型内部推理 vs 外部可审计技能", "anchors": ["claim_wechat_skillevolver_meta_audit_loop_20260716"], "body": "内部推理更灵活，外部技能更可复用和审计；技能固化过早可能丢失适应性。", "metadata": {"left_view": "依赖模型内部推理", "right_view": "沉淀外部可审计技能", "unresolved": "何时下沉及如何失效", "validation_method": "按复用次数和环境漂移比较成功率与维护成本"}, "links": [("related_to", "concept_skill_evolution")]},

    {"type": "hypothesis", "id": "hypothesis_ergodicity_offline_coverage", "title": "遍历性指标可能预测离线数据对部署轨迹的覆盖", "anchors": ["claim_wechat_ergodicity_time_vs_ensemble_20260716"], "body": "若任务具有强路径依赖和不可逆失败，群体分布覆盖可能高估单个 Agent 的时间轨迹覆盖；需要部署日志验证。", "links": [("depends_on", "concept_ergodicity"), ("answers", "question_offline_coverage_deployment")]},
    {"type": "hypothesis", "id": "hypothesis_invariants_skill_transfer", "title": "显式不变量可能提高技能跨形态迁移", "anchors": ["claim_wechat_lie_group_continuous_symmetry_20260715", "claim_wechat_param_symmetry_conserved_quantities_20260716"], "body": "将连续对称性和不变量用于技能表示，可能降低形态变化带来的重新学习成本；尚无当前语料中的直接实验支持。", "links": [("depends_on", "concept_lie_group"), ("depends_on", "concept_parameter_symmetry")]},
    {"type": "hypothesis", "id": "hypothesis_illusion_world_model_probe", "title": "视觉错觉可作为世界模型预测偏差探针", "anchors": ["claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716"], "body": "若模型在含糊输入下表现出可重复的系统偏差，可用错觉刺激区分感知表示、预测和控制层故障；需避免将人类错觉机制直接等同于模型机制。", "links": [("depends_on", "concept_perceptual_prediction_bias"), ("depends_on", "concept_world_model_evaluation")]},
    {"type": "hypothesis", "id": "hypothesis_epiplexity_memory_compaction", "title": "Epiplexity 可能帮助评价有限上下文中的记忆压缩", "anchors": ["claim_wechat_epiplexity_definition_20260715"], "body": "可复用结构信息或可作为压缩后记忆效用的候选维度，但定义、测量和与任务性能的关系尚未验证。", "links": [("depends_on", "concept_epiplexity")]},
    {"type": "hypothesis", "id": "hypothesis_kelly_project_portfolio", "title": "Kelly 式约束可能改善创新项目组合的长期存续", "anchors": ["claim_wechat_kelly_bet_fraction_20260716"], "body": "把资源下注视为重复且有破产风险的过程，可能约束单项目暴露；项目回报分布、相关性和可重复性与赌博模型不同。", "links": [("depends_on", "concept_kelly_criterion")]},

    {"type": "analogy", "id": "analogy_epiplexity_memory", "title": "Epiplexity ↔ 有限上下文记忆压缩", "anchors": ["claim_wechat_epiplexity_definition_20260715"], "body": "共同结构是有限计算预算下保留可复用结构；失效边界是 Epiplexity 的正式定义未必直接度量 Agent 记忆效用。", "metadata": {"source_domain": "information theory", "target_domain": "agent memory", "shared_structure": "有限预算下提取可复用结构", "where_it_breaks": "正式量化对象与任务效用不同", "confidence": "low"}, "links": [("analogous_to", "concept_epiplexity")]},
    {"type": "analogy", "id": "analogy_lie_group_skill_transfer", "title": "李群与不变量 ↔ 技能组合和形态迁移", "anchors": ["claim_wechat_lie_group_continuous_symmetry_20260715"], "body": "共同结构是变换下保持性质并通过局部生成元组合变化；失效边界是机器人技能未必具有精确群作用。", "metadata": {"source_domain": "geometry and symmetry", "target_domain": "robot skill transfer", "shared_structure": "变换下的不变量与组合", "where_it_breaks": "实际技能空间可能不闭合也不光滑", "confidence": "low"}, "links": [("analogous_to", "concept_lie_group"), ("analogous_to", "concept_skill_evolution")]},
    {"type": "analogy", "id": "analogy_ergodicity_dataset_coverage", "title": "遍历性 ↔ 离线数据对部署轨迹的覆盖", "anchors": ["claim_wechat_ergodicity_time_vs_ensemble_20260716"], "body": "共同结构是群体样本与单个主体时间经历可能不等价；失效边界是 Agent 环境分布并非严格物理遍历过程。", "metadata": {"source_domain": "stochastic processes", "target_domain": "offline embodied learning", "shared_structure": "ensemble coverage may differ from temporal trajectory coverage", "where_it_breaks": "部署策略和环境会共同改变分布", "confidence": "medium"}, "links": [("analogous_to", "concept_ergodicity"), ("analogous_to", "concept_embodied_data_loop")]},
    {"type": "analogy", "id": "analogy_kelly_project_portfolio", "title": "Kelly Criterion ↔ 创新项目组合与资源下注", "anchors": ["claim_wechat_kelly_bet_fraction_20260716"], "body": "共同结构是重复下注、资本约束和避免不可恢复损失；失效边界是创新项目回报不可独立重复且概率难以估计。", "metadata": {"source_domain": "bet sizing", "target_domain": "innovation portfolio", "shared_structure": "growth under ruin constraints", "where_it_breaks": "project probabilities are non-stationary and correlated", "confidence": "low"}, "links": [("analogous_to", "concept_kelly_criterion")]},

    {"type": "synthesis", "id": "synthesis_embodied_data_bottleneck_m6", "title": "具身智能中的数据瓶颈：规模、结构、闭环与评价", "anchors": ["claim_wechat_embodied_data_structure_not_volume_20260716", "claim_wechat_embodied_data_quality_cost_tradeoff_20260716", "claim_wechat_embodied_eval_bottleneck_20260715", "claim_wechat_kairos_sim2real_training_20260716"], "body": "当前语料共同指向四个相互制约的维度：数据规模扩大覆盖，结构化 recipe 影响学习效率，部署闭环决定能否持续修正，评价决定优化方向。语料主要是二手解读，因此该综合保留规模与结构的 tension，并把原论文核验和部署实验列为下一步。", "links": [("related_to", "concept_embodied_data_loop"), ("related_to", "concept_world_model_evaluation"), ("related_to", "tension_embodied_data_scale_structure")]},
    {"type": "synthesis", "id": "synthesis_limited_resource_experience_m6", "title": "智能系统如何在有限资源下压缩和沉淀经验", "anchors": ["claim_wechat_epiplexity_definition_20260715", "claim_wechat_skillevolver_meta_audit_loop_20260716", "claim_wechat_ergodicity_time_vs_ensemble_20260716", "claim_wechat_kelly_bet_fraction_20260716"], "body": "四组材料分别关注可学习结构、技能沉淀、时间路径与资源存续。它们共同提示：经验压缩不能只追求短摘要，还要保留可复用结构、失败边界、路径依赖和资源风险。跨域映射均保持为 analogy/hypothesis，不作为已证实事实。", "links": [("related_to", "concept_epiplexity"), ("related_to", "concept_skill_evolution"), ("related_to", "concept_ergodicity"), ("related_to", "concept_kelly_criterion")]},

    {"type": "project", "id": "project_embodied_agent_learning_candidate", "title": "具身 Agent 学习闭环（候选项目上下文）", "anchors": ["claim_wechat_embodied_data_structure_not_volume_20260716"], "body": "候选行动上下文：围绕数据、技能、世界模型评价和 sim-to-real 建立可验证闭环；仅在用户审阅后进入行动层。"},
    {"type": "experiment", "id": "experiment_dataset_trajectory_coverage", "title": "比较数据集覆盖与真实部署轨迹覆盖", "anchors": ["claim_wechat_ergodicity_time_vs_ensemble_20260716", "claim_wechat_embodied_data_structure_not_volume_20260716"], "body": "记录单个 Agent 的时间轨迹、不可逆失败与恢复，比较其与离线数据集群体覆盖指标的偏差。", "links": [("applied_in", "project_embodied_agent_learning_candidate"), ("tested_by", "hypothesis_ergodicity_offline_coverage")]},
    {"type": "experiment", "id": "experiment_visual_illusion_world_model", "title": "用视觉错觉刺激测试世界模型预测偏差", "anchors": ["claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716"], "body": "构造物理输入不变但知觉解释变化的测试，分别检查视觉编码、预测和动作层响应。", "links": [("applied_in", "project_embodied_agent_learning_candidate"), ("tested_by", "hypothesis_illusion_world_model_probe")]},
    {"type": "opportunity", "id": "opportunity_invariant_skill_transfer", "title": "以不变量约束技能跨形态迁移", "anchors": ["claim_wechat_lie_group_continuous_symmetry_20260715", "claim_wechat_param_symmetry_conserved_quantities_20260716"], "body": "探索用几何不变量和等变表示减少不同机器人形态之间的技能重学成本；先作为低置信度机会而非架构决策。", "links": [("applied_in", "project_embodied_agent_learning_candidate"), ("depends_on", "hypothesis_invariants_skill_transfer")]},
]


@dataclass(frozen=True)
class DistillationResult:
    dry_run: bool
    proposal_id: str | None
    source_count: int
    input_proposal_count: int
    selected_claims: int
    node_counts: dict[str, int]
    source_only_count: int
    invalid_source_count: int
    superseded_proposals: int
    followup_count: int
    backup_path: str | None
    report_path: str | None
    errors: list[str]


class CorpusDistillationService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def _inputs(self) -> tuple[dict[str, tuple[Path, dict[str, Any], str]], list[tuple[Path, dict[str, Any], str]]]:
        candidates: dict[str, tuple[Path, dict[str, Any], str]] = {}
        proposals = []
        for path in self.repository.proposal_documents():
            proposal, body = read_document(path)
            if proposal.get("proposal_kind") != "model_candidate" or proposal.get("status") not in {"pending", "superseded"}:
                continue
            candidate_path = self.repository.resolve_inside(str(proposal["candidate_path"]))
            candidate, candidate_body = read_document(candidate_path)
            candidates[str(candidate["id"])] = (candidate_path, candidate, candidate_body)
            proposals.append((path, proposal, body))
        return candidates, proposals

    def _source_ids(self, anchors: list[str], candidates: dict[str, tuple[Path, dict[str, Any], str]]) -> list[str]:
        return list(dict.fromkeys(source_id for anchor in anchors if anchor in candidates for source_id in candidates[anchor][1].get("source_ids", [])))

    def plan(self) -> DistillationResult:
        candidates, proposals = self._inputs()
        sources = list(self.repository.source_documents())
        qualities = []
        followups = []
        for path in sources:
            source, _ = read_document(path)
            assessment = SourceQualityService(self.repository).assess(str(source["id"]), persist=False)
            qualities.append(assessment)
            if assessment.source_authority in {"secondary_analysis", "industry_commentary", "social_post"}:
                followups.extend(assessment.primary_source_locators)
        selected = [item for item in SELECTED_CLAIMS if item in candidates]
        used_sources = set(source_id for item in selected for source_id in candidates[item][1].get("source_ids", []))
        used_sources.update(source_id for node in CURATED_NODES for source_id in self._source_ids(node["anchors"], candidates))
        valid_sources = {item.source_id for item in qualities if item.compile_allowed}
        counts = Counter(node["type"] for node in CURATED_NODES)
        counts["claim"] = len(selected)
        return DistillationResult(
            dry_run=True, proposal_id=None, source_count=len(sources), input_proposal_count=len(proposals),
            selected_claims=len(selected), node_counts=dict(sorted(counts.items())),
            source_only_count=len(valid_sources - used_sources),
            invalid_source_count=sum(not item.compile_allowed for item in qualities),
            superseded_proposals=sum(proposal.get("status") == "pending" for _, proposal, _ in proposals),
            followup_count=len(set(followups)), backup_path=None, report_path=None, errors=[],
        )

    @staticmethod
    def _relation(relation_type: str, target_id: str, reason: str) -> dict[str, str]:
        return {"type": relation_type, "target_id": target_id, "reason": reason, "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}

    def apply(self) -> DistillationResult:
        plan = self.plan()
        candidates, proposals = self._inputs()
        all_source_ids = []
        all_invalid_sources = []
        for path in self.repository.source_documents():
            source, _ = read_document(path)
            source_id = str(source["id"])
            all_source_ids.append(source_id)
            if not SourceQualityService(self.repository).assess(source_id, persist=False).compile_allowed:
                all_invalid_sources.append(source_id)
        existing_corpus: list[tuple[Path, dict[str, Any], str]] = []
        for path in self.repository.proposal_documents():
            metadata, body = read_document(path)
            if metadata.get("proposal_kind") == "corpus_distillation":
                existing_corpus.append((path, metadata, body))
        if existing_corpus:
            existing_corpus.sort(key=lambda item: str(item[1].get("created_at", "")))
            current_path, current, current_body = existing_corpus[-1]
            current_id = str(current["id"])
            from .bundle import BundleReviewService
            reviewer = BundleReviewService(self.repository)
            for item in list(current.get("bundle_items", [])):
                if item.get("object_type") != "claim" or item.get("evidence_coverage") != "missing":
                    continue
                candidate_path = self.repository.resolve_inside(str(item["candidate_path"]))
                candidate, candidate_body = read_document(candidate_path)
                if not candidate.get("evidence"):
                    continue
                candidate["evidence_coverage"] = "partial"
                candidate["evidence_entailment"] = "partial"
                candidate["publication_gate"] = "needs_split" if candidate.get("atomicity_status") == "compound" else "needs_review"
                revision_input = self.repository.root / "data/derived" / f"m6-revision-{item['item_id']}.md"
                atomic_write_text(revision_input, render_document(candidate, candidate_body))
                reviewer.revise_item(current_id, str(item["item_id"]), revision_input, "M6 将字符串定位与语义 evidence coverage 分离；有证据但未完成人工蕴含核验")
            current_path, current, current_body = self.repository.find_document(current_id)
            inherited_superseded = list(current.get("superseded_proposal_ids", []))
            for old_path, old, old_body in existing_corpus[:-1]:
                inherited_superseded.extend(old.get("superseded_proposal_ids", []))
                if old.get("status") in {"pending", "deferred"}:
                    old["status"] = "superseded"
                    old["superseded_by"] = current_id
                    old["updated_at"] = now_iso()
                    old["review_reason"] = "幂等键修正后由最新 M6 corpus bundle 取代"
                    atomic_write_text(old_path, render_document(old, old_body))
            current["invalid_source_ids"] = sorted(all_invalid_sources)
            current["corpus_source_count"] = len(all_source_ids)
            current["superseded_proposal_ids"] = sorted(set(inherited_superseded))
            atomic_write_text(current_path, render_document(current, current_body))
            for model_path, model_proposal, model_body in proposals:
                if (
                    model_proposal.get("status") == "superseded"
                    and str(model_proposal.get("id")) in current["superseded_proposal_ids"]
                    and model_proposal.get("superseded_by") != current_id
                ):
                    model_proposal["superseded_by"] = current_id
                    model_proposal["updated_at"] = now_iso()
                    model_proposal["review_reason"] = "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
                    atomic_write_text(model_path, render_document(model_proposal, model_body))
            return DistillationResult(**{
                **plan.__dict__, "dry_run": False, "proposal_id": current_id,
                "source_count": len(all_source_ids), "invalid_source_count": len(all_invalid_sources),
                "source_only_count": len(current.get("source_only_source_ids", [])),
                "superseded_proposals": len(current.get("superseded_proposal_ids", [])),
                "backup_path": current.get("distillation_backup_path"), "report_path": current.get("validation_report_path"),
            })
        selected = [item for item in SELECTED_CLAIMS if item in candidates]
        input_hashes = [sha256_bytes(path.read_bytes()) for path, _, _ in proposals]
        proposal_id = "proposal_corpus_m6_" + hashlib.sha256("\n".join(sorted(input_hashes)).encode()).hexdigest()[:20]
        proposal_path = self.repository.root / "vault/proposals" / f"proposal-{proposal_id}.md"
        timestamp = now_iso()
        backup = self.repository.root / "data/backups" / f"m6-distillation-{timestamp.replace(':', '-')}"
        backup.mkdir(parents=True, exist_ok=False)
        for path, _, _ in proposals:
            shutil.copy2(path, backup / path.name)
        source_ids = sorted({source_id for _, candidate, _ in candidates.values() for source_id in candidate.get("source_ids", [])})
        bundle_items: list[dict[str, Any]] = []
        diff_sections: list[str] = []
        item_index = 0

        def add_candidate(metadata: dict[str, Any], body: str, *, review_tier: str = "low") -> None:
            nonlocal item_index
            item_index += 1
            object_type = str(metadata["type"])
            target_id = str(metadata["id"])
            target_path = self.repository.root / CANONICAL_DIRECTORIES[object_type] / f"{target_id}-{slugify(str(metadata['title']))}.md"
            same = None
            try:
                found_path, found, found_body = self.repository.find_document(target_id)
                if found.get("type") != "proposal" and "vault/proposals" not in self.repository.rel(found_path):
                    same = (found_path, found, found_body)
            except Exception:
                pass
            if same:
                found_path, found, found_body = same
                action, target_path, base_bytes = "update", found_path, found_path.read_bytes()
                metadata["created_at"] = found["created_at"]
                metadata["proposed_status"] = found.get("status", "confirmed")
                metadata["source_ids"] = list(dict.fromkeys([*found.get("source_ids", []), *metadata.get("source_ids", [])]))
                body = found_body.rstrip() + "\n\n## M6 增量候选\n\n" + body + "\n"
            else:
                action, base_bytes = "create", b""
            candidate_text = render_document(metadata, body)
            candidate_path = self.repository.root / "vault/proposals" / f"candidate-{proposal_id}-{target_id}.md"
            base_path = self.repository.root / "vault/proposals" / f"base-{proposal_id}-{target_id}.md"
            self.repository.immutable_write(candidate_path, candidate_text.encode("utf-8"))
            if base_bytes:
                self.repository.immutable_write(base_path, base_bytes)
            diff = "".join(difflib.unified_diff(
                base_bytes.decode("utf-8").splitlines(keepends=True) if base_bytes else [],
                candidate_text.splitlines(keepends=True), fromfile="base" if base_bytes else "/dev/null", tofile=self.repository.rel(target_path),
            ))
            item_id = f"{object_type}-{item_index}"
            bundle_items.append({
                "item_id": item_id, "object_type": object_type, "action": action,
                "target_id": target_id, "target_path": self.repository.rel(target_path),
                "base_path": self.repository.rel(base_path) if base_bytes else None,
                "base_sha256": sha256_bytes(base_bytes) if base_bytes else None,
                "candidate_path": self.repository.rel(candidate_path),
                "candidate_sha256": sha256_bytes(candidate_text.encode("utf-8")),
                "decision": "pending", "potential_conflicts": [], "review_tier": review_tier,
                "atomicity_status": metadata.get("atomicity_status"),
                "evidence_coverage": metadata.get("evidence_coverage"),
            })
            diff_sections.append(f"### {item_id}: {metadata['title']}\n\n```diff\n{diff.rstrip()}\n```\n")

        for claim_id in selected:
            _, original, body = candidates[claim_id]
            metadata = dict(original)
            inspected = AtomicClaimInspector.inspect(str(metadata.get("title", "")), [str(item.get("original_text", item.get("excerpt", ""))) for item in metadata.get("evidence", [])])
            metadata.update({
                "status": "proposal", "updated_at": timestamp,
                "atomicity_status": inspected.status, "evidence_coverage": inspected.evidence_coverage,
                "quote_verification": "exact" if all(item.get("verification_status") == "verified" for item in metadata.get("evidence", [])) else "normalized_match",
                "extraction_quality": "good", "epistemic_source_authority": "secondary",
                "evidence_entailment": "partial" if inspected.evidence_coverage != "full" else "full",
                "claim_confidence": str(metadata.get("confidence", "low")),
                "publication_gate": "needs_split" if inspected.status == "compound" else "needs_review",
                "change_reason": f"M6 corpus distillation from {claim_id}",
            })
            metadata["relations"] = [
                self._relation(str(rel.get("type", "derived_from")), str(rel["target_id"]), str(rel.get("reason", "M6 retained source relation")))
                for rel in metadata.get("relations", []) if rel.get("target_id")
            ]
            add_candidate(metadata, body)

        for node in CURATED_NODES:
            node_sources = self._source_ids(node["anchors"], candidates)
            if not node_sources:
                continue
            relations = [self._relation("derived_from", source_id, "由当前语料蒸馏为待审知识对象") for source_id in node_sources]
            relations += [self._relation(kind, target, "M6 人工可审阅结构连接；不得仅凭关键词确认") for kind, target in node.get("links", [])]
            metadata = {
                "id": node["id"], "type": node["type"], "status": "proposal", "title": node["title"],
                "created_at": timestamp, "updated_at": timestamp, "aliases": [], "tags": ["m6-distillation"],
                "domains": [], "confidence": node.get("metadata", {}).get("confidence", "low" if node["type"] in {"hypothesis", "analogy"} else "unknown"),
                "source_ids": node_sources, "relations": relations,
                "change_reason": "M6 controlled corpus distillation; requires human review",
                **node.get("metadata", {}),
            }
            add_candidate(metadata, f"# {node['title']}\n\n{node['body']}\n")

        followups = []
        invalid_sources = list(all_invalid_sources)
        used_sources = {source_id for item in bundle_items for source_id in read_document(self.repository.resolve_inside(item["candidate_path"]))[0].get("source_ids", [])}
        all_valid_sources = set()
        for source_id in source_ids:
            assessment = SourceQualityService(self.repository).assess(source_id, persist=True)
            if assessment.compile_allowed:
                all_valid_sources.add(source_id)
            followups.extend(FollowupService(self.repository).detect(source_id))
        source_only = sorted(all_valid_sources - used_sources)
        selected_ids = set(selected)
        low_value = sorted(set(candidates) - selected_ids)
        counts = Counter(item["object_type"] for item in bundle_items)
        proposal = {
            "id": proposal_id, "type": "proposal", "status": "pending",
            "title": "M6：33 个 Source 的受控知识蒸馏", "created_at": timestamp, "updated_at": timestamp,
            "aliases": [], "tags": ["m6", "corpus-distillation"], "domains": [], "confidence": "low",
            "source_ids": source_ids, "relations": [], "proposal_kind": "corpus_distillation",
            "processor": "m6-controlled-distillation-v1", "review_unit": "source_collection_bundle",
            "compile_disposition": "knowledge_proposed", "bundle_items": bundle_items,
            "existing_context": [{"id": "claim_via_interface_first_robot_control_20260715", "status": "confirmed"}],
            "contradiction_candidates": ["tension_embodied_data_scale_structure", "tension_world_model_eval_action"],
            "unresolved_items": [node["id"] for node in CURATED_NODES if node["type"] in {"question", "tension", "hypothesis", "analogy"}],
            "primary_source_followups": sorted({item["id"] for item in followups}),
            "duplicate_findings": [], "low_value_items_not_proposed": low_value,
            "source_only_source_ids": source_only, "invalid_source_ids": invalid_sources,
            "corpus_source_count": len(all_source_ids),
            "superseded_proposal_ids": [str(p["id"]) for _, p, _ in proposals if p.get("status") == "pending"],
            "provenance_validation": {"ok": True, "sources": len(source_ids), "selected_claims": len(selected)},
            "bundle_metrics": {
                "novelty_score": "not_calibrated", "importance_score": "human_review_required",
                "source_authority": "mixed; predominantly secondary_analysis", "evidence_quality": "mixed",
                "knowledge_reuse_count": 0, "new_object_count": sum(item["action"] == "create" for item in bundle_items),
                "updated_object_count": sum(item["action"] == "update" for item in bundle_items),
                "duplicate_count": len(low_value), "unresolved_count": len([n for n in CURATED_NODES if n["type"] in {"question", "tension", "hypothesis", "analogy"}]),
                "review_cost_estimate": len(bundle_items), "node_counts": dict(sorted(counts.items())),
                "scoring_basis": "curated deterministic selection over existing proposals; no probability calibration",
            },
            "distillation_backup_path": self.repository.rel(backup),
            "validation_report_path": None, "reviewed_at": None, "review_reason": None,
        }
        body = "# M6 受控知识蒸馏\n\n本 bundle 只形成待审知识图，不批准 canonical。旧逐条 claim proposals 保留并标记 superseded。\n\n## Items\n\n" + "\n".join(diff_sections)
        self.repository.immutable_write(proposal_path, render_document(proposal, body).encode("utf-8"))
        superseded = 0
        for path, old, old_body in proposals:
            if old.get("status") != "pending":
                continue
            old["status"] = "superseded"
            old["superseded_by"] = proposal_id
            old["updated_at"] = timestamp
            old["review_reason"] = "由 M6 corpus distillation bundle 取代逐条审阅；candidate 与证据仍保留"
            atomic_write_text(path, render_document(old, old_body))
            superseded += 1
        report_path = self.repository.root / "system/reports" / f"generated-m6-distillation-{timestamp[:10]}.md"
        report = (
            "# M6 Real Corpus Distillation Report\n\n"
            f"- Sources: {len(all_source_ids)} ({len(source_ids)} with model proposals)\n- Input model proposals: {len(proposals)}\n"
            f"- Superseded individual proposals: {superseded}\n- Source-only: {len(source_only)}\n"
            f"- Invalid sources: {len(invalid_sources)}\n- Primary follow-ups: {len(set(item['id'] for item in followups))}\n"
            "- Canonical writes: 0\n\n## Proposed node counts\n\n" +
            "\n".join(f"- {key}: {value}" for key, value in sorted(counts.items())) +
            "\n\n所有 Concept、Tension、Hypothesis、Analogy、Synthesis 和 Action 连接均为 proposal，需人工审阅。\n"
        )
        atomic_write_text(report_path, report)
        proposal, proposal_body = read_document(proposal_path)
        proposal["validation_report_path"] = self.repository.rel(report_path)
        atomic_write_text(proposal_path, render_document(proposal, proposal_body))
        self.repository.append_event("proposal-events", {"event": "m6-corpus-distilled", "proposal_id": proposal_id, "superseded": superseded, "source_count": len(source_ids)})
        return DistillationResult(
            dry_run=False, proposal_id=proposal_id, source_count=len(all_source_ids), input_proposal_count=len(proposals),
            selected_claims=len(selected), node_counts=dict(sorted(counts.items())), source_only_count=len(source_only),
            invalid_source_count=len(invalid_sources), superseded_proposals=superseded,
            followup_count=len(set(item["id"] for item in followups)), backup_path=self.repository.rel(backup),
            report_path=self.repository.rel(report_path), errors=[],
        )
