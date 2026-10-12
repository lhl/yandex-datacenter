# Reddit activity event study

Sources:

- Reddit discussion: https://www.reddit.com/r/theydidthemath/comments/1x3q43a/offsite_comparing_reddit_activity_around_three/
- Author's research repository: https://github.com/silkier-muses/raes
- Infographic: https://files.catbox.moe/3xe10s.png
- Original data/code archive: https://files.catbox.moe/eqj4gh.zip
- Local infographic copy: [`sources/images/theydidthemath-yandex-infographic.png`](images/theydidthemath-yandex-infographic.png)

Captured: 2026-10-12 UTC

## What the study does

The study uses Syften public hourly counts of subreddit posts plus comments, in UTC. It examines 1,221 selected communities; 968 pass activity/completeness rules. It compares 12-hour windows around three reported Yandex incidents with the preceding 12 hours, adjusting each hour against the same weekday/hour 7, 14, and 21 days earlier. It also checks 10-hour windows, alternative start times, and a broad-sample benchmark.

The original result is easy to misread because the infographic highlights the nominal screen:

- 90 of 968 eligible communities have negative adjusted `r` and negative adjusted percentage change in all three nominal windows.
- **Zero** retain both negative directions across every tested start hour and both 10/12-hour window lengths.
- The author explicitly describes the analysis as exploratory and descriptive, not a causal difference-in-differences estimate and not a bot census.

The repository includes the complete first-release archive, including 1,221 source snapshots, 908,424 hourly cells, results, sensitivity rows, source hashes, and reproduction code. Its stated SHA-256 for `eqj4gh.zip` is:

```text
bf93862bd93b17bc5fdea74e1dae84024b96e0dfa33010e057e678afbf8a5ed2
```

The downloaded archive matched that hash.

## What is genuinely interesting

This is much stronger than an anecdotal “the subreddit felt quiet” report because it:

- exposes the underlying aggregate data and code;
- includes the full eligible universe rather than only the displayed political examples;
- reports positive and excluded communities as well as nominal decreases;
- performs timing and window-length sensitivity checks;
- discloses that no result survives all timing checks;
- removes two hours associated with a documented Reddit status incident.

The accompanying X graphic from Irish Politics Newsletter shows a related, smaller presentation of the nominal pattern: `r/de`, `r/askarussian`, `r/irishpolitics`, `r/czech`, `r/sweden`, and `r/spainpolitics`, with event-specific drops around Sasovo, Kaluga, and Vladimir. That image is archived locally at [`sources/images/irish-politics-reddit-event-study.webp`](images/irish-politics-reddit-event-study.webp). It appears to be derived from the same research line, but the X post itself does not expose the full data or methods.

## Main limitations

1. **No independent control-date/placebo distribution.** The study asks whether 90 is unusual, but does not yet compare the same procedure across unrelated dates. That is the most important missing analysis. With 968 communities and three windows, many nominal matches are expected under ordinary variability.
2. **The timing is uncertain.** The event anchors are analyst-selected proxies, not verified strike instants. The later pre-windows can also contain effects from earlier incidents.
3. **The outcome is not bot activity.** Posts plus comments measure aggregate subreddit activity observed by Syften. They cannot identify bots, users' locations, server providers, or political affiliations.
4. **The treatment is not clearly connected to Reddit.** Even if Yandex traffic fell, the study does not show that the affected Reddit activity used Yandex infrastructure.
5. **The correlation statistic is assumption-sensitive.** The author is transparent that `r` is a within-incident, adjusted before/after association, not a correlation between three event totals. Its interpretation depends heavily on the selected windows and historical adjustment.
6. **Possible serial dependence and carryover.** Three closely spaced events are not independent replications, and 7/14/21-day references may include unusual events or earlier disruption.
7. **Selection and multiple comparisons.** The subreddit set is broad but not random, and ranking 1,221 series makes extreme-looking results unsurprising without a pre-specified target or an empirical null.

## Assessment

This is currently the most useful Reddit-side artifact in the collection, but its strongest result is negative: **the apparent 90-community pattern is not timing-stable, and the study provides no evidence that those declines were bot removals.** It supports a focused follow-up rather than the claim that Yandex attacks demonstrably silenced political bots.

The next analysis should run the identical pipeline on many placebo event triplets or matched unrelated dates, preserving weekday, hour, holiday, outage, and news-cycle structure. Only then can the nominal 90/968 figure be compared with a null distribution. A second improvement would be to pre-register a small set of communities and outcomes before looking at the event-period results.
