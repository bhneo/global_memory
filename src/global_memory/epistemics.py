from __future__ import annotations

from pathlib import Path
from typing import Any


MEMORY_TIERS = {"working", "trusted", "canonical", "historical"}
EPISTEMIC_STATUSES = {
    "established", "supported", "provisional", "contested", "hypothetical",
    "open_question", "partially_answered", "exploratory_analogy",
    "observed_anomaly", "user_intuition", "superseded", "unknown",
}


def default_epistemic_status(object_type: str, tier: str = "working") -> str:
    """Return a conservative type-aware status without inventing certainty."""
    if object_type == "question":
        return "open_question"
    if object_type == "hypothesis":
        return "hypothetical"
    if object_type == "analogy":
        return "exploratory_analogy"
    if object_type == "anomaly":
        return "observed_anomaly"
    if object_type == "intuition":
        return "user_intuition"
    if object_type == "claim" and tier == "trusted":
        return "supported"
    return "unknown"


def infer_tier(metadata: dict[str, Any], path: Path | None = None) -> str:
    explicit = str(metadata.get("memory_tier", ""))
    if explicit in MEMORY_TIERS:
        return explicit
    status = str(metadata.get("status", ""))
    if status in MEMORY_TIERS:
        return status
    path_text = path.as_posix() if path else ""
    if "/archive/" in f"/{path_text}":
        return "historical"
    if any(f"/vault/{root}/" in f"/{path_text}" for root in ("knowledge", "frontier", "action")):
        return "canonical"
    if status in {"confirmed"}:
        return "canonical"
    if status in {"archived", "superseded"}:
        return "historical"
    # Unknown legacy states are deliberately downgraded, never promoted.
    return "working"


def infer_epistemic_status(metadata: dict[str, Any], tier: str | None = None) -> str:
    explicit = str(metadata.get("epistemic_status", ""))
    if explicit in EPISTEMIC_STATUSES:
        return explicit
    legacy = str(metadata.get("status", ""))
    direct = {
        "confirmed": "established",
        "provisional": "provisional",
        "contested": "contested",
        "superseded": "superseded",
        "archived": "superseded",
    }
    if legacy in direct:
        return direct[legacy]
    resolved_tier = tier or infer_tier(metadata)
    return default_epistemic_status(str(metadata.get("type", "")), resolved_tier)


def normalized_dimensions(metadata: dict[str, Any], path: Path | None = None) -> tuple[str, str]:
    tier = infer_tier(metadata, path)
    return tier, infer_epistemic_status(metadata, tier)


def truth_layer(metadata: dict[str, Any], path: Path | None = None) -> str:
    object_type = str(metadata.get("type", ""))
    if object_type == "source":
        return "source_capture"
    if object_type == "proposal":
        return "proposal"
    explicit = str(metadata.get("memory_tier", ""))
    legacy = str(metadata.get("status", ""))
    recognized_legacy = MEMORY_TIERS | {"confirmed", "provisional", "contested", "archived", "superseded"}
    path_text = path.as_posix() if path else ""
    if explicit not in MEMORY_TIERS and legacy not in recognized_legacy and not any(
        f"/vault/{root}/" in f"/{path_text}" for root in ("knowledge", "frontier", "action", "archive")
    ):
        return "unknown"
    tier, _ = normalized_dimensions(metadata, path)
    return tier if tier in MEMORY_TIERS else "unknown"
