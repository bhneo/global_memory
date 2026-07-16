from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_68161c78067d7b4add05ba1a"
EXT = "extraction_fe8826e067e84de0741c77af"
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
        "reason": "由机器之心对 UCL 汪军 2023 AI 科技年会演讲整理归纳；非原始讲稿 capture",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_wangjun_dl_x_to_y_limit_20260716",
                "title": "该文称当前深度学习本质是 X→Y 映射，缺乏 System 2 式思考，在新环境下适应有限",
                "tags": ["deep-learning", "system1-system2", "generalization"],
                "domains": ["machine-learning", "cognitive-science"],
                "confidence": "low",
                "applicability": ["汪军 2023 演讲对神经网络局限的论述", "自动驾驶复杂决策类比"],
                "uncertainty": "为演讲者观点；与当前大模型推理能力争论需区分时代背景（2023）。",
                "evidence": [
                    quote_between(
                        "X 到 Y 的映射",
                        "没有思考的",
                        "映射局限",
                        "文内对神经网络缺乏思考的表述。",
                    ),
                    quote_between(
                        "System 2",
                        "有效的适应",
                        "System 1/2",
                        "文内对比 System 2 与当前 NN 在新环境适应。",
                    ),
                ],
            },
            "# X→Y 映射局限\n\n拟合非思考；复杂环境需 System 2（演讲观点）。",
        ),
        (
            {
                "id": "claim_wechat_wangjun_no_free_lunch_generalization_20260716",
                "title": "该文引 No free lunch 称神经网络虽具通用近似能力，但并非适合所有任务，泛化至未见环境是关键",
                "tags": ["no-free-lunch", "generalization", "universal-approximation"],
                "domains": ["machine-learning", "learning-theory"],
                "confidence": "medium",
                "applicability": ["通用近似定理与 NFL 对照讨论", "变化环境适应语境"],
                "uncertainty": "为标准 ML 理论科普化表述；与具体架构能力边界需细分。",
                "evidence": [
                    quote_between(
                        "No free lunch",
                        "另一些任务上失败",
                        "NFL 定理",
                        "文内对 No free lunch 的说明。",
                    ),
                    quote_between(
                        "泛化性",
                        "有限制的",
                        "泛化要求",
                        "文内对泛化至新环境的强调。",
                    ),
                ],
            },
            "# NFL 与泛化\n\n普适近似≠所有任务；泛化是智能关键。",
        ),
        (
            {
                "id": "claim_wechat_wangjun_iit_zero_integration_20260716",
                "title": "该文引整合信息理论称传统前馈/Transformer 信息整合度为零，需反馈回路才可能有非零整合",
                "tags": ["integrated-information-theory", "transformer", "recurrent"],
                "domains": ["consciousness-studies", "machine-learning"],
                "confidence": "low",
                "applicability": ["IIT 与 NN 架构讨论", "global workspace / 回路必要性"],
                "uncertainty": "「整合度为零」为演讲转述 IIT 测量结论，争议大且非共识；需回 IIT 原文。",
                "evidence": [
                    quote_between(
                        "Integrated information",
                        "信息整合度是零",
                        "IIT 测量",
                        "文内对 Transformer/前馈网络整合度的判断。",
                    ),
                    quote_between(
                        "反馈回路",
                        "信息就有集成了",
                        "回路必要性",
                        "文内对回路产生信息集成的说明。",
                    ),
                ],
            },
            "# IIT 与架构\n\n前馈/Transformer 整合度为零（演讲引 IIT）；回路或 RNN 不同。",
        ),
        (
            {
                "id": "claim_wechat_wangjun_global_workspace_integration_20260716",
                "title": "该文称 Global neuronal workspace 通过全局工作空间整合各模块信息，是有意识决策的建模方向之一",
                "tags": ["global-workspace-theory", "consciousness", "modularity"],
                "domains": ["cognitive-science", "machine-learning"],
                "confidence": "low",
                "applicability": ["GNW 理论计算机化讨论", "compositional 适应复杂任务"],
                "uncertainty": "为意识理论科普；「产生意识」的数学建模为演讲者解读，非实验确立。",
                "evidence": [
                    quote_between(
                        "Global neuronal workspace",
                        "global workspace",
                        "GNW 框架",
                        "文内对 global workspace 机制的描述。",
                    ),
                    quote_between(
                        "信息整合之后",
                        "主观感受",
                        "整合与意识",
                        "文内将信息整合与主观感受关联。",
                    ),
                ],
            },
            "# Global workspace\n\n全局整合各模块信息；意识建模候选框架。",
        ),
        (
            {
                "id": "claim_wechat_wangjun_machine_consciousness_c0_c5_20260716",
                "title": "该文提出机器意识 C0–C5 阶段划分，称当前 AIGC/Transformer 多处于 C0 拟合表象阶段",
                "tags": ["machine-consciousness", "aigc", "developmental-stages"],
                "domains": ["artificial-intelligence", "philosophy-of-mind"],
                "confidence": "low",
                "applicability": ["汪军机器意识阶段框架", "ChatGPT 拟合人类数据语境"],
                "uncertainty": "C0–C5 为演讲者提出的路线图，非领域标准 taxonomy。",
                "evidence": [
                    quote_between(
                        "沿途下蛋",
                        "C5",
                        "阶段划分",
                        "文内对机器意识分阶段的提出。",
                    ),
                    quote_between(
                        "AIGC",
                        "C0 阶段",
                        "当前阶段",
                        "文内对 AIGC/Transformer 所处阶段的判断。",
                    ),
                ],
            },
            "# C0–C5 阶段\n\n现网 AIGC 多在 C0；机制研究需更高阶段。",
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
            "created_at": "2026-07-16T01:30:00+08:00",
            "updated_at": "2026-07-16T01:30:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入汪军机器意识演讲；等待人工核验",
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
            "2023 演讲整理；IIT/意识主张为理论观点，非共识事实。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
