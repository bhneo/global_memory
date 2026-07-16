from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_6ada1b3b0033883b83a3bf40"
EXT = "extraction_4d37e41c1600afe16e196923"
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
        "reason": "量子位授权转载 openJiuwen Jiuwen Symbiosis 开源宣传；属 vendor/社区软文",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_jiuwen_moravec_embodiment_gap_20260716",
                "title": "该文引述 Moravec 悖论：逻辑/数学对计算机易，行走抓取等身体智能难；称当前大模型「缸中之脑」缺乏物理世界感知",
                "tags": ["Moravec-paradox", "embodied-ai", "physical-ai"],
                "domains": ["robotics", "artificial-intelligence"],
                "confidence": "medium",
                "applicability": ["physical AI 动机论述", "1988 Moravec 引述"],
                "uncertainty": "悖论表述为科普常见转述；「最大局限之一」为作者观点。",
                "evidence": [
                    quote_between(
                        "Moravec",
                        "莫拉维克悖论",
                        "Moravec 引入",
                        "文内对 Moravec 悖论名称与提出者的说明。",
                    ),
                    quote_between(
                        "缸中之脑",
                        "空间几何一无所知",
                        " embodiment 缺口",
                        "文内对大模型缺乏物理实体知识的比喻。",
                    ),
                ],
            },
            "# Moravec / 缸中之脑\n\nAgent 可操作数字世界但难触达物理世界。",
        ),
        (
            {
                "id": "claim_wechat_jiuwen_vla_limitations_critique_20260716",
                "title": "该文批评当前 VLA「2.0」阶段：缺组合泛化、长程任务分解与异常回退、端到端黑盒难定位故障、成功率与稳定性不足",
                "tags": ["VLA", "compositional-generalization", "long-horizon"],
                "domains": ["robotics", "machine-learning"],
                "confidence": "low",
                "applicability": ["Sim2Real 2.0 问题清单", "开抽屉+抓取零样本组合举例"],
                "uncertainty": "为 openJiuwen 产品叙事中的竞品/现状批评；未给出独立实验对照。",
                "evidence": [
                    quote_between(
                        "组合泛化",
                        "零样本组合",
                        "组合泛化不足",
                        "文内对 VLA 无法组合已学技能的批评。",
                    ),
                    quote_between(
                        "长程复合任务",
                        "无法在运行时",
                        "规划能力不足",
                        "文内对长程任务需重训、缺运行时规划的说明。",
                    ),
                ],
            },
            "# VLA 2.0 批评\n\n视觉→语言→物理→动作压入单一 Transformer 致故障难归因。",
        ),
        (
            {
                "id": "claim_wechat_jiuwen_situation_awareness_loop_20260716",
                "title": "该文称 Jiuwen Symbiosis 以「态势感知环」显式暴露 Agent 内部状态：认知层与执行层经共享 Workspace 协作，强调可观察、可调试",
                "tags": ["agent-architecture", "situation-awareness", "workspace"],
                "domains": ["robotics", "agent-systems"],
                "confidence": "low",
                "applicability": ["3.0 共生架构 vs 2.0 VLA", "JSON 堆积/debug 困难动机"],
                "uncertainty": "架构描述来自官方宣传；实现细节与评测未给出。",
                "evidence": [
                    quote_between(
                        "可观察、可调试",
                        "可协作",
                        "透明设计目标",
                        "文内对 Symbiosis 设计理念的核心句。",
                    ),
                    quote_between(
                        "态势感知环",
                        "Situation Awareness Loop",
                        "SA 环",
                        "文内对核心骨架命名。",
                    ),
                ],
            },
            "# 态势感知环\n\n感知-规划-执行-观测-反馈闭环；分离理解与生成分层。",
        ),
        (
            {
                "id": "claim_wechat_jiuwen_modules_spatial_memory_20260716",
                "title": "该文列举 Symbiosis 模块：多模态感知产出结构化世界状态；安全规划校检物理可行性；空间记忆以 3D Scene Graph 维护物体关系",
                "tags": ["safe-planning", "spatial-memory", "skill-tool"],
                "domains": ["robotics", "agent-systems"],
                "confidence": "low",
                "applicability": ["Skill/Action Tool 原子能力", "Feedback 闭环修正"],
                "uncertainty": "模块能力为设计声明；零样本跨本体等效益未附量化证据。",
                "evidence": [
                    quote_between(
                        "安全规划",
                        "Safe Planning",
                        "安全规划模块",
                        "文内对 Safe Planning 模块标题。",
                    ),
                    quote_between(
                        "空间记忆",
                        "Spatial Memory",
                        "空间记忆模块",
                        "文内对 Spatial Memory 模块标题。",
                    ),
                    quote_between(
                        "3D Scene Graph",
                        "空间关系",
                        "场景图",
                        "文内对 3D Scene Graph 物体级空间关系说明。",
                    ),
                ],
            },
            "# 功能模块\n\nAction 前场景理解结构化；观测反馈支撑参数调整与异常恢复。",
        ),
        (
            {
                "id": "claim_wechat_jiuwen_edge_cloud_ascend_20260716",
                "title": "该文称 Symbiosis 采用端云协同：云侧 LLM/VLM 负责复杂规划，端侧实时感知执行；并宣称与昇腾 NPU、鲲鹏 CPU 异构分工以降功耗",
                "tags": ["edge-cloud", "Ascend", "open-source"],
                "domains": ["robotics", "systems"],
                "confidence": "low",
                "applicability": ["gitcode.com/openJiuwen/jiuwensymbiosis 开源", "华为云 AgentArts 商业化"],
                "uncertainty": "典型 vendor 生态宣传；TOPS/功耗/吞吐提升缺乏第三方验证。",
                "evidence": [
                    quote_between(
                        "端云协同",
                        "云侧LLM/VLM",
                        "端云架构",
                        "文内对端云分工的描述。",
                    ),
                    quote_between(
                        "昇腾",
                        "鲲鹏CPU",
                        "异构分工",
                        "文内对昇腾/鲲鹏资源分工的说明。",
                    ),
                ],
            },
            "# 端云 + 昇腾\n\n2026-06 开源 Symbiosis；教 How 非 What 的共生叙事。",
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
            "created_at": "2026-07-16T11:10:00+08:00",
            "updated_at": "2026-07-16T11:10:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入 Jiuwen Symbiosis 宣传文；等待人工核验",
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
            "量子位/openJiuwen 软文；产品能力与 benchmark 需独立验证，confidence 偏低。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
