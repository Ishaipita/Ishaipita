# CONTROL-ROOM
## Engineering case study — governed AI execution

**Discipline:** Multi-tenant systems · agent orchestration · operational safeguards  
**Maturity:** Historical working implementation, subsequently undergoing modernization. Not presented as a currently available public SaaS.

> **The problem:** How can an operator coordinate AI specialists while keeping customer boundaries, cost controls, and irreversible actions under human control?

### Two separate execution planes

| Plane | Core flow | Safety boundary |
|:--|:--|:--|
| Client portal | Scoped user → task queue → sequential worker → agent → review | Tenant-specific access and task budget checks |
| Operator | Goal → plan → bounded tools → verify → propose | External actions require separate human approval |

The platform's documented architecture combines:

- **Scoped memory:** persistent context keyed to operator/client scope, not a shared unfiltered chat history.
- **Usage governance:** per-agent token budgets, circuit breakers, call-level audit records.
- **Task orchestration:** sequential job execution and distinct operator workflows.
- **Approval-gated execution:** allowlisted adapters, atomic claims and no blind retry of failed external actions.
- **Operational observability:** deterministic Python agents for infrastructure, code-quality, registry status and morning digests.
- **Multi-tenant separation:** client portal identity and storage boundaries.

### Execution boundary

```text
OWNER GOAL
    |
    v
PLAN → READ-ONLY ACTIONS → VERIFY
                         |
            +------------+-----------+
            |                        |
        DELIVERABLE            EXTERNAL ACTION
        + MEMORY                 PROPOSAL
                                     |
                                     v
                              OWNER APPROVAL
                                     |
                                     v
                              GATED EXECUTOR
                                     |
                                     v
                               AUDIT RECORD
```

**Key decision:** An LLM can propose an external change; it cannot approve its own proposal. The executor applies a separate allowlist and state transition.

### Evidence and constraints

Historical source and operations notes describe a Node.js / Express / PostgreSQL / Redis platform hosted on AWS, alongside Python health and maintenance tools. The July 2026 operations journal records local and live health checks, unit tests and Telegram delivery evidence.

These records demonstrate historical implementation and testing, **not** current production availability. Later infrastructure moved toward Cloudflare Workers and D1, with ongoing reconciliation of historic capabilities. No public paid-user traction is claimed here.

### Lessons that carry into RACAI

1. Separate model reasoning from permission to act.
2. Preserve source provenance and verifiable state transitions.
3. Require tenant isolation and bounded resource usage.
4. Treat code, tests, release, and customer acceptance as distinct evidence levels.
5. Build operational continuity before claiming autonomous operations.

### References

- [Current RACAI company site](https://rac-ai.com/)
- [Founder profile](https://github.com/Ishaipita)
- Original internal engineering repository remains private. Public details above are intentionally limited to architecture and previously documented design decisions.

---

**Ishai Pita** / Founder & Systems Architect · RACAI
