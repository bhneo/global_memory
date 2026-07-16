from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_a86d60369a021d93d1e863aa"
EXT = "extraction_59d5676353f0e4b5a43e38ec"
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
        "reason": "由中科院物理所公众号科普文章归纳；非原始研究论文",
    }
]

candidates = [
    (
        {
            "id": "claim_wechat_pi_irrational_20260715",
            "title": "该文称 π 是无理数，不能表示为两整数之比，且为无限不循环小数",
            "tags": ["pi", "irrational-number", "mathematics"],
            "domains": ["mathematics"],
            "confidence": "high",
            "applicability": ["科普文章对 π 基本性质的陈述", "小学/大学数学常识语境"],
            "uncertainty": "无理数性质为数学定论；文章同时称 π 是超越数，该句亦在文中出现但未单独成 claim。",
            "evidence": [
                quote_between(
                    "题干中，之所以要强调",
                    "无限不循环小数。",
                    "无理数定义",
                    "文内对 π 不能写成整数比与无限不循环的描述。",
                ),
                quote_between(
                    "它是无理数，无限不循环",
                    "不是任何一个有理数系数多项式的根。",
                    "超越数",
                    "文内对 π 为超越数的补充说明。",
                ),
            ],
        },
        "# π 的无理性\n\n不能表为整数比；无限不循环；超越数。",
    ),
    (
        {
            "id": "claim_wechat_zu_chongzhi_355_113_20260715",
            "title": "该文称祖冲之在公元 462 年给出 355/113 作为 π 近似值，并在近 800 年内为最高精度",
            "tags": ["pi", "history-of-mathematics", "zu-chongzhi"],
            "domains": ["mathematics", "history"],
            "confidence": "medium",
            "applicability": ["文内对中国古代圆周率史的叙述", "355/113 历史近似值讨论"],
            "uncertainty": "800 年「最高精度」为科普表述，需与史学文献交叉验证；误差示例（直径 10000 米差 3 毫米）为文内推算。",
            "evidence": [
                quote_between(
                    "公元462年，祖冲之在《缀术》中记载",
                    "3.1415929203...",
                    "355/113 记载",
                    "文内对祖冲之近似值与展开小数的描述。",
                ),
                quote_between(
                    "在之后近800年的时间内",
                    "准确度最高的π估算值。",
                    "历史精度",
                    "文内对 355/113 保持领先时间的断言。",
                ),
                quote_between(
                    "假设一个圆的直径是10000米",
                    "仅仅多了不到3毫米！",
                    "误差示例",
                    "文内用 355/113 计算的精度直观例子。",
                ),
            ],
        },
        "# 祖冲之 355/113\n\n历史高精度近似与误差示例。",
    ),
    (
        {
            "id": "claim_wechat_buffon_needle_20260715",
            "title": "该文称蒲丰投针实验中当平行线间距 a 等于 2 倍针长 l 时，n/k 近似 π",
            "tags": ["pi", "buffon-needle", "probability"],
            "domains": ["mathematics", "probability"],
            "confidence": "medium",
            "applicability": ["文内 a=2l 的小游戏设定", "蒲丰实验概率推导概述"],
            "uncertainty": "近似关系依赖大数定律与实验次数；文内亦指出精确度与投掷次数不成简单正比并提及最优停止问题。",
            "evidence": [
                quote_between(
                    "在纸上画满相距4厘米的平行线",
                    "与圆周率π十分接近！",
                    "实验步骤",
                    "文内对投针统计与 π 接近性的描述。",
                ),
                quote_between(
                    "在上述小游戏中，我们选择了参数a=2l",
                    "正好得到n/k=π。",
                    "a=2l 结论",
                    "文内对参数选择与 n/k=π 的推导结论。",
                ),
                quote_between(
                    "蒲丰实验是第一个用几何形式表达概率问题的例子",
                    "促进了积分几何学的诞生。",
                    "历史意义",
                    "文内对蒲丰实验历史地位的表述。",
                ),
            ],
        },
        "# 蒲丰投针\n\na=2l 时 n/k 近似 π。",
    ),
    (
        {
            "id": "claim_wechat_pi_supercomputer_benchmark_20260715",
            "title": "该文称多万亿位 π 计算常用于检验超算性能，且 39 位精度即可把可观测宇宙圆周算到原子尺度",
            "tags": ["pi", "supercomputer", "benchmark"],
            "domains": ["mathematics", "computing"],
            "confidence": "medium",
            "applicability": ["文内对超算 π 计算用途的说明", "宇宙学精度需求讨论"],
            "uncertainty": "39 位与「原子大小」为科普数量级说法，未给出推导来源；2021/2022 纪录为媒体报道需可核对。",
            "evidence": [
                quote_between(
                    "事实上，如果从实际测量的角度而言",
                    "这已经能够满足目前绝大多数宇宙学的计算需求了。",
                    "39 位精度",
                    "文内对 π 有效精度需求的表述。",
                ),
                quote_between(
                    "用超级计算机去计算多位π值",
                    "常用方法。",
                    "超算检验",
                    "文内对 π 作为超算 benchmark 的说明。",
                ),
                quote_between(
                    "2021 年8月，瑞士的科学家刷新世界纪录",
                    "耗时108天零9小时。",
                    "2021 纪录",
                    "文内对 2021 计算纪录的转述。",
                ),
                quote_between(
                    "2022 年 3 月， Google Cloud",
                    "恰好是0。",
                    "2022 纪录",
                    "文内对 2022 Google Cloud 100 万亿位的转述。",
                ),
            ],
        },
        "# 超算与 π\n\nbenchmark 用途；39 位宇宙尺度；2021/2022 纪录。",
    ),
    (
        {
            "id": "claim_wechat_pi_leibniz_convergence_20260715",
            "title": "该文称莱布尼茨级数项次足够多时可逼近 π，但收敛很慢，约 500,000 项才到第五位小数",
            "tags": ["pi", "leibniz-formula", "series"],
            "domains": ["mathematics"],
            "confidence": "medium",
            "applicability": ["文内对 π 的莱布尼茨公式收敛性的科普描述", "大学微积分语境"],
            "uncertainty": "500,000 项到第五小数为文内单点说法，未给出误差界推导；级数收敛性本身为经典结果。",
            "evidence": [
                quote_between(
                    "毕竟，这是π的莱布尼茨公式",
                    "总和一定会慢慢接近π。",
                    "莱布尼茨公式",
                    "文内对级数收敛性的描述。",
                ),
                quote_between(
                    "虽然，这个数列的收敛速度很慢",
                    "才能精确到π的第五小数...",
                    "收敛速度",
                    "文内对所需项次的数量级说明。",
                ),
            ],
        },
        "# 莱布尼茨级数\n\n收敛极慢；约 50 万项到第五位小数。",
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
        "created_at": "2026-07-15T19:25:00+08:00",
        "updated_at": "2026-07-15T19:25:00+08:00",
        "aliases": [],
        "superseded_by": None,
        "valid_during": None,
        "change_reason": "批量导入圆周率科普文章；等待人工核验",
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
        "科普文章；超算纪录与历史断言需独立核对；部分为经典数学结论。",
        f"导入 {meta['id']}",
        prompt if prompt.is_file() else None,
    )
    print(result.proposal_id, meta["id"])
