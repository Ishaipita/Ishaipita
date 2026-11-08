# Control-Room
*Engineering case study · Agent execution and governance*

**Stack:** Node.js / Express, PostgreSQL, Redis, Python, AI model tooling  
**Scope:** Multi-tenant task processing and operator-controlled agent execution

[← Portfolio](../README.md)

## The problem

An AI agent can propose an action, but that does not mean it should be allowed to perform it. The system needed to coordinate tasks for different clients while keeping data boundaries, resource consumption and external actions under explicit control.

## What I built

Control-Room combined two execution paths:

| Path | Execution | Boundary |
|---|---|---|
| Client work | Scoped request → sequential queue → specialist processing → review | Client-specific records and usage limits |
| Operator work | Goal → plan → read-only tools → synthesis → verification | Any external action becomes a proposal requiring separate approval |

The engine used a bounded planning loop, a restricted tool menu and a verification stage. It recorded tool evidence and distinguished results that passed verification from results that required attention. Memory was persisted by scope rather than relying on unfiltered conversation history.

## A specific engineering decision: authority is separate from reasoning

```text
GOAL
  ↓
PLAN → BOUNDED TOOL CALLS → VERIFY
                         ↙       ↘
                    DELIVERABLE   ACTION PROPOSAL
                                       ↓
                                 HUMAN APPROVAL
                                       ↓
                                ALLOWLISTED EXECUTOR
                                       ↓
                                  AUDIT RECORD
```

An agent could draft or propose an external action; the executor separately checked approval status, enabled adapter type and forbidden categories. The notification adapter used an operator-scoped delivery path.

## Another decision: avoid duplicate external actions

Before invoking an adapter, the executor used a PostgreSQL transaction and `SELECT ... FOR UPDATE` to claim an approved proposal and persist an `executing` state. Competing attempts could then observe the claim and back off.

This design favors explicit state tracking and controlled retries. External delivery guarantees depend on the connected provider and its idempotency semantics.

## Implementation evidence

The source includes a planning engine, scoped-memory implementation, operator interface and gated executor. Engineering records cover health checks, tests and delivery verification from the development period. The project informed subsequent work on Cloudflare Workers and D1.

## What I took forward

- Treat the model as a contributor to decisions, not the authority for consequential actions.
- Keep state and access boundaries outside the model's conversation.
- Define failure states and recovery behavior before broadening autonomy.
- Use recorded outcomes and verification evidence to review execution.

The [RACAI Operator](./racai-operator.md) project extends this line of work using Cloudflare Workers and D1.

---

*Internal source and operational configuration remain private.*
