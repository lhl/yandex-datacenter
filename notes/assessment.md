# Evidence assessment

## Questions

1. Did attacks on Yandex facilities cause a measurable interruption in Yandex-originated automated web requests?
2. Did that interruption propagate to coordinated influence activity on third-party platforms?
3. Did it change ordinary bot, crawler, spam, or service traffic outside Yandex's own network?

## Evidence hierarchy

### A. Directly supported

- Yandex's 9 October statement says Sasovo was seriously damaged and completely shut down after the 7–8 October attack; it says Kaluga was attacked on 9 October and part of that infrastructure was out of service.
- BBC reporting says a Vladimir data center was later damaged and that Yandex paused operations there. It also reports service interruptions.
- Cloudflare Radar is a relevant measurement source for automated HTTP requests. The Cloudflare bot-class documentation defines scores 1–29 as likely automated and 30–99 as likely human.

### B. Reported but not independently reconstructed here

- Tom's Hardware and Cybernews quote a Yandex-network chart showing a fall to 0.4% of the two-week maximum, after an initial fall to about 57% on 8 October.
- We have not yet obtained a stable machine-readable export of the underlying Radar series. Preserve a screenshot/export in a future update before treating the percentage as a reproducible time series.

### C. Not established by the reviewed evidence

- That the affected automated requests were Russian state influence bots.
- That the requests were posting to X, Reddit, Facebook, or other social platforms.
- That the viral AfD chart measures bots or has a valid causal connection to the strikes.
- That reported quietness in a subreddit, lower spam calls, or fewer political posts is caused by the attacks.

## Main confounders

- “Bot” is overloaded: search crawlers, monitoring, API clients, scrapers, fraud tools, and influence accounts are different populations.
- Known Russian data-center IP ranges are often blocked by major platforms. Covert operations can use residential proxies, compromised devices, commercial VPNs, or foreign cloud providers.
- Weekend effects, news-cycle effects, moderation, ranking changes, platform outages, and changes in query coverage can create apparent drops.
- Cloudflare's chart is source-network and request-class data, not a content or account census.

## Testable research design

### Network layer

- Archive AS13238 Radar values at a fixed cadence, plus total Russian bot traffic and YandexBot directory metadata.
- Add Cloudflare Radar outage and traffic pages for Russia, Ukraine, and relevant control countries.
- Compare against other Yandex ASNs and major Russian/foreign networks to distinguish facility-specific loss from broader Russian connectivity changes.
- Estimate level change, time to minimum, and rebound/rerouting. Use the attack windows as interventions, but avoid claiming the strikes alone caused all changes.

### Platform layer

- Build a pre-registered list of queries for AfD, CDU, SPD, Greens, US political terms, UK Reform, and control terms.
- Keep language, timezone, retweet/repost exclusions, and observation windows constant.
- Measure posts, unique accounts, posting intervals, account age distribution, text similarity, and coordinated-cluster indicators separately.
- Compare multiple weekends and unrelated breaking-news events.

### Telephony and email

- Use only opt-in aggregate reports or a provider's anonymized abuse telemetry. Individual call logs are anecdotal and confounded by campaigns, carrier filters, and seasonal changes.

## Provisional conclusion

The defensible statement is: **documented Yandex facility damage coincided with a sharp decline in Yandex-network automated HTTP requests. Public evidence reviewed so far does not demonstrate that Russian social-media influence operations or political bot accounts went offline.**

The most valuable next artifact is a timestamped, reproducible Radar export and a matched multi-platform event study.
