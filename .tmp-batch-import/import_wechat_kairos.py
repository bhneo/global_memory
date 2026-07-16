from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_a20c5fb22d91216503d413e1"
EXT = "extraction_a5edbc0cf2b49e4a1ec77b62"
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
        "reason": "由 ACERobotics 对大晓机器人 Kairos-HomeWorld 发布稿的转载归纳；项目主页未 capture",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_kairos_dataset_scale_20260716",
                "title": "该文称 Kairos-HomeWorld 开源含 30 万中国真实平面图、5000 个全屋仿真场景与 5 万可交互物体资产",
                "tags": ["kairos-homeworld", "dataset", "simulation"],
                "domains": ["robotics", "embodied-ai"],
                "confidence": "low",
                "applicability": ["中国家庭全屋 3D 数据集规模对比 RPLAN/ResPlan 语境", "2026-06 发布稿"],
                "uncertainty": "为厂商/公众号宣传稿；「全球最大」等表述需回项目主页与论文核验。",
                "evidence": [
                    quote_between(
                        "30万套真实平面图",
                        "仿真引擎训练",
                        "数据集规模（开篇）",
                        "文内开篇对数据集规模的说明。",
                    ),
                    quote_between(
                        "30万张",
                        "5万个",
                        "数据集规模（详述）",
                        "文内对平面图、场景与物体资产数量的详述。",
                    ),
                ],
            },
            "# Kairos 数据规模\n\n30万户型/5千场景/5万物体；宣传性数字待核验。",
        ),
        (
            {
                "id": "claim_wechat_kairos_four_stage_generation_20260716",
                "title": "该文称 Kairos-HomeWorld 采用四阶段分层生成（全局结构—局部细节—闭环校验—交互增强）实现全屋可交互 3D 场景",
                "tags": ["kairos-homeworld", "scene-generation", "world-model"],
                "domains": ["robotics", "computer-vision"],
                "confidence": "low",
                "applicability": ["文本到全屋 3D 生成 pipeline 科普", "K-D 树平面图表示讨论"],
                "uncertainty": "技术细节来自宣传稿；碰撞率等量化指标未给独立 benchmark。",
                "evidence": [
                    quote_between(
                        "四阶段分层生成架构",
                        "交互增强",
                        "四阶段架构",
                        "文内对四阶段 pipeline 的命名。",
                    ),
                    quote_between(
                        "K-D树",
                        "几何漂移",
                        "平面图表示",
                        "文内对 K-D 树平面图表示与 2D-3D 提升的说明。",
                    ),
                ],
            },
            "# 四阶段生成\n\n结构→细节→校验→可交互物体。",
        ),
        (
            {
                "id": "claim_wechat_kairos_china_specific_layout_20260716",
                "title": "该文称该数据集专为中国家庭户型设计，覆盖封闭式厨房、生活阳台、玄关等本土特征，区别于欧美开源室内数据",
                "tags": ["china-housing", "dataset-localization", "indoor-scene"],
                "domains": ["robotics", "embodied-ai"],
                "confidence": "low",
                "applicability": ["本土机器人训练数据本地化讨论", "与欧美 indoor scene 数据集对比"],
                "uncertainty": "「水土不服」为定性判断；具体覆盖城市/户型分布需回官方数据说明。",
                "evidence": [
                    quote_between(
                        "欧美居住习惯",
                        "水土不服",
                        "与欧美数据差异",
                        "文内对欧美数据集局限的表述。",
                    ),
                    quote_between(
                        "封闭式厨房",
                        "复杂户型",
                        "本土特征",
                        "文内对中国家庭布局特征的列举。",
                    ),
                ],
            },
            "# 中国家庭专属\n\n本土户型特征 vs 欧美数据集。",
        ),
        (
            {
                "id": "claim_wechat_kairos_interactive_objects_20260716",
                "title": "该文称每场景平均 15+ 可操作物体，借助 Physx-Omni 赋予密度/铰接/流形等属性并可导入仿真引擎",
                "tags": ["physx-omni", "interactive-objects", "simulation"],
                "domains": ["robotics", "simulation"],
                "confidence": "low",
                "applicability": ["物体级交互仿真训练", "足迹物体密度 4.16 宣传指标"],
                "uncertainty": "Physx-Omni 与 footprint density 4.16 为稿内自述；独立评测未 capture。",
                "evidence": [
                    quote_between(
                        "15 个可操作物体",
                        "4.16",
                        "物体密度指标",
                        "文内对可操作物体数量与足迹密度的说明。",
                    ),
                    quote_between(
                        "Physx-Omni",
                        "交互操作",
                        "Physx-Omni",
                        "文内对物理属性生成与仿真导入的说明。",
                    ),
                ],
            },
            "# 可交互物体\n\n15+ 物体/场景；Physx-Omni 物理属性。",
        ),
        (
            {
                "id": "claim_wechat_kairos_sim2real_training_20260716",
                "title": "该文称 Kairos-HomeWorld 已用于大晓机器人训练，支持跨房间导航与全屋整理等长程任务并缩短 sim-to-real 迁移周期",
                "tags": ["sim-to-real", "long-horizon", "household-robotics"],
                "domains": ["robotics", "embodied-ai"],
                "confidence": "low",
                "applicability": ["大晓机器人内部训练应用叙述", "全屋物品整理 demo 视频语境"],
                "uncertainty": "「大幅缩短」为宣传性表述；无定量迁移指标或第三方验证。",
                "evidence": [
                    quote_between(
                        "跨房间导航",
                        "迁移周期",
                        "训练应用",
                        "文内对长程任务训练与迁移周期的表述。",
                    ),
                    quote_between(
                        "全屋物品整理",
                        "全屋动线",
                        "长程任务 demo",
                        "文内对复杂指令拆解与全屋动线执行的说明。",
                    ),
                ],
            },
            "# Sim-to-real\n\n跨房间/全屋整理训练；迁移周期声称待量化。",
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
            "created_at": "2026-07-16T00:59:00+08:00",
            "updated_at": "2026-07-16T00:59:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入 Kairos-HomeWorld 宣传稿；等待人工核验",
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
            "厂商发布稿；规模/效果宣称需回 kairos-homeworld.github.io 与论文核验。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
