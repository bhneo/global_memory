from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_8b41a014bee47c4239a2fa81"
EXT = "extraction_27a3915bf1f44e95bc06bbae"
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
        "reason": "human five 转载 Chelsea Finn & Perry Dong 研讨会：离线迭代 RL 与 EXPO-FT 在线 VLA 微调；原论文未 capture",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_expo_ft_reliability_motivation_20260716",
                "title": "该文称仅靠模仿学习难以达到机器人长期自主所需的高可靠性，需让系统针对目标场景自主迭代优化策略",
                "tags": ["robotics", "imitation-learning", "reliability"],
                "domains": ["robotics", "reinforcement-learning"],
                "confidence": "medium",
                "applicability": ["Finn/PI 研讨会动机", "99.9%+ 可靠性目标表述"],
                "uncertainty": "为研讨会转述与观点性论述；可靠性阈值未给出严格实验定义。",
                "evidence": [
                    quote_between(
                        "仅依靠模仿学习",
                        "高可靠性的机器人策略",
                        "IL 不足",
                        "文内对模仿学习局限的核心判断。",
                    ),
                    quote_between(
                        "99.9%",
                        "自主优化策略",
                        "可靠性目标",
                        "文内对落地可靠性标准与自主迭代的表述。",
                    ),
                ],
            },
            "# 可靠性动机\n\n人工迭代数据集遇瓶颈；模型自主迭代可定位数据缺口。",
        ),
        (
            {
                "id": "claim_wechat_offline_rl_advantage_bc_20260716",
                "title": "该文介绍离线框架：MC 回归估计任务剩余时长作进度代理，二值化优势条件 BC 迭代微调 VLA；意式咖啡成功率 40%→90%+、连续运行 13 小时",
                "tags": ["offline-rl", "VLA", "advantage-conditioning"],
                "domains": ["robotics", "reinforcement-learning"],
                "confidence": "medium",
                "applicability": ["长时序 espresso/叠衣/纸箱任务", "DAgger 式人工修正"],
                "uncertainty": "数值来自研讨会转述；离线框架名称文中留空；需回原文/视频核验。",
                "evidence": [
                    quote_between(
                        "蒙特卡洛",
                        "progress proxy",
                        "价值函数设计",
                        "文内对 MC 价值函数与进度代理的说明。",
                    ),
                    quote_between(
                        "40%",
                        "90%以上",
                        "咖啡成功率",
                        "文内对核心咖啡任务量化结果。",
                    ),
                ],
            },
            "# 离线迭代 RL\n\n优势条件 BC 仅离线；13h 回放与平均 2× 吞吐量提升。",
        ),
        (
            {
                "id": "claim_wechat_expo_dual_policy_20260716",
                "title": "该文称 EXPO 对扩散/流匹配 VLA 采用双策略：预训练流策略仅用监督损失，轻量高斯修正策略优化 Q，避免长降噪链价值梯度反传",
                "tags": ["EXPO", "diffusion-policy", "off-policy-rl"],
                "domains": ["reinforcement-learning", "robotics"],
                "confidence": "medium",
                "applicability": ["扩散策略在线 RL 不稳定问题", "OTF 候选池 Q 选优"],
                "uncertainty": "公式与消融结论为综述级；12 项基准细节需回 EXPO 论文。",
                "evidence": [
                    quote_between(
                        "双策略解耦",
                        "不参与TD价值梯度",
                        "双策略设计",
                        "文内对 VLA 主干隔离 Q 梯度的核心思路。",
                    ),
                    quote_between(
                        "实时采样",
                        "策略坍缩",
                        "OTF 选优",
                        "文内对候选池选优与防坍缩的说明。",
                    ),
                ],
            },
            "# EXPO 双策略\n\n基础 VLA + 修正量；贝尔曼回溯复用选优机制。",
        ),
        (
            {
                "id": "claim_wechat_expo_ft_data_efficiency_20260716",
                "title": "该文称 EXPO-FT 在线微调预训练 VLA：支持 action chunk 与人在环局部干预，8 项真实任务平均仅需 19.1 分钟在线交互收敛，较 SFT 平均成功率 +44%",
                "tags": ["EXPO-FT", "VLA", "human-in-the-loop"],
                "domains": ["robotics", "reinforcement-learning"],
                "confidence": "medium",
                "applicability": ["稀疏二值奖励", "Actor-Learner 分布式", "冻结 VLA 视觉编码器"],
                "uncertainty": "19.1 分钟不含重置/演示采集；30/30 为最终评估边界；硬件单平台验证。",
                "evidence": [
                    quote_between(
                        "19.1分钟",
                        "纯机器人交互数据",
                        "收敛时长",
                        "文内对平均在线交互数据量的核心数据。",
                    ),
                    quote_between(
                        "44%",
                        "114%",
                        "相对 SFT 提升",
                        "文内对 EXPO-FT 相对 SFT 成功率提升幅度。",
                    ),
                ],
            },
            "# EXPO-FT 数据效率\n\nHIL 局部时序干预；LoRA 微调动作头、Critic 独立 ResNet-50。",
        ),
        (
            {
                "id": "claim_wechat_diffusion_rl_baseline_limits_20260716",
                "title": "该文称 PPO/AWR 等原生高斯策略 RL 难以适配扩散/流匹配 VLA，离线长时序场景中弱于 SFT；两套方案（离线优势 BC vs EXPO-FT）不可混用",
                "tags": ["baseline-comparison", "diffusion-policy", "VLA"],
                "domains": ["reinforcement-learning", "robotics"],
                "confidence": "medium",
                "applicability": ["vs HIL-SERL/DSRL/HG-DAgger/SFT", "离线/在线框架区分"],
                "uncertainty": "基线弱势归因为主讲观点；跨任务泛化与算力成本限制文内已承认。",
                "evidence": [
                    quote_between(
                        "PPO属于在线策略",
                        "纯监督微调",
                        "PPO/AWR 局限",
                        "文内对 PPO/AWR 不适配扩散 VLA 的说明。",
                    ),
                    quote_between(
                        "完全区分",
                        "不可混用",
                        "两套方案边界",
                        "文内强调离线框架与 EXPO-FT 相互独立。",
                    ),
                ],
            },
            "# 基线与边界\n\n扩散 RL 三类离线微调均有上限；EXPO-FT 需人工重置环境。",
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
            "created_at": "2026-07-16T11:05:00+08:00",
            "updated_at": "2026-07-16T11:05:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入 EXPO-FT / 离线 VLA RL 研讨会；等待人工核验",
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
            "Finn/Dong 研讨会转述；实验数字与算法细节需回 EXPO/EXPO-FT 原文核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
