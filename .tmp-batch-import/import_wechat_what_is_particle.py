from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_9bcee8e0abc8386cbba43b87"
EXT = "extraction_2a34ca186d194f1ec87a6741"
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
        "reason": "中科院物理所转载 Natalie Wolchover / Quanta 2020《What Is a Particle?》；原刊未 capture",
    }
]


def build_candidates() -> list:
    return [
        (
            {
                "id": "claim_wechat_particle_point_paradox_20260716",
                "title": "该文称基本粒子常被视为无内部结构、无物理体积的点，但其电荷与质量等性质难以用零维点承载",
                "tags": ["particle-physics", "foundations", "conceptual"],
                "domains": ["physics", "philosophy-of-science"],
                "confidence": "medium",
                "applicability": ["粒子概念教学困境", "盖拉德/文小刚引述"],
                "uncertainty": "为 Quanta 科普综述转述；非实验结论。",
                "evidence": [
                    quote_between(
                        "缺乏内部结构",
                        "物理体积",
                        "无结构点粒子",
                        "文内对主流「点粒子」叙述。",
                    ),
                    quote_between(
                        "没有维度的点",
                        "承载重量",
                        "点与质量悖论",
                        "文内提出的经典困惑。",
                    ),
                ],
            },
            "# 点粒子悖论\n\n性质由数学形式决定；点状图像与质量/电荷并存难自洽。",
        ),
        (
            {
                "id": "claim_wechat_particle_collapsed_wavefunction_20260716",
                "title": "该文将粒子表述为观测后坍缩的波函数，并指出测量为何选出特定结果近一个世纪仍无共识答案",
                "tags": ["quantum-mechanics", "measurement-problem", "wavefunction"],
                "domains": ["physics", "quantum-mechanics"],
                "confidence": "medium",
                "applicability": ["波粒二象性科普", "测量问题开放状态"],
                "uncertainty": "为一种诠释性表述；测量问题有多派解释未展开。",
                "evidence": [
                    quote_between(
                        "粒子是坍缩后的波函数",
                        "但这究竟意味着什么呢",
                        "坍缩定义",
                        "文内对粒子=坍缩波函数的核心句。",
                    ),
                    quote_between(
                        "将近一个世纪",
                        "没有答案",
                        "测量未解",
                        "文内对测量问题状态的说明。",
                    ),
                ],
            },
            "# 坍缩波函数\n\n观测使波函数坍缩为探测器上的局域事件；为何如此仍开放。",
        ),
        (
            {
                "id": "claim_wechat_particle_field_quantum_20260716",
                "title": "该文引述量子场论：粒子是全空间量子场的离散量子激发，相互作用由场论精确计算",
                "tags": ["quantum-field-theory", "particle-physics"],
                "domains": ["physics"],
                "confidence": "medium",
                "applicability": ["QFT 标准语言", "光子/电子等场量子化"],
                "uncertainty": "概念性综述；未涉及 QFT 数学细节或引力耦合。",
                "evidence": [
                    quote_between(
                        "狄拉克",
                        "量子场的激发",
                        "场量子化",
                        "文内对狄拉克等人场论外推的叙述。",
                    ),
                    quote_between(
                        "扰动场的小份能量",
                        "粒子之间的相互作用",
                        "激发与相互作用",
                        "文内对粒子作为场激发的功能说明。",
                    ),
                ],
            },
            "# 场量子激发\n\n粒子是量子场的离散振荡；QFT 为粒子物理通用计算语言。",
        ),
        (
            {
                "id": "claim_wechat_particle_poincare_wigner_20260716",
                "title": "该文介绍维格纳观点：粒子是庞加莱群不可约表示，自旋标签区分不同基本粒子；标准模型可写为 SU(3)×SU(2)×U(1)",
                "tags": ["group-theory", "standard-model", "spin"],
                "domains": ["physics", "mathematics"],
                "confidence": "medium",
                "applicability": ["Wigner 1939 定义科普", "内部对称性「色」「味」"],
                "uncertainty": "格拉肖等强调表示≠粒子；群论与粒子等同有争议。",
                "evidence": [
                    quote_between(
                        "庞加莱群",
                        "不可约表示",
                        "Wigner 式定义",
                        "文内对群表示标准答案的叙述。",
                    ),
                    quote_between(
                        "SU(3)",
                        "SU(3)×SU(2)×U(1)",
                        "标准模型对称群",
                        "文内对标准模型群结构的说明。",
                    ),
                ],
            },
            "# 群表示\n\n时空庞加莱表示 + 内部 SU(3)×SU(2)×U(1)；自旋决定物质/力行为。",
        ),
        (
            {
                "id": "claim_wechat_particle_modern_qubit_amplitude_20260716",
                "title": "该文对比两种当代图景：it-from-qubit 全息编码下粒子由纠缠量子比特涌现；振幅学家则用 amplituhedron 等几何对象直接编码散射振幅",
                "tags": ["quantum-gravity", "holography", "amplituhedron"],
                "domains": ["physics", "quantum-information"],
                "confidence": "medium",
                "applicability": ["it-from-qubit 与全息时空", "振幅学对 QFT「方便虚构物」批评"],
                "uncertainty": "两路线是否互补或矛盾文内称未定论；均为前沿研究非成熟理论。",
                "evidence": [
                    quote_between(
                        "it-from-qubit",
                        "量子比特",
                        "it-from-qubit",
                        "文内对量子比特涌现时空/粒子的介绍。",
                    ),
                    quote_between(
                        "amplituhedron",
                        "柏拉图",
                        "振幅几何",
                        "文内对 amplituhedron 与振幅学方法的说明。",
                    ),
                ],
            },
            "# 当代双图景\n\n全息量子比特 vs 振幅几何；恩格尔哈特：「我们不知道」仍是简短回答。",
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
            "created_at": "2026-07-16T10:48:00+08:00",
            "updated_at": "2026-07-16T10:48:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入「何谓粒子」科普；等待人工核验",
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
            "Quanta/Wolchover 2020 综述转述；前沿理论部分为开放研究非定论。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
