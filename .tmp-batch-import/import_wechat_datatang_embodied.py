from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_cda5a1b9e036598aff53e5be"
EXT = "extraction_c1cb6fe720013eb77dfa08c9"
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
        "reason": "由新智元对数据堂具身数据采集框架的软文归纳；特斯拉/OpenAI 路线为二手引述",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_embodied_data_quality_cost_tradeoff_20260716",
                "title": "该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线",
                "tags": ["embodied-ai", "data-collection", "teleoperation"],
                "domains": ["robotics", "machine-learning"],
                "confidence": "low",
                "applicability": ["2024 特斯拉 vs OpenAI 数据采集路线对比叙述", "Physical AI 数据瓶颈讨论"],
                "uncertainty": "为行业评论/软文；两家公司实际策略细节未 capture 原文，「遇挫」等判断属编辑性表述。",
                "evidence": [
                    quote_between(
                        "特斯拉选择重资产路线",
                        "海量数据",
                        "两条路线",
                        "文内对特斯拉与 OpenAI 采集路线对比。",
                    ),
                    quote_between(
                        "质量",
                        "二选一",
                        "质量成本矛盾",
                        "文内对质量与成本不可兼得的点题。",
                    ),
                ],
            },
            "# 质量 vs 成本\n\n遥操高精度 vs 众包低成本；难以兼得（文内观点）。",
        ),
        (
            {
                "id": "claim_wechat_embodied_data_three_waves_20260716",
                "title": "该文称过去两年数据采集经历真机遥操→UMI 手持夹爪→第一人称 Ego 视频三次迭代",
                "tags": ["umi", "ego-centric", "teleoperation"],
                "domains": ["robotics", "data-engineering"],
                "confidence": "medium",
                "applicability": ["具身数据采集范式演进科普", "UMI/Ego 优缺点对照"],
                "uncertainty": "三次迭代划分为主观框架；各路线缺陷列举来自软文而非系统评测。",
                "evidence": [
                    quote_between(
                        "真机遥操",
                        "Ego Centric",
                        "三次迭代",
                        "文内对三种采集范式的时序划分。",
                    ),
                    quote_between(
                        "解放对采集人的束缚",
                        "精细控制数据",
                        "迭代权衡",
                        "文内对产能扩大与精细控制损失的说明。",
                    ),
                ],
            },
            "# 三次迭代\n\n遥操→UMI→Ego；成本↓但精细控制数据↓。",
        ),
        (
            {
                "id": "claim_wechat_brain_cerebellum_layered_collection_20260716",
                "title": "该文主张「大脑+小脑」分层：场内真机遥操训练小脑执行，场外 Ego 众包训练大脑决策",
                "tags": ["brain-cerebellum", "vla", "vlm"],
                "domains": ["robotics", "embodied-ai"],
                "confidence": "low",
                "applicability": ["场内/场外双范式架构讨论", "长程任务 vs 精细操作数据分工"],
                "uncertainty": "为数据堂提出的框架性主张；与具体模型架构映射为类比性表述。",
                "evidence": [
                    quote_between(
                        "端侧小脑",
                        "分层架构",
                        "分层架构",
                        "文内对大脑/小脑分层类比。",
                    ),
                    quote_between(
                        "场内采集",
                        "肌肉记忆",
                        "场内小脑",
                        "文内对场内遥操服务小脑训练的说明。",
                    ),
                    quote_between(
                        "场外采集",
                        "做什么、为什么",
                        "场外大脑",
                        "文内对场外 Ego 服务大脑决策的说明。",
                    ),
                ],
            },
            "# 大脑+小脑分层\n\n场内遥操→执行；场外 Ego→决策。",
        ),
        (
            {
                "id": "claim_wechat_ego_collection_limitations_20260716",
                "title": "该文列举 Ego 第一人称视频采集优势为低成本可扩展，但缺乏力触觉/精确关节轨迹且需对齐与清洗",
                "tags": ["ego-centric", "data-quality", "limitations"],
                "domains": ["robotics", "computer-vision"],
                "confidence": "medium",
                "applicability": ["Ego 采集方案利弊分析", "EgoScale/DreamDojo 引用语境"],
                "uncertainty": "优劣势为科普归纳；英伟达项目能力数字为二手引述。",
                "evidence": [
                    quote_between(
                        "采集成本极低",
                        "规模可无限放大",
                        "Ego 优势",
                        "文内对 Ego 成本与规模优势的说明。",
                    ),
                    quote_between(
                        "力触觉信息",
                        "双目相机预测",
                        "Ego 局限",
                        "文内对 Ego 缺失力触觉与关键点预测的说明。",
                    ),
                ],
            },
            "# Ego 采集利弊\n\n低成本大规模 vs 无力触觉/需清洗对齐。",
        ),
        (
            {
                "id": "claim_wechat_datatang_factory_scale_20260716",
                "title": "该文称数据堂具身智能数据工厂超 8000 平方米、300 组双臂采集设备，计划年产 10 万小时数据",
                "tags": ["datatang", "data-factory", "crowdsourcing"],
                "domains": ["robotics", "data-engineering"],
                "confidence": "low",
                "applicability": ["数据堂场内工厂与 Ego 众包服务宣传", "2026 具身数据产业化叙述"],
                "uncertainty": "为厂商软文数字；600 采集员、万小时交付等未独立验证。",
                "evidence": [
                    quote_between(
                        "8000平方米",
                        "10万小时",
                        "工厂规模",
                        "文内对数据堂工厂面积与产出计划的说明。",
                    ),
                    quote_between(
                        "300组",
                        "600名",
                        "设备与人员",
                        "文内对双臂设备与采集员规模的说明。",
                    ),
                ],
            },
            "# 数据堂工厂\n\n8000㎡/300 组设备；10 万小时计划（宣传数字）。",
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
            "created_at": "2026-07-16T01:11:00+08:00",
            "updated_at": "2026-07-16T01:11:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入具身数据采集软文；等待人工核验",
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
            "行业软文/厂商宣传；特斯拉/OpenAI/数据堂数据需回原始来源核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
