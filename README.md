<div align="center">

<img src="./assets/systems-banner.svg" width="100%" alt="Ishai Pita — Systems That Finish The Work. Architectural network graphic." />

### ISHAI CHERTKOFF
**Founder · Systems Architect · Product Engineer**

Building [RACAI](https://rac-ai.com/) — intelligent software, operating systems and creative technology.

</div>

---

## 01 / FOCUS

I design and build software systems across AI, backend infrastructure and product engineering. My work has moved from experimental agent coordination to a more difficult engineering question: how do you keep actions controlled, state consistent and outcomes verifiable when software operates across models, tools and external services?

RACAI is where I develop and apply that work.

## 02 / SELECTED ENGINEERING WORK

### RACAI Operator
**Cloudflare Workers · D1 · TypeScript · Telegram / web interfaces**

An evolving internal operating system for work intake, persistent business state and controlled execution. The implementation includes proposal/confirmation flows, approval boundaries, audit records, scheduled processes and deployment safeguards.

**Engineering focus:** state transitions, access control, recovery and operational evidence.

### Control-Room
**Node.js · PostgreSQL · Redis · AI orchestration**

A historical multi-tenant implementation for coordinating AI-assisted work. Built around a bounded plan–act–verify loop, scoped memory, sequential queues and separately authorized external actions.

The executor distinguishes an agent's proposal from permission to act. Approved actions are checked against an allowlist and claimed transactionally before execution. This prevents competing workers from intentionally executing the same proposal twice, but does not by itself establish exactly-once delivery to external services.

[Read the Control-Room engineering case study →](./case-studies/control-room.md)

### B-Sure
**Applied AI · Financial analysis · Human review**

A proof of concept for a five-stage credit-analysis workflow: extract, analyze, enrich, score and formulate follow-up questions. The interface exposes reasoning and score factors for human review rather than treating model output as a final lending decision.

### NYRA
**Generative media · Python · Asset provenance · Cost controls**

A reproducible visual production workflow using a canonical reference asset, versioned manifests, spend tracking and preflight checks. Iterative failures informed additional prompt constraints and safeguards.

## 03 / ENGINEERING DECISIONS

| Problem | Approach | Boundary |
|:--|:--|:--|
| Model output is not authorization | Separate planning and proposals from an approval-gated executor | A human still owns consequential decisions |
| Agent context is not durable state | Persist structured state, scoped memory and audit events | Storage integrity is not proof of real-world success |
| Retries can repeat external effects | Atomic claims, bounded attempts and explicit failure states | External exactly-once delivery requires provider-level guarantees |
| A release can appear successful without being live | Distinguish code, tests, deployment evidence and observed behavior | Production and commercial outcomes require separate verification |

## 04 / OTHER EXPLORATIONS

**Jarvis** — earlier experiments in specialist-agent coordination and financial research tooling. Historical work, not a live trading service.

**Theta–Erdős research** — symbolic and numerical exploration with explicit evidence classifications and independent verification procedures.

These projects span different stages of development. The linked case study documents a historical implementation; current RACAI capabilities are not presented as equivalent to every historical prototype.

## 05 / WORKING STACK

`TypeScript` · `JavaScript` · `Python` · `Node.js` · `PostgreSQL` · `Redis` · `Cloudflare Workers` · `D1` · `AWS` · `GitHub Actions` · `REST APIs` · `AI systems`

---

<div align="center">

**RACAI — Ambition, made real.**

[Company](https://rac-ai.com/) · [Engineering portfolio](./case-studies/control-room.md) · [GitHub](https://github.com/Ishaipita)

</div>
