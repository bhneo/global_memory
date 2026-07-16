from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_9d39636775b188c87d6a001f"
EXT = "extraction_c6f5aba2b1a589d028d27b57"
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
        "reason": "由 DataCafe/雪鹅经中科院物理所转载的非遍历性与凯利公式科普归纳；Thorp 等原书未 capture",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_non_ergodic_coin_game_20260716",
                "title": "该文以 +80%/-50% 公平硬币复利游戏说明：群体平均财富可增长但多数个体长期变穷，属非遍历性陷阱",
                "tags": ["non-ergodicity", "gambling", "wealth-dynamics"],
                "domains": ["probability", "behavioral-economics"],
                "confidence": "medium",
                "applicability": ["+80%/-50% 重复抛硬币财富过程", "10 万玩家各 100 轮模拟叙述"],
                "uncertainty": "72 元阈值等为文内模拟叙述；非原始论文实验，参数需自行复现核验。",
                "evidence": [
                    quote_between(
                        "财富增加 80%",
                        "不到72元",
                        "硬币游戏设定",
                        "文内对游戏规则与多数玩家结局的说明。",
                    ),
                    quote_between(
                        "非遍历性陷阱",
                        "个体命运",
                        "陷阱本质",
                        "文内对误把群体平均当个体命运的点题。",
                    ),
                ],
            },
            "# 非遍历硬币游戏\n\n群体平均↑ vs 多数个体↓；+80%/-50% 例。",
        ),
        (
            {
                "id": "claim_wechat_ergodicity_time_vs_ensemble_20260716",
                "title": "该文称遍历性指时间平均与群体平均等价；现实生活常非遍历，个体可能因一次失败出局",
                "tags": ["ergodicity", "time-average", "ensemble-average"],
                "domains": ["statistical-physics", "decision-theory"],
                "confidence": "medium",
                "applicability": ["遍历性假设科普", "路径依赖与单次生命路径语境"],
                "uncertainty": "玻尔兹曼遍历性为经典物理假设简化；向人生/金融决策的推广为科普类比。",
                "evidence": [
                    quote_between(
                        "时间平均",
                        "群体平均",
                        "遍历性定义",
                        "文内对时间平均与群体平均关系的说明。",
                    ),
                    quote_between(
                        "非遍历的",
                        "直接出局",
                        "非遍历现实",
                        "文内对资源有限与出局风险的表述。",
                    ),
                ],
            },
            "# 遍历 vs 非遍历\n\n时间平均≈群体平均仅在有遍历时；出局不可逆。",
        ),
        (
            {
                "id": "claim_wechat_multiplicative_jensen_gap_20260716",
                "title": "该文称乘法型过程中几何平均（长期增长率）低于算术平均，个体长期表现系统性低于群体平均",
                "tags": ["jensen-inequality", "geometric-mean", "multiplicative-process"],
                "domains": ["probability", "finance"],
                "confidence": "medium",
                "applicability": ["复利/乘法财富过程", "波动越大差距越大叙述"],
                "uncertainty": "公式在提取文本中被省略为文字描述；严格条件与证明未给出。",
                "evidence": [
                    quote_between(
                        "Jensen",
                        "差距越明显",
                        "Jensen 不等式",
                        "文内对几何平均小于算术平均的解释。",
                    ),
                    quote_between(
                        "乘法型",
                        "结构使然",
                        "乘法系统",
                        "文内对上行有限、下行无底的乘法特征。",
                    ),
                ],
            },
            "# 几何 vs 算术平均\n\n乘法过程：个体长期低于群体算术平均。",
        ),
        (
            {
                "id": "claim_wechat_kelly_bet_fraction_20260716",
                "title": "该文称对上述硬币游戏凯利公式建议每次下注总资金的 37.5%，以平衡增长与避免爆仓",
                "tags": ["kelly-criterion", "bet-sizing", "risk-management"],
                "domains": ["probability", "finance"],
                "confidence": "medium",
                "applicability": ["+80%/-50% 公平硬币重复博弈", "Kelly 最优下注比例科普"],
                "uncertainty": "37.5% 为文内给定值；p/b/a 参数推导步骤在科普中被压缩，需独立验算。",
                "evidence": [
                    quote_between(
                        "Kelly",
                        "37.5%",
                        "凯利公式",
                        "文内对凯利公式来源与下注比例建议。",
                    ),
                    quote_between(
                        "押得太多",
                        "活得下去",
                        "下注权衡",
                        "文内对过大/过小下注的风险说明。",
                    ),
                ],
            },
            "# 凯利 37.5%\n\n硬币游戏最优下注比例（文内叙述）。",
        ),
        (
            {
                "id": "claim_wechat_kelly_simulation_survival_20260716",
                "title": "该文模拟 10 万人 200 轮硬币博弈：100% 全押几乎全灭，37.5% 凯利下注多数人稳健增值",
                "tags": ["simulation", "kelly-criterion", "bankruptcy"],
                "domains": ["probability", "behavioral-economics"],
                "confidence": "low",
                "applicability": ["作者自研 10 万人×200 轮模拟叙述", "100%/65%/37.5%/10% 策略对比"],
                "uncertainty": "模拟为文内自述未附代码/数据；幂律分布等结论需复现验证。",
                "evidence": [
                    quote_between(
                        "100%下注",
                        "几乎全灭",
                        "全押结果",
                        "文内对 100% 下注策略模拟结果的说明。",
                    ),
                    quote_between(
                        "37.5% 下注",
                        "最优财富积累",
                        "凯利模拟",
                        "文内对 37.5% 策略分布特征的描述。",
                    ),
                ],
            },
            "# 下注策略模拟\n\n全押≈全灭；凯利兼顾生存与增值（文内模拟）。",
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
            "created_at": "2026-07-16T00:36:00+08:00",
            "updated_at": "2026-07-16T00:36:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入非遍历性/凯利公式科普；等待人工核验",
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
            "概率/决策科普；模拟与 37.5% 需独立验算；Thorp 原文未 capture。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
