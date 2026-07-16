from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_11bc6c51fa038191e33bc9a7"
EXT = "extraction_abc5ebaba4c64d5f80e1daa8"
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
        "reason": "机器人前瞻报道阿里 Qwen-Robot 系列发布（2026-06-16）；属 vendor/媒体软文",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_qwen_robot_three_model_suite_20260716",
                "title": "该文称阿里发布 Qwen-Robot 系列三模型：RobotNav（VLN 移动）、RobotManip（VLA 操作）、RobotWorld（世界模型），均以语言优先接口连接 VLM 与物理行动",
                "tags": ["Qwen-Robot", "embodied-ai", "VLA"],
                "domains": ["robotics", "machine-learning"],
                "confidence": "low",
                "applicability": ["千问具身智能首套完整系列", "Qwen-RobotClaw 组合调用框架"],
                "uncertainty": "产品发布通稿；技术细节待官方博客/论文核验。",
                "evidence": [
                    quote_between(
                        "Qwen-RobotNav",
                        "自动驾驶四类任务",
                        "RobotNav 定位",
                        "文内对 VLN 移动模型任务范围说明。",
                    ),
                    quote_between(
                        "Qwen-RobotWorld",
                        "物理规律的未来",
                        "RobotWorld 定位",
                        "文内对世界模型跨场景动力学预测的说明。",
                    ),
                ],
            },
            "# 三模型套件\n\n通用 Qwen 可将三者作为物理世界工具组合。",
        ),
        (
            {
                "id": "claim_wechat_qwen_robotnav_go2_deployment_20260716",
                "title": "该文称 Qwen-RobotNav 在宇树 Go2 上单相机零样本部署（Jetson Thor 推理 196ms），训练含 1560 万条样本；NAVSIM 闭环 PDMS 91.4",
                "tags": ["VLN", "Unitree-Go2", "zero-shot"],
                "domains": ["robotics", "navigation"],
                "confidence": "low",
                "applicability": ["参数化视觉分配策略", "EXPRESS-Bench +15.4% 叙述"],
                "uncertainty": "SOTA/PDMS 数字为媒体转述；未见独立第三方复现。",
                "evidence": [
                    quote_between(
                        "196ms",
                        "单个低分辨率相机",
                        "Go2 部署",
                        "文内对 Go2 零样本部署硬件与传感器配置。",
                    ),
                    quote_between(
                        "1560万",
                        "五类导航任务",
                        "训练规模",
                        "文内对 RobotNav 训练样本量与统一任务说明。",
                    ),
                ],
            },
            "# RobotNav\n\n可控观测协议四控制轴；腿式导航与自动驾驶共享权重叙述。",
        ),
        (
            {
                "id": "claim_wechat_qwen_robotmanip_unified_80d_20260716",
                "title": "该文称 Qwen-RobotManip 以 Qwen3.5-4B VL + 流匹配 DiT 动作头，用 80 维统一状态-动作与相机系 EEF 增量位姿，在 >38100 小时开源数据上跨本体训练",
                "tags": ["Qwen-RobotManip", "cross-embodiment", "flow-matching"],
                "domains": ["robotics", "VLA"],
                "confidence": "low",
                "applicability": ["人类视频→机器人数据合成 24808h", "RoboChallenge Table30 45% SR 叙述"],
                "uncertainty": "benchmark 对比 π0.5 等为厂商通稿；需回官方技术报告。",
                "evidence": [
                    quote_between(
                        "80维",
                        "增量位姿",
                        "统一表示",
                        "文内对跨本体 80 维状态-动作与 EEF 增量的说明。",
                    ),
                    quote_between(
                        "38100小时",
                        "大规模多机型",
                        "训练数据量",
                        "文内对 RobotManip 总训练时长叙述。",
                    ),
                ],
            },
            "# RobotManip\n\n对齐是规模化前提：UnifiedSpace+UnifiedEEF 才现对数线性 scaling 叙述。",
        ),
        (
            {
                "id": "claim_wechat_qwen_robotworld_language_action_20260716",
                "title": "该文称 Qwen-RobotWorld 以自然语言统一 20+ 本体与 500+ 动作类别，在 860 万视频-文本对（>2 亿帧）上训练，采用 60 层双流 MMDiT + Qwen2.5-VL 动作编码器",
                "tags": ["world-model", "MMDiT", "synthetic-data"],
                "domains": ["robotics", "generative-models"],
                "confidence": "low",
                "applicability": ["操作/驾驶/导航联合强化", "EWMBench/DreamGen 第一叙述"],
                "uncertainty": "榜单第一等为发布稿自称；物理规律遵循 claim 未附独立评测细节。",
                "evidence": [
                    quote_between(
                        "860万",
                        "2亿帧",
                        "语料规模",
                        "文内对具身世界知识语料库规模。",
                    ),
                    quote_between(
                        "自然语言动作",
                        "500余个动作类别",
                        "语言动作接口",
                        "文内对统一自然语言动作接口的说明。",
                    ),
                ],
            },
            "# RobotWorld\n\n给定观测+语言动作预测下一观测；可作合成数据引擎。",
        ),
        (
            {
                "id": "claim_wechat_qwen_chat2robot_platform_20260716",
                "title": "该文称阿里开放 Chat2Robot 浏览器评测平台（当前仅 RobotManip、RoboTwin-Clean 50 任务训练），并提及 Qwen-RobotClaw 长程任务与开放世界卫生间搜索 demo",
                "tags": ["Chat2Robot", "evaluation-platform", "agent-framework"],
                "domains": ["robotics", "systems"],
                "confidence": "low",
                "applicability": ["qwen-robotmanip.d-robotics.cc 体验地址", "长程重规划 demo"],
                "uncertainty": "平台能力范围与 demo 为宣传描述；开放世界能力「后续发布细节」。",
                "evidence": [
                    quote_between(
                        "Chat2Robot",
                        "50个任务",
                        "评测平台限制",
                        "文内对 Chat2Robot 当前支持范围。",
                    ),
                    quote_between(
                        "Qwen-RobotClaw",
                        "上下文与记忆",
                        "Claw 框架",
                        "文内对 RobotClaw 组合物理工具与长程记忆说明。",
                    ),
                ],
            },
            "# 平台与 demo\n\n三模型独立可用；语言接口便于 Qwen 组合调度。",
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
            "created_at": "2026-07-16T11:20:00+08:00",
            "updated_at": "2026-07-16T11:20:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入 Qwen-Robot 发布稿；等待人工核验",
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
            "机器人前瞻 vendor 通稿；SOTA/benchmark 数字 confidence 低，需回阿里官方材料核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
