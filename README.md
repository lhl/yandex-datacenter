# Yandex data-center disruption and online traffic

A source-led research archive for testing claims that October 2026 attacks on Yandex data centers changed automated web traffic, social-media activity, influence operations, or spam/call activity.

## Current bottom line

The strongest public evidence currently supports a narrower claim than the viral posts make:

- Yandex says its Sasovo facility was seriously damaged and shut down on the night of **7–8 October 2026**, and that part of Kaluga infrastructure was disabled on 9 October.
- Yandex later reported that its Vladimir facility was damaged and operations were suspended. BBC and other reporting describe three affected facilities that week.
- Cloudflare Radar data, as quoted by Tom's Hardware and Cybernews, showed automated HTTP requests associated with Yandex's network (AS13238) falling sharply, reportedly to **0.4% of the recent two-week maximum**. This is not a direct count of social-media bots.
- Cloudflare's classification defines likely automated traffic as bot scores 1–29. Cloudflare's YandexBot directory identifies YandexBot as a search-engine crawler. The observed metric therefore plausibly includes ordinary crawling and other automation.
- The evidence reviewed here does **not** establish that Russian influence accounts on Reddit, X, Facebook, or other platforms went offline, or that the Yandex event caused changes in AfD, pro-Trump, Reform UK, spam-call, or subreddit activity.
- A German fact-check by Rohtext found that the viral AfD chart had no reproducible source or methodology and that a short weekend comparison did not show an AfD-specific collapse.

This repository deliberately separates **verified infrastructure events**, **measured network indicators**, and **anecdotal or causal claims**.

## Repository map

- [`notes/assessment.md`](notes/assessment.md) — evidence assessment, hypotheses, and falsification criteria.
- [`data/sources.json`](data/sources.json) — source ledger with provenance, dates, claims, and confidence.
- [`sources/`](sources/) — dated excerpts from key pages, preserved for later comparison. These are excerpts, not immutable web archives.
- [`data/observations.csv`](data/observations.csv) — normalized observations and their evidentiary status.
- [`scripts/check_sources.py`](scripts/check_sources.py) — small consistency check for the source ledger.

## How to reproduce or extend

1. Record every observation with URL, UTC capture time, exact metric definition, geography, time window, and whether it is a first-party measurement or a report of one.
2. Preserve screenshots or exported JSON for Cloudflare Radar charts. A live chart can change and some Radar endpoints require access that ordinary HTTP fetching does not provide.
3. Use event-study windows around 7–11 October: at minimum 14 days before and 14 days after, with unaffected networks and countries as controls.
4. Do not use the generic word “bot” as a proxy for “propaganda account.” Analyze separately: crawler requests, account posts, coordinated-account clusters, residential/VPN/proxy infrastructure, and telephone spam.
5. For social platforms, collect platform-native counts or a documented API/search export. Record query syntax, language, retweet/repost handling, account sampling, and rate limits.
6. Treat correlation as provisional until the same source-specific traffic falls at the time of each facility event and rebounds or reroutes in a traceable way.

## Research status

Initial archive captured 2026-10-12 UTC. This is an active research notebook, not a conclusion that any party or operation was responsible for any particular traffic.

## License and ethics

Use source terms where applicable. Do not attempt to identify private individuals, deanonymize accounts, or target infrastructure. Prefer aggregate, reproducible measurements and public reporting.
