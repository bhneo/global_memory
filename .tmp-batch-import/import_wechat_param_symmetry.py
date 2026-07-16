from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_6ae6c4bef52010f96ddb3dbf"
EXT = "extraction_4806a53e6b1eaf92d41816d5"
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
        "reason": "由机器之心对 arXiv:2506.13018 参数空间对称性综述的科普转述归纳；原论文未 capture",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_param_symmetry_definition_20260716",
                "title": "该文称参数空间对称性是保持损失函数不变的参数变换，并在参数空间中形成等价轨道",
                "tags": ["parameter-symmetry", "loss-landscape", "group-theory"],
                "domains": ["deep-learning", "optimization"],
                "confidence": "medium",
                "applicability": ["置换对称等函数等价参数配置讨论", "2506.13018 综述科普语境"],
                "uncertainty": "为机器之心科普转述；形式化群论表述需回 arXiv:2506.13018 核验。",
                "evidence": [
                    quote_between(
                        "parameter space symmetry",
                        "等价轨道",
                        "对称性定义",
                        "文内对参数空间对称性与轨道的说明。",
                    ),
                    quote_between(
                        "L (g",
                        "L (θ)",
                        "损失不变性",
                        "文内对对称变换保持损失的形式化表述。",
                    ),
                ],
            },
            "# 参数空间对称性\n\n保持 L(g·θ)=L(θ)；等价轨道表示同一函数。",
        ),
        (
            {
                "id": "claim_wechat_param_symmetry_architectures_20260716",
                "title": "该文称 ReLU/BatchNorm、线性层/注意力、Softmax 等常见架构具有连续对称性，Transformer 对称性为组件组合",
                "tags": ["relu", "transformer", "continuous-symmetry"],
                "domains": ["deep-learning", "architecture"],
                "confidence": "medium",
                "applicability": ["常见 NN 架构对称性分类", "多头注意力对称组合讨论"],
                "uncertainty": "架构列举为综述性概括；各对称群精确形式需回原文。",
                "evidence": [
                    quote_between(
                        "ReLU 网络",
                        "平移对称",
                        "连续对称类型",
                        "文内对 ReLU/归一化/线性/Softmax 对称的列举。",
                    ),
                    quote_between(
                        "Transformer",
                        "线性对称性",
                        "Transformer 对称",
                        "文内对 Transformer 组件对称组合的描述。",
                    ),
                ],
            },
            "# 架构对称性\n\n缩放/GL/平移等连续对称；Transformer 为组合。",
        ),
        (
            {
                "id": "claim_wechat_param_symmetry_flat_minima_20260716",
                "title": "该文称连续对称性将孤立极小值拉伸为平坦极小值流形，平坦方向未必反映更好泛化",
                "tags": ["flat-minima", "generalization", "symmetry"],
                "domains": ["deep-learning", "optimization"],
                "confidence": "medium",
                "applicability": ["用平坦度解释泛化的谨慎解读", "对称性塑造损失地形讨论"],
                "uncertainty": "因果表述为科普归纳；与泛化关系的定量结论需回综述原文。",
                "evidence": [
                    quote_between(
                        "连续对称性",
                        "平坦的极小值流形",
                        "平坦流形",
                        "文内对连续对称性产生平坦极小值流形的说明。",
                    ),
                    quote_between(
                        "平坦方向并非来自更好的泛化",
                        "谨慎解读",
                        "平坦度解读",
                        "文内对平坦度作为泛化指标的限定。",
                    ),
                ],
            },
            "# 平坦极小值\n\n对称性产生平坦方向；不等于泛化优势。",
        ),
        (
            {
                "id": "claim_wechat_param_symmetry_mode_connectivity_20260716",
                "title": "该文称模式连通性与模型融合部分源于对称性，离散置换对称使极小值副本数随宽度阶乘增长",
                "tags": ["mode-connectivity", "permutation-symmetry", "model-fusion"],
                "domains": ["deep-learning", "optimization"],
                "confidence": "medium",
                "applicability": ["独立训练模型低损耗路径连接讨论", "宽度与极小值数量关系科普"],
                "uncertainty": "「部分源于」为综述性解释；阶乘增长为定性表述。",
                "evidence": [
                    quote_between(
                        "模式连通性",
                        "模型融合",
                        "模式连通性",
                        "文内将模式连通性与对称性、模型融合关联。",
                    ),
                    quote_between(
                        "离散对称性",
                        "阶乘级增长",
                        "置换副本",
                        "文内对离散对称复制极小值的说明。",
                    ),
                ],
            },
            "# 模式连通性\n\n对称性提供连接路径；置换使极小值副本爆炸。",
        ),
        (
            {
                "id": "claim_wechat_param_symmetry_conserved_quantities_20260716",
                "title": "该文称连续对称性在梯度流中对应守恒量，影响隐式偏置与收敛/泛化统计",
                "tags": ["conserved-quantities", "implicit-bias", "gradient-flow"],
                "domains": ["deep-learning", "optimization"],
                "confidence": "medium",
                "applicability": ["诺特定理类比下的训练动力学讨论", "初始化与守恒量关系"],
                "uncertainty": "守恒量例子（Gram 矩阵差等）为科普列举；严格定理条件需回原文。",
                "evidence": [
                    quote_between(
                        "守恒量",
                        "诺特定理",
                        "对称与守恒",
                        "文内将对称性与守恒量的物理类比。",
                    ),
                    quote_between(
                        "隐式偏置",
                        "统计分布",
                        "隐式偏置",
                        "文内对守恒量影响收敛与泛化分布的说明。",
                    ),
                ],
            },
            "# 守恒量与隐式偏置\n\n对称结构约束梯度流轨迹与结果分布。",
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
            "created_at": "2026-07-16T00:06:00+08:00",
            "updated_at": "2026-07-16T00:06:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入参数空间对称性科普；等待人工核验",
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
            "DL 理论科普；原综述 arXiv:2506.13018 未 capture，需回原文核验定理与实验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
