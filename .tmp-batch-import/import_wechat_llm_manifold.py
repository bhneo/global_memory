from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_f35b44d4bd383fb26ca49165"
EXT = "extraction_5175d74685def36cf73e75c3"
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
        "reason": "由智能情报所转载 Lukas Nel 2025-07 观点文归纳；vec2vec/柏拉图表征等原论文未 capture",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_vec2vec_embedding_translation_20260716",
                "title": "该文称 vec2vec 可在无配对训练数据下跨架构翻译嵌入，报告约 0.92 余弦相似度与 >99% 打乱嵌入匹配",
                "tags": ["vec2vec", "representation-alignment", "embeddings"],
                "domains": ["machine-learning", "nlp"],
                "confidence": "low",
                "applicability": ["跨模型嵌入对齐/翻译讨论", "GTR(T5) 与 GTE(BERT) 等非配对样本语境"],
                "uncertainty": "数值来自二手科普转述；vec2vec 原论文与实验设置未 capture，需回 [2] 核验。",
                "evidence": [
                    quote_between(
                        "vec2vec",
                        "0.92",
                        "vec2vec 结果",
                        "文内对跨架构翻译相似度的表述。",
                    ),
                    quote_between(
                        "99%",
                        "潜在的几何结构",
                        "语义保留翻译",
                        "文内对匹配率与共享几何结构的推论。",
                    ),
                ],
            },
            "# vec2vec\n\n无配对跨模型嵌入对齐；科普性数值需回原文。",
        ),
        (
            {
                "id": "claim_wechat_platonic_representation_convergence_20260716",
                "title": "该文主张不同 LLM 随规模/能力增强内部表征趋同，并援引柏拉图式表征假说或「智能流形」解释",
                "tags": ["platonic-representation", "llm-convergence", "manifold"],
                "domains": ["machine-learning", "philosophy-of-mind"],
                "confidence": "low",
                "applicability": ["表征趋同/通用语义空间讨论", "Platonic Representation Hypothesis 科普语境"],
                "uncertainty": "为观点性长文而非系统综述；「独立存在的数学结构」属哲学推断，原假说论文 [1] 未 capture。",
                "evidence": [
                    quote_between(
                        "内部的表征正变得惊人地一致",
                        "思想通用语",
                        "表征趋同",
                        "文内对 LLM 表征趋同的观察性表述。",
                    ),
                    quote_between(
                        "柏拉图式表征假说",
                        "碳基的生命大脑",
                        "柏拉图/流形",
                        "文内对假说与智能流形说法的命名。",
                    ),
                ],
            },
            "# 表征趋同\n\n不同 LLM 表征趋同；柏拉图式/流形解释待核验。",
        ),
        (
            {
                "id": "claim_wechat_cross_modal_representation_alignment_20260716",
                "title": "该文称文本模型与视觉模型随能力增强也呈现更强表征一致性，并以颜色表征与人类感知一致为例",
                "tags": ["multimodal", "cross-modal-alignment", "color-representation"],
                "domains": ["machine-learning", "cognitive-science"],
                "confidence": "low",
                "applicability": ["跨模态表征对齐讨论", "颜色共现文本模型 vs 视觉模型比较语境"],
                "uncertainty": "跨模态趋同为科普归纳；颜色例子引用 [5] 未 capture，因果与定量关系未给出。",
                "evidence": [
                    quote_between(
                        "文本上训练的模型和在图像上训练的模型",
                        "越来越强",
                        "跨模态趋同",
                        "文内对文本/视觉模型一致性增强的表述。",
                    ),
                    quote_between(
                        "颜色共现关系",
                        "高度一致",
                        "颜色例子",
                        "文内对文本/视觉/人类颜色表征一致性的例子。",
                    ),
                ],
            },
            "# 跨模态对齐\n\n文本与视觉表征趋同；颜色例为二手引述。",
        ),
        (
            {
                "id": "claim_wechat_multilingual_shared_concept_space_20260716",
                "title": "该文引述 Anthropic 研究称多语言输入激活相同核心概念模式，而非独立「语言大脑」",
                "tags": ["multilingual", "concept-representation", "anthropic"],
                "domains": ["machine-learning", "nlp"],
                "confidence": "low",
                "applicability": ["多语言 LLM 内部概念空间讨论", "Anthropic 多语言机制科普引述"],
                "uncertainty": "Anthropic 研究 [9] 未 capture；「相同核心模式」为转述，实验细节与边界未给出。",
                "evidence": [
                    quote_between(
                        "Anthropic",
                        "独立的法语大脑",
                        "Anthropic 多语言",
                        "文内对 Anthropic 多语言研究的引述开头。",
                    ),
                    quote_between(
                        "相同的核心模式",
                        "先于我们用以表达的词汇",
                        "共享概念空间",
                        "文内对跨语言共享模式与意义先于词汇的表述。",
                    ),
                ],
            },
            "# 多语言概念空间\n\n跨语言共享核心模式；Anthropic 原文待 capture。",
        ),
        (
            {
                "id": "claim_wechat_model_merge_linear_connectivity_20260716",
                "title": "该文将模型合并/参数算术与线性模式连接作为不同训练模型共享潜在流形的证据",
                "tags": ["model-merging", "mode-connectivity", "weight-space"],
                "domains": ["machine-learning", "optimization"],
                "confidence": "low",
                "applicability": ["模型合并与权重插值讨论", "线性模式连接作为共享结构证据的科普语境"],
                "uncertainty": "从合并成功推断共享流形为哲学性跳跃；[8] 未 capture，与参数对称性等因素未区分。",
                "evidence": [
                    quote_between(
                        "两个模型相加",
                        "两种任务",
                        "模型合并",
                        "文内对参数级模型合并可行性的表述。",
                    ),
                    quote_between(
                        "线性模式连接",
                        "潜在智能图景",
                        "模式连接",
                        "文内将线性模式连接作为共享结构证据。",
                    ),
                ],
            },
            "# 模型合并与模式连接\n\n合并/连接被解释为共享流形；推断性强。",
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
            "created_at": "2026-07-16T00:26:00+08:00",
            "updated_at": "2026-07-16T00:26:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入 LLM 表征趋同观点文；等待人工核验",
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
            "观点性科普；多处哲学推断；vec2vec/Anthropic/PRH 原文未 capture，需回引文核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
