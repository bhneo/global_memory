from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_2d4f3a7d3525782c8ff503ee"
EXT = "extraction_e3377b150ecb9c199dd5bc48"
_, extraction, body = ExtractionService(repo).find(EXT)
input_sha256 = extraction["input_sha256"]
content_id = extraction["content_id"]


def quote(text: str, section: str, reason: str) -> dict:
    start = body.index(text)
    end = start + len(text)
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
        "reason": "由微信公众号评论文章归纳；非独立 peer-reviewed 论文正文",
    }
]

candidates = [
    (
        {
            "id": "claim_wechat_wam_eval_convergence_20260715",
            "title": "天南具身公园文称近月四篇世界模型相关工作收敛于「拿世界模型去做评估」",
            "tags": ["world-model", "evaluation", "embodied-ai"],
            "domains": ["robot-learning", "world-models"],
            "confidence": "medium",
            "applicability": [
                "2026-07 天南具身公园公众号评论",
                "作者归纳的智元 τ₀-WM、SC3-Eval、World Value Model、GigaWorld-1 四篇工作",
            ],
            "uncertainty": "收敛判断来自作者个人阅读归纳，非系统综述；四篇论文本身未在本仓库 capture，不能将作者归类等同于各论文自述。",
            "evidence": [
                quote(
                    "四拨人，四个方向，团队肯定没碰过，但他们这一个月放出来的东西，指向的居然是同一件事：\n\n拿世界模型去做评估。",
                    "行业转向",
                    "作者对四篇工作共同方向的直接归纳。",
                ),
                quote(
                    "一个月之内，我被四篇非常 Solid 的论文轮着轰炸了一遍，分别来自智元罗剑岚、英伟达和 PI、字节，还有极佳（GigaWorld-1）。",
                    "引用范围",
                    "限定作者所指的四处来源。",
                ),
                para(
                    "来源层级",
                    "公众号评论文章，引用多篇外部论文",
                    "提醒主张层级低于原始论文。",
                ),
            ],
        },
        "# 世界模型评估方向收敛\n\n作者认为四篇近期工作共同指向用世界模型做 policy 评估，而非直接生成动作。",
    ),
    (
        {
            "id": "claim_wechat_embodied_eval_bottleneck_20260715",
            "title": "该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住",
            "tags": ["real-robot", "evaluation", "vla"],
            "domains": ["robotics", "robot-learning"],
            "confidence": "medium",
            "applicability": [
                "作者描述的具身 VLA 真机评测流程",
                "需要排队、人工摆场、逐次记录的场景",
            ],
            "uncertainty": "来自作者基于行业经验的论断，未给出量化对比实验；「一两天出分」为顺利情况下的经验描述。",
            "evidence": [
                quote(
                    "具身的 VLA 训完一版，想知道行不行，得提交给真机评测团队，先排队，再由人一件件把测试道具摆到场地上，守着机器人一遍遍跑、一次次记，顺利的话一两天后才出个分。",
                    "真机评测流程",
                    "作者对评估流程耗时的具体描述。",
                ),
                quote(
                    "迭代速度，很多时候不是被训练卡住的，是被评估卡住的。",
                    "瓶颈判断",
                    "作者对瓶颈来源的判断句。",
                ),
            ],
        },
        "# 评估瓶颈\n\n真机评测排队与人工摆场使迭代受评估而非训练限制。",
    ),
    (
        {
            "id": "claim_wechat_eval_vs_action_tradeoff_20260715",
            "title": "该文认为世界模型做评估因「错得起」可能比直接生成动作更易先落地",
            "tags": ["world-model", "evaluation", "world-action-model"],
            "domains": ["world-models", "robot-learning"],
            "confidence": "medium",
            "applicability": [
                "作者对世界模型两条应用路线的对比",
                "真机代价较高的动作生成场景",
            ],
            "uncertainty": "属于作者观点性对比，「先落地」未给出可复现判据或统一 benchmark。",
            "evidence": [
                quote(
                    "同样是世界模型，直接生成动作那条线要「少犯贵的错」，难在错不起； 而做评估这条线，恰恰因为错得起，反而先落地了。",
                    "路线对比",
                    "作者对两条路线成本结构的对比。",
                ),
                quote(
                    "世界模型落不了地？没关系，换个思路就行。",
                    "策略转向",
                    "作者对应用路线切换的表述。",
                ),
            ],
        },
        "# 评估 vs 动作生成\n\n评估路线因错误成本较低，作者认为更易率先落地。",
    ),
    (
        {
            "id": "claim_wechat_sc3_eval_correlation_20260715",
            "title": "该文称英伟达与 PI 的 SC3-Eval 与真机相关性达 0.929 且能复现真机失败",
            "tags": ["world-model", "evaluation", "sc3-eval"],
            "domains": ["world-models", "robotics"],
            "confidence": "low",
            "applicability": [
                "作者对 SC3-Eval 论文结果的转述",
                "视频模型用于 rollout 评估的设定",
            ],
            "uncertainty": "0.929 与失败复现能力均经公众号二次转述；SC3-Eval 原文未 capture；未说明相关性指标定义与样本量。",
            "evidence": [
                quote(
                    "SC3-Eval解的是另一个事：视频模型拿来评估，最怕它一本正经地胡说八道，画面顺、物理假。他们逼模型「自己跟自己对账」，正着生成画面、反着从画面倒推动作，俩一旦对不上，就说明它在瞎编了，直接把这条 rollout 掐掉。",
                    "SC3-Eval 方法",
                    "作者对 SC3-Eval 机制的描述。",
                ),
                quote(
                    "做到了跟真机 0.929 的相关性，更狠的是能把真机上真实出现过的失败给复现出来。",
                    "SC3-Eval 结果",
                    "作者转述的相关性与失败复现表述。",
                ),
            ],
        },
        "# SC3-Eval 转述\n\n作者称 SC3-Eval 与真机相关性 0.929。",
    ),
    (
        {
            "id": "claim_wechat_gigaworld_vlm_negative_corr_20260715",
            "title": "该文转述 GigaWorld-1 结论：用 VLM 给世界模型物理一致性打分会与人工金标准负相关",
            "tags": ["world-model", "evaluation", "vlm", "gigaworld"],
            "domains": ["world-models", "robot-learning"],
            "confidence": "low",
            "applicability": [
                "作者对 GigaWorld-1 / 极佳 CVPR World Model Track 的解读",
                "以 rollout 成功失败与真机对齐为金标准的评估设定",
            ],
            "uncertainty": "负相关结论经公众号转述 GigaWorld-1；具体 VLM 型号、样本量与相关系数未在文中给出；GigaWorld-1 原文未 capture。",
            "evidence": [
                quote(
                    "王啸峰在访谈中给的答案，是一个「金标准」（golden metric）：世界模型里 rollout 出来的成功和失败，必须和真机 rollout 的成功失败完全对上。这边成功，那边也成功；这边失败，那边就一定失败。就这么硬。",
                    "金标准定义",
                    "作者转述的 golden metric 定义。",
                ),
                quote(
                    "最典型的就是 VLM。现在很多人图省事，直接拿一个多模态大模型去给世界模型的物理一致性打分。极佳实测的结论是：VLM 打出来的这个分，跟金标准是负相关的。",
                    "VLM 负相关",
                    "作者转述 GigaWorld-1 对 VLM 打分的结论。",
                ),
                para(
                    "来源层级",
                    "结论来自对 GigaWorld-1 与访谈的二次解读",
                    "需回原文核验指标与实验设置。",
                ),
            ],
        },
        "# GigaWorld-1 / VLM\n\n作者转述：VLM 物理一致性分数与人工金标准负相关。",
    ),
]

out_dir = Path(".tmp-batch-import")
out_dir.mkdir(exist_ok=True)
prompt = out_dir / "prompt-knowledge-import.md"
svc = ProposalService(repo)

for meta, body_text in candidates:
    meta = {
        **meta,
        "type": "claim",
        "status": "proposal",
        "created_at": "2026-07-15T18:12:00+08:00",
        "updated_at": "2026-07-15T18:12:00+08:00",
        "aliases": [],
        "superseded_by": None,
        "valid_during": None,
        "change_reason": "批量导入微信文章知识；等待人工核验",
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
        "公众号评论文章；多处为对第三方论文/访谈的二次转述，需回原文核验。",
        f"导入 {meta['id']}",
        prompt if prompt.is_file() else None,
    )
    print(result.proposal_id, meta["id"])
