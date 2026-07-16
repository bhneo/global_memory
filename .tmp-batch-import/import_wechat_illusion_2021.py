from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_046487376d500224386ff628"
EXT = "extraction_8e6bec146e8c61326ddc9aca"
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
        "reason": "由中科院物理所转载的 2021 最佳视错觉大赛科普文章归纳；非原始实验论文",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_ghost_queen_illusion_20260715",
                "title": "该文称 2021 最佳视错觉大赛第一名「幽灵女王」由 Matt Pritchard 创作，白棋被「隐形斗篷」纸板遮挡却在镜中可见",
                "tags": ["optical-illusion", "best-illusion-contest", "mirror-illusion"],
                "domains": ["psychology", "perception"],
                "confidence": "medium",
                "applicability": ["2021 年度最佳视错觉大赛第一名作品介绍", "棋盘+镜子场景"],
                "uncertainty": "机制描述为科普转述；Matt Pritchard 获奖信息未 capture 官方 contest 页面；图片素材文内称来自网络。",
                "evidence": [
                    quote_between(
                        "幽灵女王这是今年获得第一名的视错觉作品",
                        "作者是来自英国的Matt Pritchard。",
                        "第一名与作者",
                        "文内对作品名次与作者的说明。",
                    ),
                    quote_between(
                        "白色棋子原本就在棋盘上，只不过上面遮盖了一层「隐形斗篷」。",
                        "只不过上面遮盖了一层「隐形斗篷」。",
                        "隐形斗篷机制",
                        "文内对遮挡机制的核心解释。",
                    ),
                    quote_between(
                        "但这并不妨碍镜子映出那颗白棋",
                        "但我们眼前没有：",
                        "镜子可见",
                        "文内对镜中可见、肉眼不可见的对比。",
                    ),
                ],
            },
            "# 幽灵女王\n\n纸板图案与棋盘重合遮挡；镜中仍映出白棋。",
        ),
        (
            {
                "id": "claim_wechat_double_ring_illusion_20260715",
                "title": "该文称双环错觉在边缘重叠时运动知觉会改变，但实际旋转方式未变",
                "tags": ["optical-illusion", "motion-perception"],
                "domains": ["psychology", "perception"],
                "confidence": "medium",
                "applicability": ["Dawei Bai 与 Brent Strickland 作品介绍", "两圆环旋转知觉实验"],
                "uncertainty": "为演示性描述，未给出定量实验参数；「大多数人」为概括性说法。",
                "evidence": [
                    quote_between(
                        "在大多数人眼中，它们似乎在原地转圈",
                        "似乎在原地转圈：",
                        "初始知觉",
                        "文内对默认旋转知觉的描述。",
                    ),
                    quote_between(
                        "然而，只要让它们的边缘发生重叠",
                        "生怕相互触碰到一样。",
                        "重叠后知觉",
                        "文内对重叠后弹跳式知觉变化的描述。",
                    ),
                    quote_between(
                        "但其实圆圈的运转方式并没有改变",
                        "这种错觉也就消失了。",
                        "物理未变",
                        "文内强调实际运动未改变的说明。",
                    ),
                ],
            },
            "# 双环错觉\n\n重叠改变知觉，不改变真实旋转。",
        ),
        (
            {
                "id": "claim_wechat_rubber_hand_slime_variant_20260715",
                "title": "该文称「粘液手错觉」是橡胶手幻觉变种：同步捏扯真手与假手可诱发假手归属感",
                "tags": ["rubber-hand-illusion", "body-ownership", "perception"],
                "domains": ["psychology", "neuroscience"],
                "confidence": "medium",
                "applicability": ["镜子遮挡真手与粘液手的演示设定", "同步触觉刺激条件"],
                "uncertainty": "文内称错觉未必每次成功且不一定影响所有人；非 peer-reviewed 实验报告。",
                "evidence": [
                    quote_between(
                        "一面镜子遮挡住了被试者的真手和粘液手",
                        "两边动作同步进行。",
                        "实验设置",
                        "文内对粘液手错觉装置与同步操作的描述。",
                    ),
                    quote_between(
                        "这是错觉「橡胶手幻觉」的变种尝试",
                        "也会把橡胶手当作自己的真手。",
                        "橡胶手机制",
                        "文内对经典橡胶手幻觉机制的解释。",
                    ),
                    quote_between(
                        "当然，这是错觉未必每次都会成功",
                        "也不一定能影响所有人",
                        "适用边界",
                        "文内对效应稳定性的限定。",
                    ),
                ],
            },
            "# 粘液手 / 橡胶手\n\n同步触觉可诱发假手归属感；效应因人而异。",
        ),
        (
            {
                "id": "claim_wechat_sugihara_mirror_paper_20260715",
                "title": "该文称杉原厚吉的镜面纸片错觉：特定视角下平面纸片可在镜中呈现为「上升」的立体柱体",
                "tags": ["sugihara-illusion", "mirror-illusion", "geometry"],
                "domains": ["perception", "mathematics"],
                "confidence": "medium",
                "applicability": ["2021 年杉原厚吉作品介绍", "镜子+纸片+参照柱体场景"],
                "uncertainty": "为视觉演示机制说明，非数学证明；「被催眠」为修辞。",
                "evidence": [
                    quote_between(
                        "再来感受一下日本数学家杉原厚吉（Kokichi Sugihara）今年的视错觉作品",
                        "依然是熟悉的镜面",
                        "作者与形式",
                        "文内对作者与镜面装置的引入。",
                    ),
                    quote_between(
                        "其实黄色柱体只是一个纸片，并不是柱子",
                        "画面显得极为不合理。",
                        "纸片本质",
                        "文内揭示黄色「柱体」为平面纸片。",
                    ),
                    quote_between(
                        "让你产生错觉的，只不过是一个经过科学设计的纸片罢了",
                        "只不过是一个经过科学设计的纸片罢了。",
                        "设计本质",
                        "文内对错觉来源的总结。",
                    ),
                ],
            },
            "# 杉原厚吉镜面纸片\n\n平面纸片在特定视角+镜子中似立体上升。",
        ),
        (
            {
                "id": "claim_wechat_oh_la_la_box_20260715",
                "title": "该文称「Oh La La 盒子」由两片纸片在特定角度观看可产生立方体错觉",
                "tags": ["optical-illusion", "3d-from-2d"],
                "domains": ["perception"],
                "confidence": "medium",
                "applicability": ["Oh La La 盒子作品描述", "两纸片特定视角观看"],
                "uncertainty": "仅为简短演示说明，未给出精确几何参数或作者信息。",
                "evidence": [
                    quote_between(
                        "乍一看，这是一个立方体。",
                        "但其实它只是两个纸片而已：",
                        "立方体 vs 纸片",
                        "文内对物体真实构成的对比。",
                    ),
                    quote_between(
                        "两个纸壳贴近后，只要找到一个特定的角度",
                        "非常巧妙。",
                        "观看角度",
                        "文内对产生错觉所需视角条件的说明。",
                    ),
                ],
            },
            "# Oh La La 盒子\n\n两纸片特定角度产生立方体错觉。",
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
            "created_at": "2026-07-15T21:25:00+08:00",
            "updated_at": "2026-07-15T21:25:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入视错觉科普；等待人工核验",
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
            "科普文章；获奖与实验细节需回 Best Illusion 官方或原论文核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
