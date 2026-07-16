from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_9bd3bdfb9a5b1a728c3adf25"
EXT = "extraction_275083c46743bccdd54985ba"
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
        "reason": "由中科院物理所转载的等离子体/磁约束科普文章归纳；非原始实验论文",
    }
]

candidates = [
    (
        {
            "id": "claim_wechat_plasma_universe_fraction_20260715",
            "title": "该文称等离子体为物质第四态，且在宇宙可见物质中占比超过 99.9%",
            "tags": ["plasma", "astrophysics", "fourth-state"],
            "domains": ["physics", "plasma-physics"],
            "confidence": "medium",
            "applicability": ["大学物理学/中科院物理所科普语境", "可见宇宙物质组成的一般性描述"],
            "uncertainty": "99.9% 为科普常用数量级表述，精确比例依测量与定义边界而异；非 peer-reviewed 原文。",
            "evidence": [
                quote_between(
                    "作为物质的第四态，等离子体物质",
                    "典型的如恒星物质。",
                    "等离子体定义",
                    "文内对等离子体组成与宇宙占比的描述。",
                ),
            ],
        },
        "# 等离子体占比\n\n第四态；可见宇宙物质 >99.9% 为等离子体。",
    ),
    (
        {
            "id": "claim_wechat_plasma_temperature_range_20260715",
            "title": "该文称等离子体温度跨度很大：低温等离子体可仅几十摄氏度，聚变点火温度可达上亿度",
            "tags": ["plasma", "fusion", "temperature"],
            "domains": ["physics", "plasma-physics"],
            "confidence": "medium",
            "applicability": ["文内对等离子体电视与太阳核心/聚变点火的对比", "温度数量级科普"],
            "uncertainty": "「几乎没有上限」为修辞；50mK 超冷等离子体案例引自 2009 Science 报道但未 capture 原文。",
            "evidence": [
                quote_between(
                    "低温等离子体只有几十度",
                    "例如等离子体电视屏幕。",
                    "低温等离子体",
                    "文内低温等离子体例子。",
                ),
                quote_between(
                    "太阳中心温度高达1500万度",
                    "更是高达上亿度。",
                    "高温等离子体",
                    "文内对恒星与聚变点火温度的数量级。",
                ),
                quote_between(
                    "Science就曾报道了一种处在50mK低温的等离子体",
                    "通过对超冷原子光电离得到的。",
                    "超冷等离子体",
                    "文内对 2009 人造超冷等离子体的转述。",
                ),
            ],
        },
        "# 等离子体温度范围\n\n几十度到上亿度的跨度。",
    ),
    (
        {
            "id": "claim_wechat_magnetic_bottle_constraint_20260715",
            "title": "该文称不均匀「磁瓶/磁镜」磁场可通过磁矩近似守恒约束带电粒子纵向与横向运动",
            "tags": ["magnetic-confinement", "magnetic-mirror", "plasma"],
            "domains": ["physics", "plasma-physics"],
            "confidence": "medium",
            "applicability": ["高中/大学物理磁约束概念介绍", "两头强中间弱的不均匀磁场结构"],
            "uncertainty": "为科普化推导，文内自述「不容易但可以证明」磁矩守恒；高速纵向粒子仍可能从磁瓶端逃逸。",
            "evidence": [
                quote_between(
                    "当不均匀的磁场呈现两头强中间弱时",
                    "因此这种磁场结构被形象的称作为磁瓶。",
                    "磁瓶结构",
                    "文内对磁瓶命名的物理图像。",
                ),
                quote_between(
                    "粒子的纵向和横向的运动都受到限制",
                    "这就是“磁约束”一词的由来！",
                    "磁约束结论",
                    "文内对纵向/横向运动受限的总结。",
                ),
                quote_between(
                    "然而，磁瓶并不完美",
                    "从磁瓶两端逃逸。",
                    "磁镜泄漏",
                    "文内对高纵向速度粒子逃逸的限制说明。",
                ),
            ],
        },
        "# 磁瓶约束\n\n磁矩近似守恒限制粒子；高速粒子可逃逸。",
    ),
    (
        {
            "id": "claim_wechat_tokamak_fusion_device_20260715",
            "title": "该文称托卡马克为磁约束聚变主选装置，苏联 1950 年代发明，运行温度约 1.5–3 亿摄氏度",
            "tags": ["tokamak", "fusion", "iter"],
            "domains": ["physics", "energy"],
            "confidence": "medium",
            "applicability": ["文内对托卡马克历史与工作原理的概述", "ITER 等实验堆语境"],
            "uncertainty": "「最有希望」「目前尚未用于能源生产」为 2022 年科普时点判断；ITER 进展需独立更新。",
            "evidence": [
                quote_between(
                    "该设备最初由苏联的研究人员于上世纪50年代发明",
                    "它也是一种螺旋形状磁场。",
                    "托卡马克起源",
                    "文内对托卡马克发明与磁场合成的描述。",
                ),
                quote_between(
                    "利用辅助加热系统将温度提高到聚变所需的水平（1.5-3亿摄氏度）",
                    "使其聚合并释放出大量能量。",
                    "运行温度",
                    "文内给出的托卡马克等离子体温度范围。",
                ),
                quote_between(
                    "由于启动和维持聚变反应的能量门槛太高",
                    "有望能逐步实现这一目标。",
                    "能源应用状态",
                    "文内对托卡马克尚未商用与 ITER 期望的表述。",
                ),
            ],
        },
        "# 托卡马克\n\n1950 年代苏联发明；1.5–3 亿°C；ITER 候选。",
    ),
    (
        {
            "id": "claim_wechat_stellarator_vs_tokamak_20260715",
            "title": "该文称全球约有 60 台托克马克与 10 台仿星器运行，且两者在保温与稳定性上各有优劣",
            "tags": ["stellarator", "tokamak", "fusion"],
            "domains": ["physics", "energy"],
            "confidence": "low",
            "applicability": ["2022 科普文对全球聚变装置数量的概述", "仿星器扭转螺旋磁场的约束思路"],
            "uncertainty": "60/10 台数量为文内单点统计，随新建/退役装置变化；优劣对比为概括性说法。",
            "evidence": [
                quote_between(
                    "基于以上这种扭转磁场的装置被称作仿星器（stellarator）",
                    "重要的反应堆设备候选者。",
                    "仿星器定义",
                    "文内对 stellarator 的命名与定位。",
                ),
                quote_between(
                    "目前世界上约有60台托克马克和10台仿星器在运行。",
                    "这两种反应器都有一定的优点。",
                    "全球数量",
                    "文内对运行中装置数量的表述。",
                ),
                quote_between(
                    "托克马克能更好地保持等离子体的高温",
                    "成为未来聚变能源工厂的首选。",
                    "装置对比",
                    "文内对两类装置优缺点的对比总结。",
                ),
            ],
        },
        "# 托卡马克 vs 仿星器\n\n约 60 vs 10 台；保温 vs 稳定性权衡。",
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
        "created_at": "2026-07-15T20:30:00+08:00",
        "updated_at": "2026-07-15T20:30:00+08:00",
        "aliases": [],
        "superseded_by": None,
        "valid_during": None,
        "change_reason": "批量导入等离子体磁约束科普；等待人工核验",
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
        "科普文章；装置数量与 ITER 状态有时效性；聚变温度等为数量级表述。",
        f"导入 {meta['id']}",
        prompt if prompt.is_file() else None,
    )
    print(result.proposal_id, meta["id"])
