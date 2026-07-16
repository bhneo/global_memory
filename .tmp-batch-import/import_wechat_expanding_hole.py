from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_38756ea977001ddb8594f144"
EXT = "extraction_185ffd5cd427923efa0d9edb"
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
        "reason": "由环球科学/中科院物理所转载的 expanding hole 研究科普；原论文 Frontiers 2022 未 capture",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_expanding_hole_perceived_darkness_20260716",
                "title": "该文称「扩大的黑洞」为静态图错觉，大脑将中央暗区解读为正在进入黑暗环境而非像素变化",
                "tags": ["expanding-hole", "visual-illusion", "perception"],
                "domains": ["neuroscience", "psychology"],
                "confidence": "medium",
                "applicability": ["Bruno Laeng 等 expanding hole 错觉讨论", "静态图动态感错觉"],
                "uncertainty": "为科普转述；Laeng 原论文细节需回 Frontiers 2022 核验。",
                "evidence": [
                    quote_between(
                        "静态图",
                        "没有改变过颜色",
                        "静态错觉",
                        "文内强调图像像素未变。",
                    ),
                    quote_between(
                        "Bruno Laeng",
                        "黑暗的环境",
                        "大脑解读",
                        "文内对 Laeng 团队机制解释的核心表述。",
                    ),
                ],
            },
            "# 静态 expanding hole\n\n错觉来自大脑对暗区运动/环境的预测。",
        ),
        (
            {
                "id": "claim_wechat_expanding_hole_pupil_dilation_20260716",
                "title": "该文报告 50 名被试凝视「黑洞」图时瞳孔随时间扩大（约 4.1mm→4.9mm），86% 主观感到扩张",
                "tags": ["pupil-response", "psychophysics", "expanding-hole"],
                "domains": ["neuroscience", "psychology"],
                "confidence": "medium",
                "applicability": ["n=50 眼动实验科普叙述", "0.5s vs 8s 瞳孔直径对比"],
                "uncertainty": "数值来自科普转述；43/50 比例与 mm 数据需回原文核验。",
                "evidence": [
                    quote_between(
                        "50位",
                        "43人",
                        "样本与主观报告",
                        "文内对被试数量与主观扩张报告比例。",
                    ),
                    quote_between(
                        "4.1毫米",
                        "4.9毫米",
                        "瞳孔直径",
                        "文内对 0.5s 与 8s 瞳孔直径的叙述。",
                    ),
                ],
            },
            "# 瞳孔扩大\n\n凝视黑洞图瞳孔随时间增大；多数被试主观感到扩张。",
        ),
        (
            {
                "id": "claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716",
                "title": "该文称瞳孔调节可能依据大脑对光的感知而非实际照度，主观扩张感与瞳孔幅度正相关",
                "tags": ["pupil", "perceived-luminance", "illusion"],
                "domains": ["neuroscience", "psychology"],
                "confidence": "medium",
                "applicability": ["感知驱动瞳孔 vs 物理光照不变语境", "洋红背景扩张更明显"],
                "uncertainty": "「推测」性表述；因果机制在科普中被简化。",
                "evidence": [
                    quote_between(
                        "并不是根据实际的光照多少",
                        "感知",
                        "感知驱动",
                        "文内对瞳孔调节依据的推测。",
                    ),
                    quote_between(
                        "主观感受",
                        "幅度也越大",
                        "主观-瞳孔相关",
                        "文内对主观扩张与瞳孔扩张相关的说明。",
                    ),
                ],
            },
            "# 感知 vs 照度\n\n瞳孔可能随感知暗化而扩大，非仅物理光强。",
        ),
        (
            {
                "id": "claim_wechat_expanding_hole_white_hole_constriction_20260716",
                "title": "该文称反色「白洞」图使被试瞳孔由扩大转为缩小，大脑或解读为走向明亮环境",
                "tags": ["expanding-hole", "pupil", "aftereffect"],
                "domains": ["neuroscience", "psychology"],
                "confidence": "medium",
                "applicability": ["黑底白洞反色条件讨论", "明暗方向性瞳孔响应"],
                "uncertainty": "反色实验细节在科普中被压缩；效应量未给出。",
                "evidence": [
                    quote_between(
                        "反色处理",
                        "白洞",
                        "反色刺激",
                        "文内对反色图条件的说明。",
                    ),
                    quote_between(
                        "不再是逐渐放大",
                        "缩小",
                        "瞳孔缩小",
                        "文内对白洞条件下瞳孔缩小的叙述。",
                    ),
                ],
            },
            "# 白洞反色\n\n白洞条件瞳孔缩小；与黑洞条件对照。",
        ),
        (
            {
                "id": "claim_wechat_expanding_hole_optic_flow_20260716",
                "title": "该文以光流与隧道/洞穴类比解释错觉：大脑预测环境将变暗并提前扩大瞳孔作为补偿",
                "tags": ["optic-flow", "predictive-processing", "evolution"],
                "domains": ["psychology", "neuroscience"],
                "confidence": "medium",
                "applicability": ["Gibson 光流概念科普", "隧道进入类比"],
                "uncertainty": "光流解释为主观理论框架；Laeng 教授引述需回原文。",
                "evidence": [
                    quote_between(
                        "光流",
                        "optic flow",
                        "光流概念",
                        "文内对光流定义与引入。",
                    ),
                    quote_between(
                        "走进一条隧道",
                        "补偿机制",
                        "隧道类比",
                        "文内对预测变暗与瞳孔补偿的解释。",
                    ),
                ],
            },
            "# 光流预测\n\n静态渐变阴影触发进入隧道式预测；演化适应解释。",
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
            "created_at": "2026-07-16T01:41:00+08:00",
            "updated_at": "2026-07-16T01:41:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入 expanding hole 视错觉科普；等待人工核验",
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
            "知觉科普；n=50 与瞳孔 mm 数据需回 Frontiers 2022 原文核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
