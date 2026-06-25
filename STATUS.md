# Status

_Last updated: 2026-06-25_

## Done
- Niche selected: MTD Checker (UK Making Tax Digital for Income Tax)
- Business brief written ([BRIEF.md](BRIEF.md))
- Repo scaffolded (README, DECISIONS, COSTS, .env.example, STATUS)
- Built working tool page ([site/index.html](site/index.html)) — calculator, timeline, software recs (affiliate links not yet live), email capture UI (not yet wired)
- **Live at https://mtd-checker.vercel.app/** — deployed via GitHub (JOEPARKER07/mtd-checker) + Vercel, auto-deploys on every push to main
- Verified live site loads and the calculator works end to end
- Built out full SEO/content depth: meta tags, FAQ schema, worked examples, penalties section, pre-deadline checklist, shareable result links, form validation, accessibility pass, robots.txt + sitemap.xml

## In progress
- Validating riskiest assumption: real search demand for MTD-related queries now vs. closer to each threshold deadline
- Deciding whether to buy a custom domain or stick with the free vercel.app subdomain for now

## Marketing arm (new)
- Scaffolded `marketing/` with STRATEGY.md, voice.md, subreddits.md, research_tiktok.md, utm_scheme.md, CONTENT_CALENDAR.md, APPROVALS/
- Reddit account (u/Beneficial-Mark-1584) is 3 years old, ~1 karma — aged but unproven, so plan starts with a link-free karma-building phase before any promotional content
- Per-subreddit rules NOT yet live-verified (Reddit pages aren't fetchable by our tools) — hard gate before any post, see subreddits.md
- No TikTok account exists yet
- No content has been posted anywhere — content calendar is intentionally empty until subreddit rules are verified

## Blocked on you
- Affiliate program signups (FreeAgent, QuickBooks UK, Xero, Coconut) need your identity/payment details — I'll send exact links when ready
- Email capture provider signup (free tier, e.g. Resend/Buttondown) needed to make the "Notify me" button actually work
- Analytics provider signup (free tier, e.g. Plausible) needed to start measuring real traffic
- TikTok account creation (needs your phone/identity verification)
- Manually checking the actual current sidebar/wiki rules for each candidate subreddit in marketing/subreddits.md (I can't fetch Reddit pages directly) — without this, no post can go out

## Next action
- Either: (a) sign up for analytics now so we measure traffic from day one, or (b) go check the subreddit rules in marketing/subreddits.md so the marketing plan can move from research to drafting actual content. Both are cheap, free, and unblock different parts of the system.
