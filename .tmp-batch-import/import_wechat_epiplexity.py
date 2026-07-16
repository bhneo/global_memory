from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_494ab02c17c5f495f1ed29d0"
EXT = "extraction_5281bc038cb077d2d54e9da5"
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
        "reason": "由伊芝冰对 arXiv:2601.03220 epiplexity 论文的科普解读归纳；原论文未 capture",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_epiplexity_definition_20260715",
                "title": "该文称 epiplexity（认知复杂度）指在算力约束下观察者能从数据中提取的可复用、可泛化结构信息总量",
                "tags": ["epiplexity", "information-theory", "computational-bounds"],
                "domains": ["information-theory", "machine-learning"],
                "confidence": "medium",
                "applicability": ["有限算力观察者视角的信息论", "2026 From Entropy to Epiplexity 论文科普语境"],
                "uncertainty": "为第三方科普转述；形式化定义细节需回 arXiv:2601.03220 核验。",
                "evidence": [
                    quote_between(
                        "算力约束下，观察者能从数据中提取",
                        "可泛化的结构性信息总量",
                        "核心定义",
                        "文内对 epiplexity 的第三代范式定义。",
                    ),
                    quote_between(
                        "香农熵解决了",
                        "能不能用来解决新问题",
                        "与香农熵关系",
                        "文内对比香农熵与 epiplexity 的分工。",
                    ),
                ],
            },
            "# Epiplexity 定义\n\n有限算力下可学习结构信息；拓展经典信息论边界。",
        ),
        (
            {
                "id": "claim_wechat_epiplexity_pseudorandom_theorem_20260715",
                "title": "该文称伪随机数在有限算力下熵高但 epiplexity 低，可解释随机噪声缺乏学习价值",
                "tags": ["epiplexity", "pseudorandom", "algorithmic-complexity"],
                "domains": ["information-theory", "cryptography"],
                "confidence": "medium",
                "applicability": ["定理 1 科普表述", "区分 PRNG 与真随机"],
                "uncertainty": "定理条件与证明细节在科普中被压缩；依赖原论文与密码学假设。",
                "evidence": [
                    quote_between(
                        "定理 1",
                        "核心痛点",
                        "定理 1",
                        "文内对伪随机数低 epiplexity 的说明。",
                    ),
                    quote_between(
                        "无限算力的神眼里",
                        "认知复杂度低",
                        "有限 vs 无限算力",
                        "文内对比无限算力与有限算力下的信息观。",
                    ),
                ],
            },
            "# 伪随机与 epiplexity\n\n高熵不等于可学习结构。",
        ),
        (
            {
                "id": "claim_wechat_epiplexity_order_matters_20260715",
                "title": "该文称数据顺序可显著影响 epiplexity 与时间有界熵，挑战「顺序无关」经典假设",
                "tags": ["epiplexity", "data-order", "time-bounded-entropy"],
                "domains": ["information-theory", "machine-learning"],
                "confidence": "medium",
                "applicability": ["定理 3 与单向置换 f 的正反向建模讨论", "课程学习/数据排序语境"],
                "uncertainty": "超对数级差距为科普性表述；具体构造需回原文。",
                "evidence": [
                    quote_between(
                        "定理 3",
                        "解锁信息价值的钥匙",
                        "定理 3",
                        "文内对顺序决定信息价值的结论。",
                    ),
                    quote_between(
                        "单向置换",
                        "超对数级",
                        "正反向建模",
                        "文内对 X→f(X) 与 f(X)→X 差距的说明。",
                    ),
                ],
            },
            "# 数据顺序\n\n顺序影响 epiplexity；非无关紧要细节。",
        ),
        (
            {
                "id": "claim_wechat_epiplexity_data_center_ai_20260715",
                "title": "该文称 epiplexity 支持从模型中心转向数据中心主义，并指出文本模态认知复杂度通常高于图像/视频",
                "tags": ["data-centric-ai", "epiplexity", "pretraining"],
                "domains": ["machine-learning", "data-engineering"],
                "confidence": "low",
                "applicability": ["预训练数据筛选与课程学习讨论", "模态间 epiplexity 比较科普"],
                "uncertainty": "文本>图像/视频为科普归纳，未给出统一 benchmark；工程模块为作者框架性主张。",
                "evidence": [
                    quote_between(
                        "数据中心主义",
                        "严谨科学",
                        "工程转向",
                        "文内对 AI 范式从模型到数据的转向。",
                    ),
                    quote_between(
                        "文本模态认知复杂度远超图像",
                        "精准依据",
                        "模态差异",
                        "文内对文本相对图像/视频 epiplexity 的表述。",
                    ),
                ],
            },
            "# 数据中心 AI\n\n数据 epiplexity 决定泛化上限；文本常更高。",
        ),
        (
            {
                "id": "claim_wechat_epiplexity_emergence_ca_20260715",
                "title": "该文称元胞自动机实验中 Class IV 规则 epiplexity 持续增长，可为涌现提供量化标准",
                "tags": ["emergence", "cellular-automata", "complex-systems"],
                "domains": ["complex-systems", "information-theory"],
                "confidence": "low",
                "applicability": ["复杂系统涌现定性转定量讨论", "原论文元胞自动机实验科普"],
                "uncertainty": "Class II/III/IV 分类结果为科普转述；涌现的 epiplexity 定义需回原文严格核验。",
                "evidence": [
                    quote_between(
                        "epiplexity 涌现",
                        "涌现现象",
                        "涌现定义",
                        "文内对 epiplexity 涌现的形式化科普描述。",
                    ),
                    quote_between(
                        "Class IV",
                        "量化标准",
                        "元胞自动机",
                        "文内对 CA 规则类别的 epiplexity 对比。",
                    ),
                ],
            },
            "# 涌现量化\n\nClass IV epiplexity 增长；涌现可计算化。",
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
            "created_at": "2026-07-15T23:50:00+08:00",
            "updated_at": "2026-07-15T23:50:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入 epiplexity 科普；等待人工核验",
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
            "信息论/AI 科普；原论文 arXiv:2601.03220 未 capture，需回原文核验定理与公式。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
