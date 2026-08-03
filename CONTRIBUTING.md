# Contributing

Keep changes small, tested, and compatible with the truth-layer boundary:
Raw is immutable, derived state is rebuildable, Reflection/Synthesis are
non-factual, and Canonical promotion remains human-only. Do not submit a real
Vault, raw research material, tokens, browser data, logs, recovery journals,
or generated indexes.

Run `python -m pytest`, `galois doctor`, `galois lint`, and `galois raw verify`
before proposing a change. Public release candidates must also pass the release
builder and boundary audit. Contributions are accepted under Apache-2.0.
