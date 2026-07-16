from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_aff280ea206f7233b98afc6a"
EXT = "extraction_c75ef107de8e6b99a4239708"
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
        "reason": "由科学世界/中科院物理所转载的哥德尔不完全性定理科普归纳；非原始论文 capture",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_godel_first_incompleteness_20260716",
                "title": "该文称哥德尔第一不完全性定理表明：在《数学原理》体系中存在既不可证也不可否的佩亚诺算术命题",
                "tags": ["godel", "incompleteness", "peano-arithmetic"],
                "domains": ["mathematics", "logic"],
                "confidence": "medium",
                "applicability": ["Principia Mathematica / PA 语境下的不可判定命题", "科普性第一定理表述"],
                "uncertainty": "为科普转述；「《数学原理》体系」与标准 PA 形式化细节需回 Gödel 1931 原文核验。",
                "evidence": [
                    quote_between(
                        "第一不完全性定理",
                        "佩亚诺算术",
                        "第一定理",
                        "文内对第一不完全性定理与 PA 命题的说明。",
                    ),
                    quote_between(
                        "无法通过证明来判断命题真伪",
                        "第一不完全性定理",
                        "不完全性含义",
                        "文内对「不完全性」含义的解释。",
                    ),
                ],
            },
            "# 第一不完全性定理\n\n存在不可判定命题；非「所有问题都可证伪」。",
        ),
        (
            {
                "id": "claim_wechat_godel_second_incompleteness_20260716",
                "title": "该文称第二不完全性定理表明体系无法在内部证明自身无矛盾，从而挫败希尔伯特计划的相容性目标",
                "tags": ["godel", "consistency", "hilbert-program"],
                "domains": ["mathematics", "logic"],
                "confidence": "medium",
                "applicability": ["希尔伯特计划相容性目标讨论", "第二不完全性定理科普"],
                "uncertainty": "科普压缩了形式系统条件；严格定理需指定足够强的递归公理化系统。",
                "evidence": [
                    quote_between(
                        "第二不完全性定理",
                        "不存在矛盾",
                        "第二定理",
                        "文内对第二定理与体系无矛盾不可证的表述。",
                    ),
                    quote_between(
                        "希尔伯特计划",
                        "相容性",
                        "希尔伯特计划",
                        "文内将第二定理与希尔伯特计划失败关联。",
                    ),
                ],
            },
            "# 第二不完全性定理\n\n系统内无法证明自身一致性。",
        ),
        (
            {
                "id": "claim_wechat_godel_numbering_method_20260716",
                "title": "该文称哥德尔通过哥德尔数将命题与证明符号化，并配合对角线方法构造自指不可证命题",
                "tags": ["godel-numbering", "diagonal-method", "proof-technique"],
                "domains": ["mathematics", "logic"],
                "confidence": "medium",
                "applicability": ["哥德尔证明技术科普", "对角线方法简介"],
                "uncertainty": "证明细节在科普中被大幅压缩；与康托尔对角线仅为类比介绍。",
                "evidence": [
                    quote_between(
                        "哥德尔数",
                        "符号化",
                        "哥德尔数",
                        "文内对哥德尔数编码方法的说明。",
                    ),
                    quote_between(
                        "对角线方法",
                        "无法证明",
                        "对角线构造",
                        "文内对构造「此命题无法证明」的表述。",
                    ),
                ],
            },
            "# 哥德尔数与对角线\n\n编码 + 对角线 → 自指不可证命题。",
        ),
        (
            {
                "id": "claim_wechat_self_reference_paradox_20260716",
                "title": "该文以「这句话是错误的」等自涉悖论说明存在无法判真伪的命题，并类比哥德尔证明思路",
                "tags": ["self-reference", "paradox", "logic"],
                "domains": ["logic", "philosophy"],
                "confidence": "medium",
                "applicability": ["自涉悖论入门", "不完全性定理直观类比"],
                "uncertainty": "悖论例子与形式系统不可判定命题仅为类比；严格逻辑层级不同。",
                "evidence": [
                    quote_between(
                        "这句话是错误的",
                        "二律背反",
                        "说谎者悖论",
                        "文内对自涉悖论与二律背反的说明。",
                    ),
                    quote_between(
                        "自涉悖论",
                        "第一不完全性定理",
                        "类比",
                        "文内将自涉讨论与第一定理证明方法关联。",
                    ),
                ],
            },
            "# 自涉悖论\n\n直观类比；非严格等同形式不可判定性。",
        ),
        (
            {
                "id": "claim_wechat_hilbert_program_limits_20260716",
                "title": "该文称不完全性定理使希尔伯特计划的相容性与完全性目标均无法实现",
                "tags": ["hilbert-program", "completeness", "consistency"],
                "domains": ["mathematics", "logic"],
                "confidence": "medium",
                "applicability": ["20 世纪数学基础计划科普", "完全性 vs 不完全性对照"],
                "uncertainty": "「完全性目标」在科普中与第一定理关系被简化；希尔伯特原目标需回历史文献。",
                "evidence": [
                    quote_between(
                        "数学完全性",
                        "不可能的事",
                        "完全性失败",
                        "文内对完全性目标不可达的表述。",
                    ),
                    quote_between(
                        "希尔伯特计划",
                        "以失败而告终",
                        "计划失败",
                        "文内总结不完全性定理对希尔伯特计划的影响。",
                    ),
                ],
            },
            "# 希尔伯特计划\n\n相容性与（科普所称）完全性目标均受挫。",
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
            "created_at": "2026-07-16T00:48:00+08:00",
            "updated_at": "2026-07-16T00:48:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入哥德尔不完全性定理科普；等待人工核验",
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
            "数理逻辑科普；定理条件在文中被简化，需回 Gödel 1931 与标准教科书核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
