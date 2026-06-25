# UTM Link Scheme

Every link we ever post anywhere uses these parameters, so clicks show up distinctly in analytics once it's connected. No exceptions — an unlabelled link is a link we can't measure.

## Parameters
- `utm_source` — the platform: `reddit`, `tiktok`
- `utm_medium` — `social` for both, for now
- `utm_campaign` — the content pillar: `am-i-affected`, `what-to-do`, `penalties`
- `utm_content` — a short slug identifying the specific post/video, e.g. `r-ukpersonalfinance-comment1`, `tiktok-video3-softwarecompare`

## Format
```
https://mtd-checker.vercel.app/?utm_source=reddit&utm_medium=social&utm_campaign=am-i-affected&utm_content=r-ukpersonalfinance-comment1
```

## Process
1. Every item drafted into `APPROVALS/` includes its exact UTM-tagged URL already built using this scheme.
2. The URL gets logged in `subreddits.md` (posting log) or `CONTENT_CALENDAR.md` at the same time it's marked posted — never after the fact, or we lose the link between content and result.
3. Once analytics (Plausible/Umami, still pending your signup) is live, UTM source/campaign/content show up as filters directly — that's how we tell, per the weekly report, which specific post/video drove which clicks.
