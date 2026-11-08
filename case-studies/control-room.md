# Control-Room
*Engineering case study · Historical implementation*

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

An agent could draft or propose an external action; the executor separately checked approval status, enabled adapter type and forbidden categories. The initial enabled notification adapter was narrowly scoped to the operator. Other outbound integrations were deliberately not assumed to be active.

## Another decision: avoid duplicate external actions

Before invoking an adapter, the executor used a PostgreSQL transaction and `SELECT ... FOR UPDATE` to claim an approved proposal and persist an `executing` state. Competing attempts could then observe the claim and back off.

**Trade-off:** this favors avoiding duplicate effects over automatic retries. A process crash after the claim, or after an external effect but before finalization, still requires reconciliation. It is not a universal exactly-once delivery guarantee.

## What the implementation does and does not show

The private source includes the planning engine, scoped-memory implementation, operator interface and gated executor. Historical operations records describe local and live health checks, tests and Telegram delivery. Those records support the existence of a working historical system; they are not evidence that every historical capability is deployed in the current RACAI runtime.

There is no claim here of independently verified paid-customer traction, general production readiness or novel model training.

## What I took forward

- Treat the model as a contributor to decisions, not the authority for consequential actions.
- Keep state and access boundaries outside the model's conversation.
- Define failure states and recovery behavior before broadening autonomy.
- Judge completion from evidence, not from an agent's self-report.

The later [RACAI Operator](./racai-operator.md) explores related problems on a different runtime.

---

*Internal code remains private. This case study describes selected engineering decisions without publishing credentials, customer records or proprietary configuration.*
