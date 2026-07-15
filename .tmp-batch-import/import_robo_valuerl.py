from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_7b278ba348f2a8bb94cce1fc"
EXT = "extraction_a288c4114d2d830f1678fd14"
_, extraction, body = ExtractionService(repo).find(EXT)
input_sha256 = extraction["input_sha256"]
content_id = extraction["content_id"]


def quote(text: str, section: str, reason: str) -> dict:
    start = body.index(text)
    end = start + len(text)
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


def para(section: str, interpretation: str, reason: str) -> dict:
    return {
        "evidence_id": f"evp_{abs(hash(section)) % 100000}",
        "evidence_kind": "paraphrase",
        "source_id": SRC,
        "input_sha256": input_sha256,
        "section": section,
        "interpretation": interpretation,
        "stance": "context",
        "verification_status": "verified",
        "reason": reason,
    }


REL = [
    {
        "type": "derived_from",
        "target_id": SRC,
        "reason": "由 Robo-ValueRL 官方项目页归纳；非独立 peer-reviewed 论文正文",
    }
]

candidates = [
    (
        {
            "id": "claim_robo_valuerl_pipeline_20260715",
            "title": "Robo-ValueRL 项目页称该方法把价值估计、质量条件策略学习与残差在线适应串联为 offline-to-online 流水线",
            "tags": ["offline-to-online-rl", "value-function", "robotics"],
            "domains": ["robot-learning", "robotics"],
            "confidence": "medium",
            "applicability": [
                "GeWu-Lab 官方项目页自述的方法概述",
                "真实机器人 offline-to-online RL 设定",
            ],
            "uncertainty": "来源是项目 landing page 而非 arXiv/PDF 正文；页面写 Citation will be updated after the arXiv release；演示视频多为 placeholder，不能当作已发表实验细节。",
            "evidence": [
                quote(
                    "The framework links value estimation, quality-conditioned policy learning, and residual online adaptation in one offline-to-online pipeline.",
                    "Methodology",
                    "项目页对三模块流水线结构的直接陈述。",
                ),
                quote(
                    "Robo-ValueRL studies how value-function reliability shapes offline-to-online robotic reinforcement learning.",
                    "Intro",
                    "项目页对研究问题的表述。",
                ),
                para("Citation", "项目页尚未给出正式 arXiv 引用", "提醒来源层级低于原始论文。"),
            ],
        },
        "# Robo-ValueRL 方法流水线\n\n三模块：history-conditioned value → quality-conditioned policy → online residual adaptation。",
    ),
    (
        {
            "id": "claim_robo_valuerl_chip_insertion_20260715",
            "title": "Robo-ValueRL 项目页报告真实机器人毫米级芯片插入任务最终成功率 86%",
            "tags": ["real-robot", "insertion", "manipulation"],
            "domains": ["robotics"],
            "confidence": "medium",
            "applicability": [
                "项目页 Chip Insertion 任务描述",
                "Millimeter-level chip insertion 测试床",
                "真实机器人 rollout",
            ],
            "uncertainty": "86% 来自项目页 headline 数字，未给出 trial 数、置信区间或实验协议；PDF/论文未 capture，不能外推为独立复现结果。",
            "evidence": [
                quote("86% final success", "Task Videos / Chip Insertion", "项目页对该任务最终成功率的直接标注。"),
                quote(
                    "The robot grasps a PCB, adjusts it to a feasible insertion pose, then grasps and inserts a chip into millimeter-scale clearance.",
                    "Chip Insertion 任务描述",
                    "限定任务为毫米级间隙插入。",
                ),
            ],
        },
        "# 芯片插入 86%\n\n项目页 reported final success。",
    ),
    (
        {
            "id": "claim_robo_valuerl_block_disassembly_20260715",
            "title": "Robo-ValueRL 项目页报告真实机器人可泛化方块拆解任务最终成功率 84%",
            "tags": ["real-robot", "generalization", "manipulation"],
            "domains": ["robotics"],
            "confidence": "medium",
            "applicability": ["Block Disassembly 测试床", "随机放置方块与随机 plate 布局"],
            "uncertainty": "84% 同样仅来自项目页；Generalizable 为项目页用语，未给出对照基线或 seed 数。",
            "evidence": [
                quote("84% final success", "Task Videos / Block Disassembly", "项目页对该任务最终成功率的直接标注。"),
                quote(
                    "The robot disassembles randomly placed blocks and sorts them into color-matched plates under randomized plate layouts.",
                    "Block Disassembly 任务描述",
                    "描述泛化压力来自随机布局。",
                ),
            ],
        },
        "# 方块拆解 84%\n\n项目页 reported final success。",
    ),
    (
        {
            "id": "claim_robo_valuerl_data_scale_20260715",
            "title": "Robo-ValueRL 项目页称使用约 240 小时离线演示与 3000+ 在线 rollout，并报告 chip/block 离线预训练增益 +26% / +34%",
            "tags": ["offline-to-online-rl", "data-scale"],
            "domains": ["robot-learning"],
            "confidence": "low",
            "applicability": [
                "项目页 Results 区块",
                "240h offline demonstrations",
                "3000+ online rollout trajectories",
            ],
            "uncertainty": "+26%/+34% 的基线与计算方式在项目页未定义；240h/3000+ 为项目自述规模，未经第三方核验；arXiv 未 release。",
            "evidence": [
                quote(
                    "Across 240 hours of offline demonstrations and over 3,000 online rollout trajectories, reliable value estimates support stronger offline scaling and more stable online improvement.",
                    "Results",
                    "规模与价值估计作用的综合陈述。",
                ),
                quote("+26%", "Results / chip offline gain", "项目页 chip 离线增益 headline。"),
                quote("+34%", "Results / block offline gain", "项目页 block 离线增益 headline。"),
            ],
        },
        "# 数据规模与离线增益\n\n项目页 headline 数字。",
    ),
]

out_dir = Path(".tmp-batch-import")
out_dir.mkdir(exist_ok=True)
prompt = out_dir / "prompt-knowledge-import.md"
svc = ProposalService(repo)

for meta, body_text in candidates:
    meta = {
        **meta,
        "type": "claim",
        "status": "proposal",
        "created_at": "2026-07-15T17:30:00+08:00",
        "updated_at": "2026-07-15T17:30:00+08:00",
        "aliases": [],
        "superseded_by": None,
        "valid_during": None,
        "change_reason": "批量导入项目页知识；等待人工核验",
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
        "项目页数字与协议未完整披露；非 peer-reviewed 正文。",
        f"导入 {meta['id']}",
        prompt if prompt.is_file() else None,
    )
    print(result.proposal_id, meta["id"])
