# Marketing Strategy — MTD Checker

## Objective
Drive real organic traffic to https://mtd-checker.vercel.app/ from people who'll actually use the calculator and (where relevant) click an affiliate software link — without ever risking the Reddit account's standing or violating TikTok's automation policy. A banned/shadowbanned account or a blacklisted domain is a total failure, full stop — it's worse than zero growth.

## Reality constraints (confirmed via research, re-check periodically — rules change)
- **Reddit:** no blanket ban on self-promotion, but the unofficial 90/10 (or 90-9-1) rule is the real norm — roughly 90%+ of account activity should be genuine participation, no more than ~10% promotional, measured across the account's history. Posting identical content across multiple subreddits in a short window is the fastest path to a site-wide spam flag. Multiple accounts promoting the same thing, or self-upvoting, is a bannable offense Reddit actively detects.
- **Our specific handicap:** current account is 3 years old with ~1 karma — dormant-then-suddenly-active accounts are a known spam signal. Plan starts with a karma-building, link-free phase.
- **TikTok:** the only sanctioned automated posting path is TikTok's official Content Posting API (OAuth2, ~15-25 posts/day cap, shared across API clients). Anything outside that official API for automated posting violates ToS and risks a ban — we will not build or use unofficial posting automation.
- **Per-subreddit rules are not yet verified** (Reddit's pages aren't fetchable by our tools) — see [subreddits.md](subreddits.md). No subreddit gets posted to until its specific rules are confirmed.

## Content pillars (3, kept tight on purpose)
1. **"Am I affected and when?"** — practical answers to the core anxiety (dates, thresholds, what counts as qualifying income).
2. **"What do I actually do about it?"** — software choice, getting digital records started early, what quarterly updates look like.
3. **"What happens if I get it wrong?"** — penalties explained factually and reassuringly (the soft-landing year, point expiry), aimed at reducing fear rather than spiking it.

All three map directly to sections already built into the site, so genuine answers can (when relevant and allowed) point to a specific section rather than just the homepage.

## Value-to-promotion ratio per platform
- **Reddit:** 90/10 minimum, enforced by *not posting promotional content at all* until the account has a real base of genuine comments. Even after that, most contributions stay non-promotional.
- **TikTok:** value-first by format — the video itself must be useful/interesting independent of the link; the link is a secondary CTA, never the hook.

## Phasing
1. **Karma & credibility building (Reddit), account setup (TikTok)** — weeks 1-3+, no links, no tool mentions, just genuinely useful participation and, on TikTok, genuinely useful videos building an audience before any link-in-bio push.
2. **Earned mentions** — only in subreddits confirmed 🟢 in subreddits.md, only where the answer to an actual question is improved by mentioning the tool, always disclosed.
3. **Scale what works** — once we have real click-through and conversion data (via UTM tracking), double down on the specific subreddits/formats that converted, drop what didn't.

## KPIs
- Reddit: comment karma growth, % of activity that's promotional (must stay ≤10%), click-throughs via UTM links, no removals/warnings.
- TikTok: views, completion rate, link-in-bio clicks, follower growth, no strikes/restrictions.
- Site: sessions by UTM source, affiliate link clicks, email signups, affiliate conversions (once those are live).

## Standing approvals
None granted yet. Every piece of content — Reddit comment, Reddit post, TikTok script, TikTok caption — goes into `APPROVALS/` for review until the user explicitly grants standing approval for a specific, narrow content type (e.g. "you can auto-post FAQ-answer comments in r/X without review").

## Open risks / riskiest assumptions
- That genuinely helpful participation from a near-zero-karma account will be accepted by these communities at all, rather than auto-filtered by spam detection regardless of content quality.
- That the relevant subreddits permit any self-promotion at all once we check — some ban it outright, in which case the plan for that community becomes "be a real, anonymous, helpful participant, no tool mentions, ever."
