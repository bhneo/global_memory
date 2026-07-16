from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_ef99e322cc662cffb7eb5c8f"
EXT = "extraction_a9bbb7d4b3a1e278c955120f"
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
        "reason": "由量子位公众号对 PhySO/Φ-SO 论文报道归纳；非 arXiv 原文 capture",
    }
]

candidates = [
    (
        {
            "id": "claim_wechat_physo_overview_20260715",
            "title": "该文称开源工具 Φ-SO 可直接从实验数据发现物理公式",
            "tags": ["symbolic-regression", "physo", "physics-ai"],
            "domains": ["physics", "machine-learning"],
            "confidence": "medium",
            "applicability": [
                "2023 量子位对 PhySO 开源报道",
                "GitHub: WassimTenachi/PhySO",
            ],
            "uncertainty": "为科技媒体报道而非论文正文；「一步到位」为媒体表述；实际性能需回 arXiv:2303.03192 核验。",
            "evidence": [
                quote_between(
                    "它名叫Φ-SO",
                    "直接给出对应公式。",
                    "工具能力",
                    "文内对 Φ-SO 功能的直接描述。",
                ),
                quote_between(
                    "GitHub：",
                    "https://github.com/WassimTenachi/PhySO",
                    "开源链接",
                    "文内给出的代码仓库。",
                ),
                para(
                    "来源层级",
                    "报道链接 arXiv:2303.03192 但原文未 capture",
                    "提醒需回论文核验实验设置。",
                ),
            ],
        },
        "# Φ-SO 概述\n\n开源符号回归工具，从数据发现公式。",
    ),
    (
        {
            "id": "claim_wechat_physo_laptop_runtime_20260715",
            "title": "该文称 Φ-SO 在笔记本上约 4 小时可恢复爱因斯坦质能方程",
            "tags": ["physo", "runtime", "symbolic-regression"],
            "domains": ["physics", "machine-learning"],
            "confidence": "low",
            "applicability": [
                "文内爱因斯坦能量公式实验叙述",
                "无需超算、普通笔记本设定",
            ],
            "uncertainty": "4 小时为媒体报道的单点案例，未给出硬件规格、数据量或随机种子；不能外推为所有公式的一般运行时间。",
            "evidence": [
                quote_between(
                    "整个过程也不需要动用超算",
                    "就能搞定爱因斯坦的质能方程。",
                    "运行时间",
                    "文内对硬件需求与耗时的表述。",
                ),
            ],
        },
        "# 笔记本运行时间\n\n报道称约 4 小时恢复质能方程。",
    ),
    (
        {
            "id": "claim_wechat_physo_method_20260715",
            "title": "该文称 Φ-SO 使用 RNN+强化学习的深度符号回归，并纳入物理先验约束搜索空间",
            "tags": ["symbolic-regression", "reinforcement-learning", "rnn"],
            "domains": ["machine-learning", "physics"],
            "confidence": "medium",
            "applicability": ["量子位对 PhySO 方法栈的概述", "深度符号回归 + 物理条件先验"],
            "uncertainty": "方法描述为媒体压缩版；RL 奖励设计等细节需回论文；不等同于独立方法评估。",
            "evidence": [
                quote_between(
                    "Φ-SO背后的技术被叫做",
                    "循环神经网络（RNN）+强化学习实现。",
                    "方法名称",
                    "文内对技术路线的命名与组件。",
                ),
                quote_between(
                    "同时将物理条件作为先验知识纳入学习过程中",
                    "可以大大减少搜索空间。",
                    "物理先验",
                    "文内对先验约束作用的描述。",
                ),
                quote_between(
                    "于是强化学习的规则被设计成",
                    "鼓励模型充分探索搜索空间。",
                    "RL 奖励",
                    "文内对符号回归 RL 奖励设计的描述。",
                ),
            ],
        },
        "# 方法栈\n\nRNN + RL 深度符号回归，带物理先验。",
    ),
    (
        {
            "id": "claim_wechat_physo_classic_recovery_20260715",
            "title": "该文称 Φ-SO 对阻尼谐振子、爱因斯坦能量与万有引力等经典公式实验均 100% 还原且各方法缺一不可",
            "tags": ["physo", "benchmark", "symbolic-regression"],
            "domains": ["physics", "machine-learning"],
            "confidence": "low",
            "applicability": [
                "文内列举的三类经典公式实验",
                "作者通过媒体报道给出的结果概述",
            ],
            "uncertainty": "100% 与「缺一不可」为报道转述论文结论，未给出 ablation 细节、噪声水平或失败案例；需回 arXiv 原文核验。",
            "evidence": [
                quote_between(
                    "研究团队用阻尼谐振子解析表达式",
                    "牛顿的万有引力公式等经典公式来做实验。",
                    "实验对象",
                    "文内列举的 benchmark 公式。",
                ),
                quote_between(
                    "Φ-SO都能100%的从数据中还原这些公式",
                    "以上方法缺一不可。",
                    "实验结果",
                    "文内对还原率与 ablation 结论的转述。",
                ),
            ],
        },
        "# 经典公式 benchmark\n\n报道称 100% 还原且方法组件缺一不可。",
    ),
    (
        {
            "id": "claim_wechat_physo_provenance_20260715",
            "title": "该文称 PhySO 研究来自斯特拉斯堡大学与 CSIRO Data61，历时约 1.5 年",
            "tags": ["physo", "provenance"],
            "domains": ["physics", "machine-learning"],
            "confidence": "medium",
            "applicability": ["2023 量子位报道中的机构与周期信息", "arXiv:2303.03192 关联论文"],
            "uncertainty": "1.5 年为「论文一作透露」的媒体转述；机构名与论文作者列表需与 arXiv 交叉验证。",
            "evidence": [
                quote_between(
                    "这项成果来自德国斯特拉斯堡大学",
                    "受到学术界广泛关注。",
                    "机构与周期",
                    "文内对来源机构与研究周期的描述。",
                ),
                quote_between(
                    "论文：",
                    "https://arxiv.org/abs/2303.03192",
                    "论文链接",
                    "文内给出的 arXiv 链接。",
                ),
            ],
        },
        "# 研究出处\n\n斯特拉斯堡大学 + CSIRO Data61；报道称 1.5 年。",
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
        "created_at": "2026-07-15T18:45:00+08:00",
        "updated_at": "2026-07-15T18:45:00+08:00",
        "aliases": [],
        "superseded_by": None,
        "valid_during": None,
        "change_reason": "批量导入微信科技报道；等待人工核验",
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
        "科技媒体报道；实验数字与 100% 结论需回 arXiv:2303.03192 核验。",
        f"导入 {meta['id']}",
        prompt if prompt.is_file() else None,
    )
    print(result.proposal_id, meta["id"])
