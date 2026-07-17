# ADR 0034: Memory lifecycle tiers

- Status: accepted
- Date: 2026-07-17

## Decision

Use `raw -> derived -> working -> trusted -> canonical`, with `superseded` and `archived` as historical outcomes. Raw is immutable evidence, derived is rebuildable, Working is usable but revisable, Trusted passed policy-backed consolidation, and Canonical is explicitly confirmed by the user.

Stable object IDs survive tier changes. Working and Trusted live in `vault/memory/`; Canonical retains the existing knowledge/frontier/action directories.
