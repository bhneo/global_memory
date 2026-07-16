from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_91199da18f239c48bbcdd49f"
EXT = "extraction_b0ef424e09475b568376445b"
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
        "reason": "Synced 机器之心 2020 综述：内在动机在 RL 中的应用；引述 Baldassarre/Barto/h-DQN/texplore-vanir/MARL 等文献",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_im_rl_baldassarre_distinction_20260716",
                "title": "该文引述 Baldassarre：外在动机为外部奖励驱动行为，内在动机为因事物本身有趣/愉悦而行动，后者推动知识与技能积累",
                "tags": ["intrinsic-motivation", "extrinsic-motivation", "evolution"],
                "domains": ["psychology", "reinforcement-learning"],
                "confidence": "medium",
                "applicability": ["内在/外在动机概念区分", "进化适应度 vs 延迟收益技能"],
                "uncertainty": "为 2020 科普综述转述 Baldassarre [1]；生物学机制细节需回原文。",
                "evidence": [
                    quote_between(
                        "Baldassarre",
                        "外部提供的奖励",
                        "Baldassarre 引入",
                        "文内对 Baldassarre 生物学视角的引述起点。",
                    ),
                    quote_between(
                        "外在动机是指",
                        "后期才能够显现作用",
                        "内外动机进化差异",
                        "文内对内外动机定义与进化功能的对比。",
                    ),
                ],
            },
            "# Baldassarre 区分\n\n外在动机直接服务适应度；内在动机积累可延迟使用的技能与知识。",
        ),
        (
            {
                "id": "claim_wechat_im_rl_framework_internal_rewards_20260716",
                "title": "该文称经典 RL 虽常被视为仅处理外在奖励，但 Barto 等框架可将奖励生成机制置于「内部环境」，内在与外在奖励可统一建模",
                "tags": ["reinforcement-learning", "intrinsic-motivation", "Barto"],
                "domains": ["reinforcement-learning", "cognitive-science"],
                "confidence": "medium",
                "applicability": ["RL 内部/外部奖励通道讨论", "图 1/图 2 环境划分"],
                "uncertainty": "概念性综述；具体实现因任务而异。",
                "evidence": [
                    quote_between(
                        "RL 框架同样适合",
                        "内在动机的原理",
                        "RL 可结合 IM",
                        "文内对 RL 适用性的核心论断。",
                    ),
                    quote_between(
                        "奖励信号是内在的还是外在的",
                        "并不需要专门区分",
                        "统一奖励视角",
                        "文内强调 RL 只关注奖励生成机制而非标签。",
                    ),
                ],
            },
            "# RL 统一奖励\n\n内在奖励可在体内生成；RL 框架不必限定外部通道。",
        ),
        (
            {
                "id": "claim_wechat_im_rl_hdqn_hierarchy_20260716",
                "title": "该文介绍 Kulkarni 的 h-DQN：元控制器最大化外在奖励选目标，控制器以内在奖励学习达成子目标的原子动作",
                "tags": ["h-DQN", "hierarchical-rl", "goal-driven"],
                "domains": ["reinforcement-learning", "deep-learning"],
                "confidence": "medium",
                "applicability": ["稀疏奖励环境", "分层时间尺度 Q 学习"],
                "uncertainty": "架构描述来自综述；超参与实验细节需回 NIPS 2016 原文。",
                "evidence": [
                    quote_between(
                        "hierarchical-DQN",
                        "h-DQN",
                        "h-DQN 引入",
                        "文内对 h-DQN 框架名称与提出者。",
                    ),
                    quote_between(
                        "元控制器",
                        "外在奖励",
                        "分层奖励分工",
                        "文内对元控制器与控制器奖励分工的说明。",
                    ),
                ],
            },
            "# h-DQN\n\n顶层选目标（外在）；底层学动作（内在）；稀疏反馈下先学子技能。",
        ),
        (
            {
                "id": "claim_wechat_im_rl_texplore_vanir_20260716",
                "title": "该文介绍 texplore-vanir：结合模型预测方差奖励与状态空间新颖性奖励，驱动机器人好奇探索并加速模型学习",
                "tags": ["curiosity", "model-based-rl", "exploration"],
                "domains": ["robotics", "reinforcement-learning"],
                "confidence": "medium",
                "applicability": ["基于模型 RL 探索", "Nao 机器人按钮任务实验叙述"],
                "uncertainty": "实验结论（7/13 vs 0/13）来自综述转述 Hester & Stone 2017。",
                "evidence": [
                    quote_between(
                        "Variance-And-Novelty-Intrinsic-Rewards",
                        "texplore-vanir",
                        "算法命名",
                        "文内对 texplore-vanir 算法全称与简称。",
                    ),
                    quote_between(
                        "变异报酬",
                        "Novelty-reward",
                        "双重内在奖励",
                        "文内对方差奖励与新颖性奖励的定义段落。",
                    ),
                ],
            },
            "# texplore-vanir\n\n方差奖励探索模型不确定区域；新颖性奖励远离已访问状态。",
        ),
        (
            {
                "id": "claim_wechat_im_rl_social_influence_marl_20260716",
                "title": "该文介绍多智能体「社会影响」内在奖励：用反事实行动评估对同伴行为的因果影响，据称在 Cleanup/Harvest 中优于基线",
                "tags": ["multi-agent-rl", "social-influence", "communication"],
                "domains": ["reinforcement-learning", "multi-agent-systems"],
                "confidence": "medium",
                "applicability": ["MARL 合作困境", "MOA 模块与通信协议学习"],
                "uncertainty": "因果影响≈互信息的论述为综述归纳；Jaques et al. 2018 细节需回原文。",
                "evidence": [
                    quote_between(
                        "Social Influence as Intrinsic Motivation",
                        "multi-agent reinforcement learning",
                        "社会影响论文",
                        "文内对社会影响 MARL 论文的标题级引述。",
                    ),
                    quote_between(
                        "反事实",
                        "因果影响",
                        "反事实因果",
                        "文内对反事实评估因果影响机制的核心说明。",
                    ),
                ],
            },
            "# 社会影响 MARL\n\n奖励对其他智能体行为有因果影响的动作；可鼓励合作与通信。",
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
            "created_at": "2026-07-16T10:42:00+08:00",
            "updated_at": "2026-07-16T10:42:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入内在动机×RL 综述；等待人工核验",
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
            "Synced 2020 综述转述多篇 RL/机器人论文；实验数据需回原文核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
