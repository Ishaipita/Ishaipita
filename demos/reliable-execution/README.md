# Reliable Execution — bounded SQLite state machine

**A standalone Python demonstration, not RACAI production code.** This exercise illustrates a failure mode that matters in distributed workflows: a remote action may succeed even when the worker never receives confirmation.

## Run

From this directory:

```bash
python3 -m unittest discover -s tests -v
```

Python 3.10+; standard library only.

## What is demonstrated

- Duplicate job IDs are ignored without resetting state.
- SQLite `BEGIN IMMEDIATE` and a conditional update allow only one claimant for a pending job.
- Jobs have explicit `pending → claimed → verified/unknown` transitions.
- Uncertain outcomes are not automatically retried.
- SQLite persists state across reopened connections.

## What is **not** demonstrated

No remote provider, receipt authentication, exactly-once delivery, distributed lease recovery, network fault injection, deployment or production-grade security. A caller can supply a fabricated receipt: `verified` is a **local state label**, not external proof.

## Design trade-off

Leaving an uncertain action in `unknown` is conservative: it avoids accidental repeat side effects, but requires an operator or a provider reconciliation API to recover.

## Context

This is a recent, narrow, reproducible demonstration connected to the engineering themes of [Control-Room](../../case-studies/control-room.md) and [RACAI Operator](../../case-studies/racai-operator.md). It is **not** represented as the multi-year work itself.
