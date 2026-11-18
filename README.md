# news-image-nov-18

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/wenjinqin/news-image-nov-18/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/wenjinqin/news-image-nov-18/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One page that sums up the world news of **Wednesday 18 November 2026**,
drawn entirely with code — no photographs, no stock art. The front page
leads with the Quad summit in Manila and carries five more of the day's
stories as illustrated panels:

- **Trump, Modi lead Quad summit in Manila** — Quad leaders open their
  summit and unveil new maritime, AI and cyber initiatives.
- **Military plane crash kills 19 in Siberia** — a Russian transport plane
  comes down; all 19 aboard die.
- **Nvidia beats forecasts, bars Huang return** — strong earnings, but the
  board rules out the founder's return as CEO.
- **US loses its measles-free status** — elimination status withdrawn as
  cases keep climbing.
- **Netanyahu blow as Knesset elects speaker** — parliament picks an ally
  of rival Gadi Eisenkot as its speaker.
- **Scientist sacked after gene-trial death** — China dismisses a
  scientist after a six-year-old dies in a gene-editing trial.

A ticker along the bottom adds Ebola cases doubling in DR Congo, Dhoni's
IPL retirement, a 27-year US sentence over an Iran-backed Trump plot and
Mongolia's president resigning.

`draw18.py` renders `entry.png` (1024 × 1024) with Pillow; `main.ts` is
the contest program — it validates the image against the gate's limits
and copies it to `/output/entry.png` in the grading sandbox.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
python3 draw18.py                                     # regenerates entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=d5a50dzy&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
