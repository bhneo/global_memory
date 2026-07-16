from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_12432807660136b2471717f1"
EXT = "extraction_b2b09f628e4a2fab15043dd6"
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
        "reason": "由利维坦转载的 ScienceAlert 科普译文归纳；非原始研究论文",
    }
]

candidates = [
    (
        {
            "id": "claim_wechat_ganzfeld_mechanism_20260715",
            "title": "该文称甘兹菲尔德效应下，大脑会在均匀感官剥夺场中放大神经元噪音以补偿缺失视觉信号",
            "tags": ["ganzfeld-effect", "sensory-deprivation", "neuroscience"],
            "domains": ["neuroscience", "psychology"],
            "confidence": "medium",
            "applicability": [
                "2016 Scam Nation YouTube 演示的 DIY 感官剥夺设定",
                "眼前漆黑且持续听到电视白噪音的非结构化刺激场",
            ],
            "uncertainty": "机制描述来自科普译文对甘兹菲尔德效应的通俗解释，未引用原始实验论文；ScienceAlert 原文未 capture。",
            "evidence": [
                quote(
                    "你的大脑会通过放大神经元噪音来寻找缺失的视觉信号。",
                    "甘兹菲尔德机制",
                    "文内对大脑补偿缺失视觉信号机制的描述。",
                ),
                quote(
                    "这就会造成我们在视频里看到的那样，人们产生了视力上和听力上的双重幻觉。",
                    "效应结果",
                    "作者对效应后果的归纳。",
                ),
                para(
                    "效应名称",
                    "文内将上述现象称为甘兹菲尔德效应（Ganzfeld effect）",
                    "补充效应名称与来源说明。",
                ),
            ],
        },
        "# 甘兹菲尔德效应\n\n均匀感官剥夺下，大脑放大神经噪音并可能诱发视听幻觉。",
    ),
    (
        {
            "id": "claim_wechat_scam_nation_diy_setup_20260715",
            "title": "该文描述 Scam Nation 演示可用白纸、棉填充、白噪音视频等家用物品在约 10–30 分钟后诱发强烈幻觉",
            "tags": ["sensory-deprivation", "diy-experiment", "hallucination"],
            "domains": ["psychology", "neuroscience"],
            "confidence": "low",
            "applicability": [
                "2016 Scam Nation YouTube 视频演示",
                "至少 30 分钟不间断白噪音/静电干扰音",
            ],
            "uncertainty": "效果时间窗与具体幻觉内容来自视频参与者自述，非对照实验；「只能采信视频中二人的说法」为文内自述。",
            "evidence": [
                quote(
                    "正如2016年Scam Nation频道在YouTube上发布的一段视频所演示的那样，如果用一些常见的家用物品制造出一种高度感官剥夺的情景，你就会产生足以扰乱你的视觉和听觉的强烈幻觉。",
                    "Scam Nation 演示",
                    "文内对视频目的与效果的概述。",
                ),
                quote(
                    "效果通常在10到30分钟后体现出来。",
                    "时间窗",
                    "文内给出的典型起效时间。",
                ),
                quote(
                    "当然，就这个特定场景而言，我们只能采信视频中二人的说法",
                    "证据边界",
                    "文内对证据强度的自我限定。",
                ),
            ],
        },
        "# Scam Nation DIY\n\n家用感官剥夺约 10–30 分钟可报告强烈视听扰动。",
    ),
    (
        {
            "id": "claim_wechat_scam_nation_visuals_20260715",
            "title": "该文转述 Scam Nation 参与者在约 20 分钟后报告彩色光斑并形成恐龙、水母等形状幻觉",
            "tags": ["hallucination", "visual-perception"],
            "domains": ["psychology"],
            "confidence": "low",
            "applicability": ["Scam Nation 节目 20 分钟节点", "两名视频参与者的自述"],
            "uncertainty": "具体视觉内容（恐龙剪影、水母、索伦之眼）为参与者口述，无独立测量；一人报告尖叫、另一人报告笑声，个体差异大。",
            "evidence": [
                quote(
                    "实验进行20分钟后，参与Scam Nation节目的人说，他们看到了",
                    "视觉幻觉自述",
                    "文内对 20 分钟节点视觉体验转述的起始句。",
                ),
                quote(
                    "其中之一听到尖叫声，而另一个人听到笑声。",
                    "听觉差异",
                    "文内对两名参与者听觉体验差异的描述。",
                ),
            ],
        },
        "# Scam Nation 视觉/听觉\n\n20 分钟后参与者自述彩色光斑与成形幻觉。",
    ),
    (
        {
            "id": "claim_wechat_veritasium_sensory_deprivation_20260715",
            "title": "该文称 Veritasium 主持人在 45 分钟漆黑静音房间中主要体验到心脏搏动感被放大，而非完整幻觉",
            "tags": ["sensory-deprivation", "interoception"],
            "domains": ["neuroscience", "psychology"],
            "confidence": "medium",
            "applicability": [
                "Veritasium 频道德里克·穆勒的感官剥夺试验",
                "45 分钟漆黑、极度安静且无回音房间",
            ],
            "uncertainty": "体验报告来自科普视频转述；文内称「并不完全是幻觉」，属主观感受描述。",
            "evidence": [
                quote(
                    "当“真理元素”频道（Veritasium）的主持人德里克·穆勒（Derek Muller）用他自己的方式试验“感官剥夺”时——他把自己关在一个漆黑、极度安静并且没有回音的房间里45分钟——他破除了“丧失刺激致人疯狂”的传言，但同时也表明确实会有一些奇怪的感受。",
                    "Veritasium 试验设定",
                    "文内对试验条件与部分结论的描述。",
                ),
                quote(
                    "“或许我注意到的最奇怪的事情就是对自己心脏的感觉，”他说。",
                    "心脏感受",
                    "穆勒对最显著体验的直接引语。",
                ),
                quote(
                    "在这种情况下，德里克体验到的并不完全是幻觉，但是他所描述的心脏的感受说明他的大脑确实在缺乏刺激的情况下放大了某些感受。",
                    "作者解读",
                    "文内对体验性质的判断。",
                ),
            ],
        },
        "# Veritasium 感官剥夺\n\n45 分钟静音暗室中主要报告内感受（心跳）被放大。",
    ),
    (
        {
            "id": "claim_wechat_mutual_gaze_2015_20260715",
            "title": "该文转述 2015 年实验：志愿者互相直视 10 分钟后报告「前所未有的强烈感受」",
            "tags": ["mutual-gaze", "perception", "psychology"],
            "domains": ["psychology", "neuroscience"],
            "confidence": "low",
            "applicability": [
                "2015 年互相直视实验",
                "英国心理学会 Research Digest 报道转述",
            ],
            "uncertainty": "文内自述「不是一门严谨的科学」；具体实验设计、样本量与原论文未在文中给出；仅经 Research Digest 二次报道。",
            "evidence": [
                quote(
                    "有趣的是，研究人员在2015年的一项实验中也证明了类似的效果，当时他们让志愿者互相直视对方的眼睛保持10分钟。",
                    "2015 实验设定",
                    "文内对实验的基本描述。",
                ),
                quote(
                    "“参与了对视实验的人说，他们产生了前所未有的强烈感受，”克里斯蒂安·贾勒特（Christian Jarrett）在当时发表在英国心理学会《研究文摘》（Research Digest）上的报告中如此提到。",
                    "参与者报告",
                    "文内引述 Research Digest 报道。",
                ),
                quote(
                    "当然，这不是一门严谨的科学，因为每个人的大脑都会对奇怪的东西产生不一样的反应",
                    "证据边界",
                    "文内对实验严谨性的自我限定。",
                ),
            ],
        },
        "# 2015 对视实验\n\n10 分钟互相直视后参与者报告强烈 unusual 感受。",
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
        "created_at": "2026-07-15T18:23:00+08:00",
        "updated_at": "2026-07-15T18:23:00+08:00",
        "aliases": [],
        "superseded_by": None,
        "valid_during": None,
        "change_reason": "批量导入微信科普译文；等待人工核验",
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
        "利维坦转载科普译文；多处为 YouTube/Research Digest 二次转述，非原始研究。",
        f"导入 {meta['id']}",
        prompt if prompt.is_file() else None,
    )
    print(result.proposal_id, meta["id"])
