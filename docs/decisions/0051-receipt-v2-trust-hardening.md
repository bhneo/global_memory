# ADR 0051: Receipt v2 trust hardening

- Status: accepted

Trusted promotion now requires a Receipt v2 whose object hash and consolidation fingerprint still match. The fingerprint covers object, sources/raw state, evidence, extraction/work identity, relations, contradictions, schema and policy versions. Receipt v1 files remain immutable audit history but cannot qualify a new Trusted promotion.

Weekly drift uses the typed `drift_type` field. High drift becomes an exception rather than a crash. Failed consolidation is observational: it must not update a governed object. Contradictions require explicit source-linked contrary evidence.
