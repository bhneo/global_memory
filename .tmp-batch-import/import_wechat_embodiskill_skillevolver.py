from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_d01f40e4896de2e186cbbe8a"
EXT = "extraction_86edc5111c5d99c3f9f2bf7c"
_, extraction, body = ExtractionService(repo).find(EXT)
input_sha256 = extraction["input_sha256"]
content_id = extraction["content_id"]


def quote_between(start_marker: str, end_marker: str, section: str, reason: str) -> dict:
    start = body.index(start_marker)
    end = body.index(end_marker, start) + len(end_marker)
    text = body[start:end]
    return {
        "evidence_id": f"ev_{start}",
        "evidence_kind": "quote",
        "source_id": SRC,
        "content_id": content_id,
        "extraction_id": EXT,
        "input_sha256": input_sha256,
        "span_start": start,
        "span_end": end,
        "original_text": text,
        "section": section,
        "stance": "supports",
        "verification_status": "verified",
        "reason": reason,
    }


REL = [
    {
        "type": "derived_from",
        "target_id": SRC,
        "reason": "Gavin AI 记事本解读 EmbodiSkill (2605.10332) 与 SkillEvolver (2605.10500)；原论文未 capture",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_embodiskill_skillevolver_fork_20260716",
                "title": "该文称 EmbodiSkill 与 SkillEvolver 代表技能自进化两条分叉：前者区分技能缺陷 vs 执行偏差归因，后者把技能写作变成可审计的 meta-skill 在线学习",
                "tags": ["skill-evolution", "EmbodiSkill", "SkillEvolver"],
                "domains": ["agent-systems", "robotics"],
                "confidence": "medium",
                "applicability": ["2026-05-11 同期 arXiv 论文对比", "外部 skill 资产 vs 权重更新"],
                "uncertainty": "为博客综述；系统边界对比为作者归纳。",
                "evidence": [
                    quote_between(
                        "EmbodiSkill 解决",
                        "ExecutionLapse",
                        "EmbodiSkill 定位",
                        "文内摘要中对 EmbodiSkill 问题定义。",
                    ),
                    quote_between(
                        "SkillEvolver 解决",
                        "meta-skill",
                        "SkillEvolver 定位",
                        "文内摘要中对 SkillEvolver 问题定义。",
                    ),
                ],
            },
            "# 两条分叉\n\nskill 是外部可读可改程序性知识；Update 需结构化非自由反思。",
        ),
        (
            {
                "id": "claim_wechat_embodiskill_body_appendix_attribution_20260716",
                "title": "该文介绍 EmbodiSkill 将 skill 拆为 S_body 与 S_app：Discovery/Optimization/SkillDefect 可改正文，ExecutionLapse 仅更新附录强调执行遵守",
                "tags": ["skill-aware-reflection", "embodied-agents", "attribution"],
                "domains": ["agent-systems", "robotics"],
                "confidence": "medium",
                "applicability": ["冻结 executor 仅演化外部 skill", "revision buffer 分区更新"],
                "uncertainty": "算法细节来自论文转述；K=1 等超参需回 arXiv:2605.10332。",
                "evidence": [
                    quote_between(
                        "S_body",
                        "S_app",
                        "skill 二分",
                        "文内对 skill 正文与附录的形式化拆分。",
                    ),
                    quote_between(
                        "ExecutionLapse",
                        "不能改正文",
                        "执行偏差处理",
                        "文内对 ExecutionLapse 不可改正文的规则。",
                    ),
                ],
            },
            "# EmbodiSkill 归因\n\nSkill-Aware Evolution Spiral：执行→轨迹→归因→定向修订。",
        ),
        (
            {
                "id": "claim_wechat_embodiskill_alfworld_results_20260716",
                "title": "该文报告 EmbodiSkill 在 ALFWorld 上达 93.28% 成功率（冻结 Qwen3.5-27B executor + GPT-5.2 演化 skill），消融显示 skill-aware 归因由 78.36% 提至 93.28%",
                "tags": ["ALFWorld", "benchmark", "ablation"],
                "domains": ["agent-systems", "evaluation"],
                "confidence": "medium",
                "applicability": ["vs G-Memory 74.62%", "Puttwo 100% 叙述"],
                "uncertainty": "数字来自博客转述 Ju et al. 2026；GPT-5.2 等命名需回原文核验。",
                "evidence": [
                    quote_between(
                        "93.28%",
                        "70.89%",
                        "ALFWorld 主结果",
                        "文内对 EmbodiSkill 与 direct agent 成功率对比。",
                    ),
                    quote_between(
                        "Skill-unaware evolution",
                        "93.28%",
                        "消融对比",
                        "文内同 executor 消融：skill-unaware 78.36% vs EmbodiSkill 93.28%。",
                    ),
                ],
            },
            "# EmbodiSkill 实验\n\nEB-Habitat/Navigation 亦报告超 memory baseline 双位数百分点。",
        ),
        (
            {
                "id": "claim_wechat_skillevolver_meta_audit_loop_20260716",
                "title": "该文介绍 SkillEvolver 四步循环：K=4 策略探索→对比轨迹补丁→独立 Auditor 门控；Auditor 含 silent-bypass 等检查技能是否被下游 Agent 实际调用",
                "tags": ["SkillEvolver", "auditor", "CLI-agent"],
                "domains": ["agent-systems", "software-engineering"],
                "confidence": "medium",
                "applicability": ["Domain-Skill Agent 与 SkillEvolver Agent 分离", "Patch 禁止硬编码训练实例"],
                "uncertainty": "9 类 Auditor 检查为论文转述；需回 arXiv:2605.10500。",
                "evidence": [
                    quote_between(
                        "strategy-diversified exploration",
                        "K = 4",
                        "策略探索",
                        "文内对多策略探索步骤的说明。",
                    ),
                    quote_between(
                        "silent-bypass",
                        "fresh agent",
                        "silent-bypass 检查",
                        "文内对第 9 类 Auditor 检查的描述。",
                    ),
                ],
            },
            "# SkillEvolver 流程\n\ncontrastive update + surgical patch + independent audit。",
        ),
        (
            {
                "id": "claim_wechat_skillevolver_skillsbench_results_20260716",
                "title": "该文报告 SkillEvolver R=2 在 SkillsBench 验证集 avg@5 达 56.87%，超 human-curated 43.6%；R=1→R=2 增 8.7pp，下游 token/turns/wall-clock 约降 15–24%",
                "tags": ["SkillsBench", "meta-skill", "efficiency"],
                "domains": ["agent-systems", "evaluation"],
                "confidence": "medium",
                "applicability": ["83 任务 15+ 领域", "R=2 成本 3.92 USD/task"],
                "uncertainty": "Claude Opus 4.6 配置与数字需回原文；KernelBench 3 任务探针作者称不可过度解读。",
                "evidence": [
                    quote_between(
                        "SkillEvolver R=2:",
                        "56.87%",
                        "SkillsBench 主结果",
                        "文内对比表格 R=2 聚合成功率。",
                    ),
                    quote_between(
                        "tokens:",
                        "wall-clock:-23.8%",
                        "下游效率",
                        "文内对 evolved skill 降低下游成本的三项指标。",
                    ),
                ],
            },
            "# SkillEvolver 实验\n\none-shot Self-Gen 32% 未明显超 no-skill 29.9%。",
        ),
    ]


def main() -> None:
    out_dir = Path(".tmp-batch-import")
    out_dir.mkdir(exist_ok=True)
    prompt = out_dir / "prompt-knowledge-import.md"
    svc = ProposalService(repo)

    for meta, body_text in build_candidates():
        meta = {
            **meta,
            "type": "claim",
            "status": "proposal",
            "created_at": "2026-07-16T11:16:00+08:00",
            "updated_at": "2026-07-16T11:16:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入 EmbodiSkill/SkillEvolver 综述；等待人工核验",
            "source_ids": [SRC],
            "relations": REL,
        }
        path = out_dir / f"candidate-{meta['id']}.md"
        path.write_text(render_document(meta, body_text), encoding="utf-8")
        result = svc.propose_model_candidate(
            SRC,
            path,
            "cursor",
            "composer-2.5",
            "knowledge-import-v2",
            "博客转述 2605.10332/2605.10500；benchmark 数字需回 arXiv 原文核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
