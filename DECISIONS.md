# Decisions Log

## 2026-06-25 — Chose micro-tool model over content site or info-product
**Decision:** Build a single-purpose free calculator/checker tool monetized via affiliate links, rather than a content/affiliate site or a paid digital product.
**Why:** Lowest legal/reputational surface area for a UK/EU-based owner with no existing audience; smallest scope to build and automate; fits the moderate budget (£100-500) and 5-10 hrs/week.
**Alternatives considered:** Niche content/affiliate site (higher ceiling but slower SEO trust-building, more ongoing content-quality risk); digital info-product on Gumroad (highest per-unit payoff but blocked by having no distribution audience).

## 2026-06-25 — Selected niche: UK Making Tax Digital (MTD) for Income Tax checker
**Decision:** Build "MTD Checker" — a personalized tool for UK self-employed/landlords to find out when MTD rules affect them, monetized via UK accounting-software affiliate programs (FreeAgent, QuickBooks, Xero, Coconut).
**Why:** MTD thresholds roll out in stages through 2026-2028, creating a multi-year wave of fresh, recurring search demand. GOV.UK's official checker exists but is generic and doesn't personalize or follow up — leaves room for a better, narrower tool. Clear, established affiliate programs exist for monetization.
**Riskiest assumption:** People search for this ahead of their own threshold year rather than only in the weeks before their deadline. Must validate with real search-trend data in Phase 1 before building out full personalization logic.
**Status:** Selected, not yet validated.

## 2026-06-25 — Deployed via GitHub + Vercel, built out full content depth
**Decision:** Pushed the repo to github.com/JOEPARKER07/mtd-checker, connected to Vercel for auto-deploy on every push to main. Expanded the single-page tool with SEO metadata, FAQ schema (JSON-LD), worked examples, a penalties section (sourced from HMRC's points-based penalty system), and a pre-deadline checklist.
**Why:** Auto-deploy on push removes a manual step from every future content/code change, fitting the "autonomous agents" goal for later phases. The added content depth is the main lever to outrank GOV.UK's bare official checker in search — thin tools don't rank, useful explainers do.
**Status:** Live at https://mtd-checker.vercel.app/. Still on free Vercel subdomain — no custom domain purchased yet.

## 2026-06-25 — Marketing operator role established, Reddit/TikTok distribution scaffolded
**Decision:** Built `marketing/` with strategy, voice guide, candidate subreddit list, TikTok research, UTM scheme, and an approval queue. No content drafted or posted yet.
**Why:** User requested a dedicated growth/marketing operator role for TikTok and Reddit, with platform ToS treated as hard constraints and human approval required on everything public until standing approval is granted.
**Key constraint discovered:** Reddit account (u/Beneficial-Mark-1584) is 3 years old but ~1 karma — a dormant-then-active account is itself a spam signal, so the plan opens with a link-free, comment-only phase to build genuine history before any promotional content. Per-subreddit rules can't be fetched by our tools directly (Reddit blocks it), so live verification is a recurring human gate before any post, not a one-time research task.
**Status:** Research/scaffolding done. No content created or posted. TikTok account doesn't exist yet (needs user's identity verification to create).
