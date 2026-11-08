# RACAI Operator
*Selected engineering notes · Evolving internal platform*

**Stack:** TypeScript, Cloudflare Workers, D1, web and Telegram interfaces  
**Focus:** Persistent work state, approvals and operational evidence

[← Portfolio](../README.md)

## Context

RACAI Operator grew from a recurring problem in AI-assisted work: context can be lost between sessions, a proposed change can be confused with an authorized one, and an execution report can be mistaken for evidence of an outcome.

The project explores ways to make work traceable through state transitions rather than relying solely on a conversation.

## Implementation

The private codebase includes a Cloudflare-based runtime with D1-backed records, founder-facing task and proposal flows, approval and rejection handling, scheduled processes, audit records and guarded release procedures.

The central approach is deliberately narrower than an unrestricted autonomous agent:

```text
WORK REQUEST
    ↓
STRUCTURED PROPOSAL
    ↓
OWNER DECISION ──→ REJECT / REVISE
    ↓
AUTHORIZED STATE CHANGE
    ↓
AUDIT / EVIDENCE RECORD
    ↓
FOLLOW-UP OR REVIEW
```

The platform also contains distinct operational and commercial experiments. Their presence in the repository does not mean every integration is deployed or producing revenue.

## Decisions worth examining

**State outside the chat.** Work and operational records belong in persistent storage so that the same task can be inspected and continued across interfaces.

**Authority before action.** External or consequential changes are separated from drafts and proposals; the authorization boundary is part of application behavior, not merely prompt wording.

**Evidence has levels.** Tests, commits, deployed versions, provider receipts and actual outcomes answer different questions. A passing test cannot establish customer value or confirm that a deployment is active.

**Recovery is part of the design.** Duplicate requests, retries, stalled work and rollback require explicit treatment. A system that only reports successful paths is difficult to operate.

## Current boundary

This is ongoing internal engineering, not a publicly available autonomous-company product. The existing runtime has working components and documented tests, while integration gaps, limited authorized executors and incomplete end-to-end operational value remain areas of development.

The historical [Control-Room](./control-room.md) describes an earlier, separate approach. Its capabilities should not be assumed to be present in the current runtime.

---

*Detailed operational configuration, internal repositories and customer information remain private.*
