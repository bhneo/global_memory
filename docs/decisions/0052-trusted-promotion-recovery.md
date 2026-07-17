# ADR 0052: Recoverable Trusted promotion

- Status: accepted

Trusted promotion is a staged local transaction. A recovery journal records the original Working bytes before the staged Trusted write. Receipt v2 completion checkpoints the journal; normal completion removes it. If the process stops before receipt completion, `gm recover` restores the exact Working bytes. If receipt completion was already checkpointed, recovery only removes the stale journal.

The doctor command treats pending Trusted-promotion journals as an integrity issue. This path has no Canonical write authority.
