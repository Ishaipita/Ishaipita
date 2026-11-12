# ISHAI OS
*Engineering case study · Local-first personal agent and verifiable execution*

**Stack:** Python, SQLite, GitHub API, local model experiments  
**Status:** Active development; owner-observed, bounded read-only verification, not production or general autonomy.

[← Portfolio](../README.md)

## The problem

A task marked “completed” is not necessarily a task that was performed. During development, an agent could prepare an external action in a local outbox and still report success. A separate read-only request could be misrouted toward a pull-request proposal. Both cases exposed a critical design requirement: **intent, authorization, execution and evidence must be distinct states**.

## What changed

I worked on a bounded workflow where a Hebrew request to inspect a GitHub pull request triggers authenticated, read-only GitHub access instead of a write proposal. The workflow reads current pull-request state, checks a specified historical CI run, verifies two original CI artifact archives against recorded SHA-256 digests, and saves a timestamped, source-attributed result. A subsequent answer can distinguish an older observation from a newer verified state.

This is a deliberately narrow integration, not a claim that the agent can browse or operate arbitrary services.

## The engineering principle

```text
USER REQUEST
    |
UNDERSTAND INTENT
    |
SCOPE + PERMISSION CHECK
    |
READ-ONLY TOOL EXECUTION
    |
VERIFY REMOTE EVIDENCE
    |
STORE SOURCED RESULT
    |
REPORT VERIFIED / BLOCKED / FAILED
```

A prepared proposal is not a completed external action. A successful local test is not a production deployment. Historical evidence must remain traceable without being mistaken for the latest state.

## Field note — 12 November 2026

The acceptance request was written in Hebrew and asked the local Control Room to check the **current** state of a GitHub pull request, validate two named artifacts from a specified **historical** CI run, and preserve the result with sources.

| Check | Observation | What it does *not* prove |
|---|---|---|
| Pull request | A fresh authenticated API read returned a merged state with an observation timestamp | The CI run belongs to the merged head |
| Artifact integrity | Two ZIP archives were downloaded and their SHA-256 values matched the corresponding upload records in the CI job log | Hash matching alone establishes provenance or release readiness |
| Authorization | This read-only diagnostic created no write approval or pull-request proposal | Every possible request is safely classified |
| Memory | A new, source-attributed record superseded an earlier stale observation without deleting history | General long-term personal understanding |
| Execution | A verified read result was distinguished from a historical proposal that never left an outbox | General autonomous action or production uptime |

The artifacts and runtime state are private. These observations are a controlled engineering demonstration and are **not presented as an independently reproducible public audit**.

## What the demonstration establishes

- A real GitHub read-only workflow can return current pull-request status and validate CI artifact digests.
- The agent can preserve source references and record a newer observation without deleting earlier history.
- The permission boundary can prevent a read-only request from creating an unintended write proposal.
- Development tests cover failure and recovery paths, but test coverage does not establish continuous uptime.

## What remains open

General multi-step autonomy, broad language-model quality, production deployment, continuous operation, and additional connected services are not established by this demonstration. Source code, operational credentials and personal memory remain private.

## Relation to earlier work

[Control-Room](./control-room.md) explored scoped execution and human approval boundaries. ISHAI OS continues that engineering direction in a personal, local-first agent.

---

*This case study is a public technical summary, not a disclosure of private infrastructure or an independent audit.*
