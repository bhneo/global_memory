from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_647ffb9287507f806c354670"
EXT = "extraction_5ed8cc221c9d9bcce0c53950"
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
        "reason": "由返朴/中科院物理所转载的虫洞科普文章归纳；引用 Morris-Thorne 等经典论文但未 capture 原文",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_traversable_wormhole_exotic_matter_20260715",
                "title": "该文称 Morris-Thorne 可穿越虫洞需要违反类光能量条件的奇异负能物质",
                "tags": ["wormhole", "energy-condition", "general-relativity"],
                "domains": ["physics", "general-relativity"],
                "confidence": "medium",
                "applicability": ["Morris-Thorne 球对称虫洞构造讨论", "Ray-Chaudhuri 方程与测地线汇论证语境"],
                "uncertainty": "为科普性转述经典 GR 结论；负能物质量子来源与可工程化尺度未在文中定量给出。",
                "evidence": [
                    quote_between(
                        "Morris和Thorne",
                        "负能物质[1]",
                        "Morris-Thorne 方法",
                        "文内对反求物质分布与负能需求的说明。",
                    ),
                    quote_between(
                        "类光能量条件",
                        "奇异物质。",
                        "能量条件",
                        "文内对类光能量条件被破坏的结论。",
                    ),
                ],
            },
            "# 可穿越虫洞与负能物质\n\n喉部需奇异负能物质；违反类光能量条件。",
        ),
        (
            {
                "id": "claim_wechat_wormhole_time_machine_20260715",
                "title": "该文概述可通过让虫洞出口相对入口高速运动并再汇合，利用钟慢效应构造简化版时间机器",
                "tags": ["wormhole", "time-machine", "special-relativity"],
                "domains": ["physics", "general-relativity"],
                "confidence": "medium",
                "applicability": ["Morris-Thorne-Yurtsever 时间机器讨论科普版", "忽略细节的简化模型"],
                "uncertainty": "文内自述忽略细节；因果性难题未解决；「自然憎恶时间机器」为引述性表述。",
                "evidence": [
                    quote_between(
                        "连接遥远两点",
                        "最简化的版本",
                        "时间机器构造",
                        "文内对虫洞改造为时间机器的简化步骤。",
                    ),
                    quote_between(
                        "因果性上的难题",
                        "不可能被制成",
                        "因果性限制",
                        "文内对时间机器研究边界的说明。",
                    ),
                ],
            },
            "# 虫洞时间机器\n\n钟慢+汇合可产生时间跃变；因果难题未解。",
        ),
        (
            {
                "id": "claim_wechat_er_epr_entanglement_20260715",
                "title": "该文称 ER=EPR 猜想表明虫洞/爱因斯坦-罗森桥与量子纠缠存在本质联系",
                "tags": ["er-epr", "quantum-entanglement", "holography"],
                "domains": ["physics", "quantum-gravity"],
                "confidence": "medium",
                "applicability": ["AdS/CFT 与 TFD 态对应讨论", "Raamsdonk、Susskind-Maldacena 工作科普"],
                "uncertainty": "ER=EPR 仍为猜想而非实验确立事实；TFD-AdS 虫洞对应为特定理论设定。",
                "evidence": [
                    quote_between(
                        "ER=EPR猜想[5]",
                        "ER=EPR这个名号",
                        "ER=EPR 提出",
                        "文内对 ER=EPR 猜想来源的说明。",
                    ),
                    quote_between(
                        "ER指代",
                        "奇点",
                        "ER 不可穿越",
                        "文内对爱因斯坦-罗森桥性质的限制。",
                    ),
                    quote_between(
                        "深刻的联系",
                        "即是",
                        "纠缠-虫洞关联",
                        "文内对纠缠与虫洞等价的表述。",
                    ),
                ],
            },
            "# ER=EPR\n\n虫洞与量子纠缠深层关联；标准 ER 不可穿越。",
        ),
        (
            {
                "id": "claim_wechat_double_trace_traversable_20260715",
                "title": "该文称边界 double trace deformation 可引入负能量流，使原本不可穿越的 ER 桥变为可穿越",
                "tags": ["traversable-wormhole", "ads-cft", "quantum-teleportation"],
                "domains": ["physics", "quantum-gravity"],
                "confidence": "low",
                "applicability": ["Gao-Jafferis-Wall 可穿越虫洞模型科普", "引力版量子隐形传态图像"],
                "uncertainty": "为特定 holographic 模型结论；double trace 操作与实验可 realizability 未讨论；科普转述。",
                "evidence": [
                    quote_between(
                        "double trace deformation",
                        "算符扰动",
                        "double trace 构造",
                        "文内对实现可穿越性的模型操作。",
                    ),
                    quote_between(
                        "根据ER=EPR",
                        "[7]",
                        "引力量子隐形传态",
                        "文内对可穿越虫洞与量子隐形传态类比。",
                    ),
                ],
            },
            "# double trace 可穿越虫洞\n\n负能量流收缩视界；类比量子隐形传态。",
        ),
        (
            {
                "id": "claim_wechat_replica_wormhole_island_20260715",
                "title": "该文称 replica trick 计算霍金辐射精确熵时需考虑连通「拷贝虫洞」构型，与岛屿公式及幺正性恢复相关",
                "tags": ["replica-wormhole", "black-hole-information", "island-formula"],
                "domains": ["physics", "quantum-gravity"],
                "confidence": "medium",
                "applicability": ["欧式路径积分与 replica trick 熵计算", "2019–2020 岛屿/replica wormhole 研究科普"],
                "uncertainty": "拷贝虫洞物理含义文内称「仍有待澄清」；岛屿公式与全连通构型关系为科普概述。",
                "evidence": [
                    quote_between(
                        "岛屿公式",
                        "岛屿公式。",
                        "岛屿公式",
                        "文内对精确熵计算方法的引入。",
                    ),
                    quote_between(
                        "连通的构型",
                        "违反",
                        "拷贝虫洞与幺正性",
                        "文内对比非连通与连通构型对熵/幺正性的影响。",
                    ),
                    quote_between(
                        "洛伦兹型的",
                        "理解和澄清",
                        "物理含义未定",
                        "文内对欧几里得拷贝虫洞与洛伦兹虫洞差异的限定。",
                    ),
                ],
            },
            "# 拷贝虫洞\n\nreplica 连通构型参与精确熵；关联 Page 曲线/幺正性。",
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
            "created_at": "2026-07-15T21:40:00+08:00",
            "updated_at": "2026-07-15T21:40:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入虫洞科普；等待人工核验",
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
            "理论物理科普；ER=EPR 为猜想；经典论文未 capture，需回原文核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
