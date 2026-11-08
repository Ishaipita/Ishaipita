<div align="center">

<img src="./assets/systems-banner.svg" width="100%" alt="Systems That Finish The Work — Ishai Chertkoff engineering portfolio." />

### ISHAI CHERTKOFF
**Independent software builder · AI systems & product engineering**

[Selected work](#selected-work) &nbsp;·&nbsp; [RACAI](https://rac-ai.com/)

</div>

---

I build software at the intersection of AI, backend systems and products. Much of my work has focused on a practical question: **what does it take for software to carry work through to a result that can be checked?**

That has meant building, revising and sometimes replacing systems for agent coordination, persistent state, permissions, external tools and operational review. RACAI is my continuing work in this area.

## Selected work

### [RACAI Operator](./case-studies/racai-operator.md)
**Internal operating software · TypeScript, Cloudflare Workers, D1**

Work intake, persistent state, approval flows, audit records and scheduled operations. The project has evolved through several deployments and release iterations.

[Architecture and implementation notes →](./case-studies/racai-operator.md)

### [Control-Room](./case-studies/control-room.md)
**Agent execution and governance · Node.js, PostgreSQL, Redis**

A historical multi-tenant system that explored a bounded plan–act–verify process, scoped memory and a separate approval-gated executor for external actions.

[Engineering case study →](./case-studies/control-room.md)

### B-Sure
**Applied AI prototype · Node.js, SSE**

A five-stage workflow for reviewing SME credit applications: document extraction, financial analysis, external research, scoring and follow-up questions. Built as a proof of concept with explainable outputs and human review.

### NYRA
**Generative media tooling · Python**

A reference-based production workflow with versioned assets, spending controls and reproducible preflight checks. Iterations were informed by recorded generation failures and image-consistency tests.

<details>
<summary>Earlier work and research</summary>

**Jarvis** — experiments in multi-agent coordination and financial research tooling.

**Theta–Erdős** — symbolic and numerical exploration using independent verification and explicit confidence classifications.

These are exploratory or historical projects, not additional production products.

</details>

## Engineering approach

I favor small, testable execution paths over broad automation claims. A model can suggest an action; the software still needs to establish authority, record what happened and handle failure. A successful test is different from a successful deployment, and neither automatically demonstrates a useful outcome.

The case studies show selected implementation decisions and their limitations. Source repositories for internal systems remain private.

## Technologies

TypeScript · JavaScript · Python · Node.js · Cloudflare Workers · D1 · PostgreSQL · Redis · AWS · GitHub Actions · REST APIs

---

<div align="center">

[RACAI](https://rac-ai.com/) &nbsp;·&nbsp; [Control-Room case study](./case-studies/control-room.md) &nbsp;·&nbsp; [GitHub profile](https://github.com/Ishaipita)

</div>
