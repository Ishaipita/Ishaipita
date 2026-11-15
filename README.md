# Ishai Chertkoff
**Infrastructure & automation engineering · Linux · Python · Cloud · backend systems**

I build software that makes complex work **observable, recoverable and verifiable**. My independent engineering projects span Linux application operations, cloud services, backend integration, durable workflow state and approval-gated AI tools.

**Open to early-career roles:** Infrastructure Engineering · Systems Integration · Cloud Operations · Backend Automation. I value hands-on debugging, technical mentorship and evidence-based engineering.

[Engineering case studies](#selected-engineering-work) · [RACAI](https://rac-ai.com/) · [LinkedIn](https://www.linkedin.com/in/ishai-chertkoff-b252183b3/)

## Selected engineering work

### [RACAI Operator — durable work and authorization](./case-studies/racai-operator.md)
**TypeScript · Cloudflare Workers · D1 · Telegram / web interfaces**

**Challenge:** Work initiated through chat needs persistent state, explicit approval and an audit trail rather than an unverified “done” message.

**Engineering approach:** Structured task and proposal records, owner approval/rejection boundaries, scheduled execution and operational evidence. Tests, merge status and live deployment are treated as separate claims.

**Status:** Internal platform; code and operational state remain private. The linked case study documents design, not independently verified uptime or commercial adoption.

### [Control-Room — controlled agent execution](./case-studies/control-room.md)
**Node.js · Express · PostgreSQL · Redis**

**Challenge:** Multi-tenant workflows require scoped data, bounded tool access and protection against concurrent duplicate action attempts.

**Engineering decision:** Separate an agent's proposal from an allowlisted executor. A PostgreSQL transaction with `SELECT ... FOR UPDATE` claims approved work before adapter invocation.

**Status:** Historical implementation. This does not claim provider-level exactly-once delivery.

### [ISHAI OS — source-backed read-only verification](./case-studies/ishai-os.md)
**Python · SQLite · GitHub API**

**Challenge:** An agent's assertion that an external task is complete is not evidence that it happened.

**Controlled demonstration:** Inspect a current GitHub pull request, validate digests of historical CI artifacts and store timestamped, source-attributed results without generating an unauthorized write proposal.

**Status:** Bounded demonstration, not general autonomy or a continuously deployed service.

## How I work

- Investigate failure states, retries and duplicate requests before claiming success.
- Keep durable state, authorization and audit evidence outside the model conversation.
- Use GitHub pull requests, CI and source-linked checks to distinguish implemented, tested and deployed work.
- Document limitations clearly; private repositories are not presented as publicly reproducible code.

## Technical toolkit

**Infrastructure:** Linux / Ubuntu · AWS EC2 / S3 / IAM · Cloudflare Workers / D1 / R2 · Docker · PM2  
**Software:** Python · TypeScript · JavaScript · Node.js · Express · REST APIs · webhooks  
**Data & delivery:** PostgreSQL · Redis · Git · GitHub Actions · CI/CD · task queues

## Links

[GitHub](https://github.com/Ishaipita) · [LinkedIn](https://www.linkedin.com/in/ishai-chertkoff-b252183b3/) · [RACAI](https://rac-ai.com/) · [RACAI Operator case study](./case-studies/racai-operator.md) · [Control-Room case study](./case-studies/control-room.md) · [ISHAI OS case study](./case-studies/ishai-os.md)
