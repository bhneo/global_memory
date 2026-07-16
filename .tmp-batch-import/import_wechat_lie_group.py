from pathlib import Path

from global_memory.extraction import ExtractionService
from global_memory.markdown import render_document
from global_memory.proposals import ProposalService
from global_memory.repository import Repository

repo = Repository(Path("."))
SRC = "source_941321d95232028c233c9433"
EXT = "extraction_c4f0793e6fac8c18c8ed3a6f"
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
        "reason": "由中科院物理所转载的李群李代数科普文章归纳；非教材定理证明",
    }
]


def build_candidates() -> list:
    return [
    (
        {
            "id": "claim_wechat_lie_group_continuous_symmetry_20260715",
            "title": "该文称李群用于描述可连续变化的对称性，并可定量处理洛伦兹变换与自旋概念",
            "tags": ["lie-group", "symmetry", "lorentz"],
            "domains": ["mathematics", "physics"],
            "confidence": "medium",
            "applicability": ["现代物理对称性/群论入门语境", "洛伦兹对称性与表示论讨论"],
            "uncertainty": "为科普性概念介绍，未给出严格定理证明；自旋导出路径被压缩叙述。",
            "evidence": [
                quote_between(
                    "物理上经常会遇到一些能连续变化的对称性",
                    "我们就要借助李群。",
                    "连续对称",
                    "文内对引入李群动机的说明。",
                ),
                quote_between(
                    "比如洛伦兹对称性就是这样一种对称性",
                    "甚至由此导出自旋的概念。",
                    "洛伦兹与自旋",
                    "文内对李群在相对论与自旋中作用的表述。",
                ),
            ],
        },
        "# 李群与连续对称\n\n描述连续对称；洛伦兹变换与自旋。",
    ),
    (
        {
            "id": "claim_wechat_particle_as_representation_basis_20260715",
            "title": "该文称现代粒子物理中的「粒子」可理解为李群不可约表示空间的基",
            "tags": ["particle-physics", "representation-theory", "lie-group"],
            "domains": ["physics", "mathematics"],
            "confidence": "medium",
            "applicability": ["粒子物理概念层解释", "理论赋予实验数据意义的讨论"],
            "uncertainty": "为概念性重定义/interpretation，不是实验操作定义；依赖表示论框架。",
            "evidence": [
                quote_between(
                    "理论告诉我们实验能看到什么",
                    "赋予实验数据意义。",
                    "理论角色",
                    "文内对理论解释实验数据的说明。",
                ),
                quote_between(
                    "李群的不可约表示空间的基",
                    "这样一个东西。",
                    "粒子定义",
                    "文内对「粒子」概念的核心表述。",
                ),
            ],
        },
        "# 粒子即表示基\n\n粒子 = 不可约表示空间基。",
    ),
    (
        {
            "id": "claim_wechat_sm_gauge_lie_group_20260715",
            "title": "该文称标准模型是规范理论，其规范群为李群",
            "tags": ["standard-model", "gauge-theory", "lie-group"],
            "domains": ["physics", "particle-physics"],
            "confidence": "medium",
            "applicability": ["标准模型结构的高层科普描述", "规范对称性语境"],
            "uncertainty": "未指明具体规范群因子（如 SU(3)×SU(2)×U(1)）；为概述性断言。",
            "evidence": [
                quote_between(
                    "目前人类最准确的物理理论——标准模型",
                    "规范群就是一个李群。",
                    "标准模型规范群",
                    "文内对标准模型与李群关系的陈述。",
                ),
            ],
        },
        "# 标准模型规范群\n\n规范理论；规范群为李群。",
    ),
    (
        {
            "id": "claim_wechat_lie_group_definition_20260715",
            "title": "该文定义李群为同时满足群公理、微分流形结构与运算相容性的集合",
            "tags": ["lie-group", "differential-geometry", "manifold"],
            "domains": ["mathematics"],
            "confidence": "medium",
            "applicability": ["文内第二节李群定义", "圆的对称 vs 离散群对比语境"],
            "uncertainty": "提取文本中公式符号有 HTML 丢失；相容性条件未完整呈现数学细节。",
            "evidence": [
                quote_between(
                    "当我们说到圆的变换时，我们可以谈圆转了一个无穷小的角度",
                    "这两者结合就引出了李群的概念。",
                    "连续 vs 离散",
                    "文内说明圆对称需要拓扑/微分结构。",
                ),
                quote_between(
                    "定义一个李群为一个集合，满足",
                    "李群同时具有群结构和微分结构",
                    "李群定义",
                    "文内对李群三重条件的概述。",
                ),
            ],
        },
        "# 李群定义\n\n群 + 微分流形 + 相容运算。",
    ),
    (
        {
            "id": "claim_wechat_lie_algebra_exponential_map_20260715",
            "title": "该文称李代数刻画李群局部结构，指数映射仅对紧致连通李群为满射",
            "tags": ["lie-algebra", "exponential-map", "lie-group"],
            "domains": ["mathematics", "physics"],
            "confidence": "medium",
            "applicability": ["文内第三节李代数构造与指数映射", "局部-整体关系讨论"],
            "uncertainty": "不同李群可共享同一李代数为文内断言，未给出反例；证明被省略。",
            "evidence": [
                quote_between(
                    "李代数可以在局部转变为李群元素",
                    "结果是一个指数映射",
                    "指数映射",
                    "文内对李代数局部生成群元的描述。",
                ),
                quote_between(
                    "只有紧致连通李群指数映射才是满射",
                    "才是满射。",
                    "满射条件",
                    "文内对指数映射覆盖范围的限制。",
                ),
                quote_between(
                    "李代数只能反映李群的局部性质",
                    "对李群的研究也不能仅借助李代数。",
                    "局部局限",
                    "文内对李代数无法捕获整体性质的说明。",
                ),
            ],
        },
        "# 李代数与指数映射\n\n局部线性化；紧致连通时 exp 满射。",
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
            "created_at": "2026-07-15T21:00:00+08:00",
            "updated_at": "2026-07-15T21:00:00+08:00",
            "aliases": [],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "批量导入李群李代数科普；等待人工核验",
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
            "数学/粒子物理科普；公式符号在 extraction 中有损；非严格证明。",
            f"导入 {meta['id']}",
            prompt if prompt.is_file() else None,
        )
        print(result.proposal_id, meta["id"])


if __name__ == "__main__":
    main()
