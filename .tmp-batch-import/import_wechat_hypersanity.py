from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_3413634e4482813fa28da48e"
EXT = "extraction_95c0d98bd7ac31b847b3caa6"
_, extraction, body = ExtractionService(repo).find(EXT)
input_sha256 = extraction["input_sha256"]
content_id = extraction["content_id"]


def quote_slice(start: int, end: int, section: str, reason: str) -> dict:
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


def quote_between(start_marker: str, end_marker: str, section: str, reason: str) -> dict:
    start = body.index(start_marker)
    end = body.index(end_marker, start) + len(end_marker)
    return quote_slice(start, end, section, reason)


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
        "reason": "由利维坦转载的 Aeon/Neel Burton 哲学评论译文归纳；非临床指南或原始研究",
    }
]

candidates = [
    (
        {
            "id": "claim_wechat_laing_breakthrough_20260715",
            "title": "该文转述 R.D. Laing 将癫狂描述为通向更高阶意识的「突破」而非「崩溃」",
            "tags": ["hypersanity", "madness", "psychiatry-history"],
            "domains": ["philosophy", "psychology"],
            "confidence": "medium",
            "applicability": [
                "Neel Burton 对 Laing《经验政治与天堂之鸟》(1967) 的解读",
                "文内 psychosis 与 madness 的区分语境",
            ],
            "uncertainty": "为哲学/文化评论而非临床诊断框架；Laing 原书未 capture；「超智识」非公认术语。",
            "evidence": [
                quote_between(
                    "在这本书中，这位苏格兰精神病学家",
                    "探索之旅。",
                    "Laing 论癫狂",
                    "文内对 Laing 核心观点的转述。",
                ),
                quote_between(
                    "根据莱恩的观点，陷入癫狂",
                    "（breakdown）。",
                    "突破 vs 崩溃",
                    "文内对 Laing 关键对举的直接引述。",
                ),
            ],
        },
        "# Laing 突破论\n\n癫狂被表述为 break-through 而非 break-down。",
    ),
    (
        {
            "id": "claim_wechat_jung_primo_materia_20260715",
            "title": "该文称荣格在一战后前混乱期从「癫狂」经验中获得毕生研究的「首要物质」",
            "tags": ["jung", "unconscious", "hypersanity"],
            "domains": ["psychology", "philosophy"],
            "confidence": "medium",
            "applicability": [
                "荣格自传《回忆·梦·思考》叙述",
                "1913 后与弗洛伊德决裂后的个人危机期",
            ],
            "uncertainty": "来自荣格自传与 Burton 评论的双重转述；幻象人物（莎乐美、费莱蒙）为荣格自述，非第三方可验证事实。",
            "evidence": [
                quote_between(
                    "1913年，在第一次世界大战前夕",
                    "与无意识持续对抗着”。",
                    "荣格危机期",
                    "文内对时间线与状态的描述。",
                ),
                quote_between(
                    "并认为他在自己的癫狂中找到了",
                    "（primo materia）”。",
                    "primo materia",
                    "文内对荣格自我评价的转述。",
                ),
            ],
        },
        "# 荣格 primo materia\n\n危机期后被叙述为获得首要研究材料。",
    ),
    (
        {
            "id": "claim_wechat_psychosis_hypersanity_contrast_20260715",
            "title": "该文区分精神病症与超智识：二者皆被主流视为越界，但后者被描述为解放而非痛不欲生",
            "tags": ["psychosis", "hypersanity", "philosophy"],
            "domains": ["psychology", "philosophy"],
            "confidence": "medium",
            "applicability": ["Burton 对 psychosis 与 hypersanity 的概念对比", "文化哲学评论语境"],
            "uncertainty": "对比为作者规范性论述，非流行病学或诊断标准；不应用于替代临床区分。",
            "evidence": [
                quote_between(
                    "精神病症（psychosis）和超智识都将我们置身于社会之外",
                    "像是“疯子”。",
                    "共同社会位置",
                    "文内对两种状态的共同描述。",
                ),
                quote_between(
                    "但鉴于精神障碍令人痛不欲生且行动不能",
                    "解放和赋能。",
                    "体验差异",
                    "文内对两者体验后果的对比。",
                ),
            ],
        },
        "# psychosis vs 超智识\n\n前者被描述为痛苦失能，后者为解放赋能。",
    ),
    (
        {
            "id": "claim_wechat_laing_normal_violence_20260715",
            "title": "该文引 Laing 称「正常人」在过去约 50 年杀害约一亿同胞",
            "tags": ["laing", "social-critique", "violence"],
            "domains": ["philosophy", "psychology"],
            "confidence": "low",
            "applicability": [
                "Laing《经验政治》(1967) 引文",
                "编者注限定为 1967 前半个世纪",
            ],
            "uncertainty": "数字为 Laing 1967 年书中的修辞性论断；编者注称 WWII 直接死亡约七千万，与「一亿」口径不同；属哲学社会批判非历史统计。",
            "evidence": [
                quote_between(
                    "在过去的50年",
                    "他们的同胞。",
                    "Laing 引文",
                    "文内直接引述 Laing 数字。",
                ),
                quote_between(
                    "（编者注：此处应考虑到莱恩此书的书写年份",
                    "约为7,000万）",
                    "编者注",
                    "文内对引文时间范围与数量的限定说明。",
                ),
            ],
        },
        "# Laing 正常人暴力论\n\n1967 前半个世纪约一亿杀害的引述。",
    ),
    (
        {
            "id": "claim_wechat_diogenes_cosmopolitan_20260715",
            "title": "该文称第欧根尼回答来处时说「我是世界公民」，为有史以来首次使用 cosmopolitan 一词",
            "tags": ["diogenes", "cynicism", "cosmopolitanism"],
            "domains": ["philosophy", "history"],
            "confidence": "low",
            "applicability": ["Burton 对犬儒派第欧根尼轶事的转述", "古希腊哲学史叙述"],
            "uncertainty": "「首次使用」为文内断言，未给出古典文献出处；属哲学轶事传统，需回 primary sources 核验。",
            "evidence": [
                quote_between(
                    "另一次，当第欧根尼被问及来自何处时",
                    "世界公民”这个词。",
                    "世界公民",
                    "文内对第欧根尼回答及历史断言的叙述。",
                ),
                quote_between(
                    "第欧根尼在故乡家锡诺帕（Sinope）因为重铸货币而被驱逐出境",
                    "被驱逐出境",
                    "生平背景",
                    "文内对第欧根尼流亡背景的简述。",
                ),
                para(
                    "来源层级",
                    "哲学史轶事经 Aeon 文章与利维坦译文二次转述",
                    "提醒非一手古典文献。",
                ),
            ],
        },
        "# 第欧根尼 cosmopolite\n\n文内称首次使用「世界公民」一词。",
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
        "created_at": "2026-07-15T18:35:00+08:00",
        "updated_at": "2026-07-15T18:35:00+08:00",
        "aliases": [],
        "superseded_by": None,
        "valid_during": None,
        "change_reason": "批量导入微信哲学评论译文；等待人工核验",
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
        "哲学/精神病学文化评论；非临床建议；多处为 Laing/Jung 著作二次转述。",
        f"导入 {meta['id']}",
        prompt if prompt.is_file() else None,
    )
    print(result.proposal_id, meta["id"])
