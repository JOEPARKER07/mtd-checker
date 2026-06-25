# MTD Checker

A free web tool that tells UK self-employed people and landlords exactly when HMRC's Making Tax Digital (MTD) for Income Tax rules will apply to them, what software they'll need, and offers a reminder email as their deadline approaches. Monetized via UK accounting-software affiliate programs.

See [BRIEF.md](BRIEF.md) for the full business rationale.

## How the system works end to end

```
Research agent  ──> finds keyword/content opportunities, writes to research/
Content agent   ──> drafts articles/copy, queued for review until trusted
Review queue     ──> human (you) approves before anything publishes
Publishing agent ──> ships approved content on schedule
Distribution agent──> posts to approved channels only, rate-limit aware
Monitoring agent ──> watches traffic/signups/affiliate clicks/errors, flags anomalies
```

All agents are scheduled background jobs (cron), are idempotent (safe to re-run),
log every action, fail safe (never spend money, never publish without approval
until explicitly trusted to skip the queue), and respect platform rate limits.

## Repo layout

- `BRIEF.md` — one-page business brief (who/what/why/how/riskiest assumption)
- `DECISIONS.md` — running log of every meaningful decision and why
- `COSTS.md` — ledger of every expense
- `STATUS.md` — at-a-glance: done / in progress / blocked on you
- `.env.example` — every credential the system needs and how to get it
- `site/` — the landing page + tool itself (added in Phase 2)
- `agents/` — scheduled automation jobs (added in Phase 3)
- `research/` — research agent output (keyword findings, topic ideas)

## Current phase

Phase 1 (validation) — see [STATUS.md](STATUS.md) for live status.

## Human checkpoints

Claude will always stop and ask before: spending money, buying domains/services,
anything needing legal identity (KYC/registration/tax), connecting financial
accounts or handling payments/refunds, publishing anything under your name with
legal/reputational risk, running paid ads, or any action it's <90% confident is
ToS/legal compliant.
