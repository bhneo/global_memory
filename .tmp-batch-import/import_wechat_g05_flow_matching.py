from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_e6608d8f849ad472bbd95143"
EXT = "extraction_4180d1579b26ecbbd8e5b21b"
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
        "reason": "具身纪元 Marilyn Liu 解读 Galaxea G0.5 技术报告 vs PI flow matching；非官方 primary source",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_g05_vla_language_action_tension_20260716",
                "title": "该文称 VLA 需同时处理离散语言 token 与连续实时控制；PI π0 以 VLM 理解 + 独立流匹配动作专家为行业主流之一",
                "tags": ["VLA", "flow-matching", "architecture"],
                "domains": ["robotics", "machine-learning"],
                "confidence": "medium",
                "applicability": ["自回归 vs 流匹配路线之争", "RT-2/OpenVLA/π0-FAST 离散化动作"],
                "uncertainty": "为自媒体架构综述；「定调」等表述含作者判断。",
                "evidence": [
                    quote_between(
                        "语言是离散的",
                        "实时控制",
                        "语言-动作矛盾",
                        "文内对 VLA 双信号冲突的定义。",
                    ),
                    quote_between(
                        "流匹配专家",
                        "管出动作",
                        "PI 双模块",
                        "文内对 π0 架构分工的叙述。",
                    ),
                ],
            },
            "# 架构分歧\n\nG0.5 主张统一权重自回归；质疑 flow matching 为唯一解。",
        ),
        (
            {
                "id": "claim_wechat_g05_flow_encoder_bottleneck_ki_20260716",
                "title": "该文称 VLM-as-Encoder + 流匹配专家可提速，但 VLM 生成/CoT 能力受条件瓶颈限制，且动作梯度可导致 VLM 能力退化；PI 以知识绝缘阻断有害梯度",
                "tags": ["VLM-as-encoder", "catastrophic-forgetting", "knowledge-insulation"],
                "domains": ["robotics", "machine-learning"],
                "confidence": "medium",
                "applicability": ["50Hz 灵巧操作动机", "离散 token 预测 vs 连续回归目标不同构"],
                "uncertainty": "抗遗忘/ KI 机制来自对 PI 论文的二手解读；需回 π0.5 原文核验。",
                "evidence": [
                    quote_between(
                        "VLM-as-Encoder",
                        "动作专家模型",
                        "编码器架构",
                        "文内对 VLM 退居二线、外挂专家的说明。",
                    ),
                    quote_between(
                        "抗遗忘",
                        "知识绝缘",
                        "KI 与遗忘",
                        "文内对梯度回传伤害与 PI KI 对策。",
                    ),
                ],
            },
            "# 流匹配代价\n\n高频控制推动 flow matching；VLA-0 被引证自回归仍可竞争。",
        ),
        (
            {
                "id": "claim_wechat_g05_actioncodec_rvq_skeleton_20260716",
                "title": "该文介绍 G0.5 用 RVQ ActionCodec 与 27 维虚拟骨架（左/右臂、夹爪、底盘）统一跨本体动作 token，并按需只为激活部件生成 token",
                "tags": ["ActionCodec", "RVQ", "cross-embodiment"],
                "domains": ["robotics", "machine-learning"],
                "confidence": "medium",
                "applicability": ["三代动作分词器对比", "TCL 时域对比学习"],
                "uncertainty": "技术细节来自 G0.5 报告二手转述；benchmark 需回 Galaxea 原文。",
                "evidence": [
                    quote_between(
                        "残差向量量化",
                        "ActionCodec",
                        "RVQ 编解码",
                        "文内对 G0.5 分词器核心设计。",
                    ),
                    quote_between(
                        "27 维",
                        "按需生成",
                        "虚拟骨架",
                        "文内对跨本体布局与按需 token 的说明。",
                    ),
                ],
            },
            "# ActionCodec\n\n5 个乐高模块；冻结单一编解码器消费统一布局。",
        ),
        (
            {
                "id": "claim_wechat_g05_native_cot_memory_mixture_20260716",
                "title": "该文称 G0.5 在同一自回归序列中原生生成 subtask/BBox/trace/action hint 四类推理，ViT 每 4 层插时空注意力记 5 秒历史，预训练 VQA:机器人数据=1:4",
                "tags": ["chain-of-thought", "visual-memory", "pretraining-mixture"],
                "domains": ["robotics", "machine-learning"],
                "confidence": "medium",
                "applicability": ["Qwen3.5 2B 基座", "Gemini/SAM3 自动标注流水线"],
                "uncertainty": "数据规模与标注 pipeline 为报告转述；1:4 配比效果需独立验证。",
                "evidence": [
                    quote_between(
                        "Native Chain-of-Thought",
                        "ActionHint",
                        "原生 CoT",
                        "文内对四类推理 token 的列举。",
                    ),
                    quote_between(
                        "1:4",
                        "交叉熵损失",
                        "数据配比",
                        "文内对 VQA 与动作样本混合比例。",
                    ),
                ],
            },
            "# 统一序列\n\n1Hz×6 帧视觉记忆；训练随机丢弃 30% 历史帧防过拟合。",
        ),
        (
            {
                "id": "claim_wechat_g05_reported_benchmarks_20260716",
                "title": "该文报告 G0.5 零样本 DROID Franka 成功率 82.5%，PP Bench 指令跟随 65.6%→84.4%（50h 后训练）；BEHAVIOR-1K 1 epoch 29.0% 超 π0.5 四 epoch 26.3%",
                "tags": ["benchmark", "Galaxea-G0.5", "zero-shot"],
                "domains": ["robotics", "evaluation"],
                "confidence": "low",
                "applicability": ["vs π0.5/GR00T 对比叙述", "prompt 副词微调行为 +15%/+10%"],
                "uncertainty": "全部为自媒体转述 G0.5 报告数字；非独立复现，宜标 contested/low 待回原文。",
                "evidence": [
                    quote_between(
                        "82.5%",
                        "π0.5-DROID",
                        "DROID 零样本",
                        "文内对 DROID Franka 零样本成功率叙述。",
                    ),
                    quote_between(
                        "BEHAVIOR-1K",
                        "26.3%",
                        "长程家务",
                        "文内对 BEHAVIOR-1K epoch 对比数据。",
                    ),
                ],
            },
            "# 报告数字\n\nLIBERO 98.9% 等仿真数文内亦有；本文仅引 DROID 与 BEHAVIOR 作代表。",
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
            "created_at": "2026-07-16T11:08:00+08:00",
            "updated_at": "2026-07-16T11:08:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入 G0.5 vs PI flow matching 解读；等待人工核验",
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
            "自媒体解读 Galaxea G0.5；benchmark 数字 confidence 低，需回技术报告核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
