from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_0a113baae7ce4d1ab78da1a3"
EXT = "extraction_c6ecc197e026c4f58b633b83"
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
        "reason": "由杜伦文/青稞具身智能专栏归纳；引述 RT-2、Re-Mix、Covariant 等为二手分析",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_embodied_data_structure_not_volume_20260716",
                "title": "该文主张机器人瓶颈不只是数据量，而是把数据转化为能力的结构与 recipe",
                "tags": ["embodied-ai", "data-infrastructure", "training-recipe"],
                "domains": ["robotics", "machine-learning"],
                "confidence": "low",
                "applicability": ["Joe Harris 推文引述语境", "部署日志 vs 模型训练数据割裂讨论"],
                "uncertainty": "为作者观点文；「不缺数据」论断依赖 anecdote，非系统统计。",
                "evidence": [
                    quote_between(
                        "机器人不缺数据",
                        "能力的结构",
                        "核心论点",
                        "文内开篇对问题重定义的表述。",
                    ),
                    quote_between(
                        "TB 级传感器日志",
                        "可用的基础设施",
                        "Joe Harris",
                        "文内引述 Joe Harris 对缺基础设施的判断。",
                    ),
                ],
            },
            "# 结构 vs 数量\n\n缺的是把数据变成能力的结构，非单纯缺 TB 日志。",
        ),
        (
            {
                "id": "claim_wechat_rt2_vlm_prior_not_robot_scaling_20260716",
                "title": "该文以 RT-2 为例称关键在联网规模 VLM 先验加有限机器人示范，而非继续堆机器人数据",
                "tags": ["rt-2", "vla", "pretraining"],
                "domains": ["robotics", "machine-learning"],
                "confidence": "medium",
                "applicability": ["RT-2 / Open X-Embodiment 案例讨论", "robotics scaling 变量辨析"],
                "uncertainty": "为作者对 DeepMind 博客的解读；与原始论文细节需回原文核验。",
                "evidence": [
                    quote_between(
                        "RT-2",
                        "关系不大",
                        "RT-2 案例",
                        "文内对 RT-2 数据量与能力来源的分析。",
                    ),
                    quote_between(
                        "web 预训练",
                        "机器人示范数据",
                        "VLM 先验",
                        "文内对 RT-2 训练组成的归纳。",
                    ),
                ],
            },
            "# RT-2 启示\n\n互联网 VLM 先验 + 有限动作数据；非纯 robot data scaling。",
        ),
        (
            {
                "id": "claim_wechat_remix_domain_weighting_20260716",
                "title": "该文引 Re-Mix 称学习到的 domain weight 比均匀混合高 38%，说明数据混合/recipe 比总量更关键",
                "tags": ["re-mix", "data-mixing", "open-x-embodiment"],
                "domains": ["robotics", "machine-learning"],
                "confidence": "medium",
                "applicability": ["Open X-Embodiment 混合策略讨论", "错误混数据可能比缺数据更糟语境"],
                "uncertainty": "38%/32% 数字来自作者转述 2024 Re-Mix 论文；原论文未 capture。",
                "evidence": [
                    quote_between(
                        "Re-Mix",
                        "高 38%",
                        "Re-Mix 结果",
                        "文内对 Re-Mix domain weight 提升的引述。",
                    ),
                    quote_between(
                        "均匀混合",
                        "高 32%",
                        "相对人工权重",
                        "文内对比 learned vs uniform/manual mixing。",
                    ),
                ],
            },
            "# Re-Mix\n\n混合权重/recipe 影响大；非仅数据总量。",
        ),
        (
            {
                "id": "claim_wechat_embodied_data_four_layers_20260716",
                "title": "该文将具身数据基础设施分为可视化、目录检索、标注供给与评测训练闭环四层，称最内层闭环最难外包",
                "tags": ["data-platform", "evaluation", "foxglove"],
                "domains": ["robotics", "data-engineering"],
                "confidence": "low",
                "applicability": ["Foxglove/Rerun/Scale 产品层定位讨论", "头部公司自建系统原因分析"],
                "uncertainty": "四层框架为作者构造；与 Joe Harris 观点的延伸，非行业标准 taxonomy。",
                "evidence": [
                    quote_between(
                        "Foxglove",
                        "几分钟就能做完",
                        "可视化层",
                        "文内对最外层观测/调试层的说明。",
                    ),
                    quote_between(
                        "评测与训练闭环",
                        "改不动模型",
                        "最内层瓶颈",
                        "文内对第四层为核心卡点的判断。",
                    ),
                ],
            },
            "# 四层基础设施\n\n可见→可找→可标注→评测闭环；内层最难外包。",
        ),
        (
            {
                "id": "claim_wechat_physical_world_generalization_walls_20260716",
                "title": "该文称即使 recipe 正确，物理世界仍有评测不稳定、环境变异性、长程记忆与在线精度等 LLM 未遇瓶颈",
                "tags": ["generalization", "evaluation", "online-adaptation"],
                "domains": ["robotics", "embodied-ai"],
                "confidence": "low",
                "applicability": ["Levine AutoEval、Finn DROID、PI Memory/RLT 引述语境", "闭环控制 vs 开环录像类比"],
                "uncertainty": "为综述性观点；具体 PI 项目细节为作者解读，需回原始材料。",
                "evidence": [
                    quote_between(
                        "开环轨迹",
                        "闭环世界",
                        "闭环 vs 开环",
                        "文内对机器人控制与录像本质差异的说明。",
                    ),
                    quote_between(
                        "cook shrimp",
                        "kitchen",
                        "Finn 引述",
                        "文内对跨厨房迁移困难的 Finn 引述。",
                    ),
                    quote_between(
                        "在线改进",
                        "执行本身",
                        "在线适应",
                        "文内对 RLT/在线修正必要性的说明。",
                    ),
                ],
            },
            "# 物理世界之墙\n\n评测/变异性/记忆/精度/在线适应；非 LLM 式 scaling。",
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
            "created_at": "2026-07-16T01:19:00+08:00",
            "updated_at": "2026-07-16T01:19:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入具身数据问题分析文；等待人工核验",
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
            "观点/分析文；Re-Mix/RT-2 等数字需回论文；含融资叙事批判。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
