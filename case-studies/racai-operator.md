# RACAI Operator
*Selected engineering notes · Internal platform*

**Stack:** TypeScript, Cloudflare Workers, D1, web and Telegram interfaces  
**Focus:** Persistent work state, approvals and operational evidence

[← Portfolio](../README.md)

## Context

RACAI Operator focuses on preserving work context across sessions, separating proposals from authorized decisions, and recording execution evidence in structured state.

The project explores ways to make work traceable through state transitions rather than relying solely on a conversation.

## Implementation

The private codebase includes a Cloudflare-based runtime with D1-backed records, founder-facing task and proposal flows, approval and rejection handling, scheduled processes, audit records and guarded release procedures.

The operating flow separates decisions and state changes:

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



## Decisions worth examining

**State outside the chat.** Work and operational records belong in persistent storage so that the same task can be inspected and continued across interfaces.

**Authority before action.** External or consequential changes are separated from drafts and proposals; the authorization boundary is part of application behavior, not merely prompt wording.

**Evidence-driven reviews.** Tests, commits, deployed versions and operational records provide distinct views of engineering progress.

**Operational continuity.** Duplicate requests, retries, job state and rollback are addressed explicitly within the execution lifecycle.

## Engineering context

RACAI Operator is an internal engineering platform developed through successive iterations. The [Control-Room case study](./control-room.md) provides context on an earlier approach to controlled agent execution.

---

*Internal source and operational configuration are private.*
