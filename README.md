# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/oraybora-source/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/oraybora-source/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image summing up the world's news of Friday 20 November 2026: a giant date masthead, four big illustrated heroes (Cyclone Akvan's landfall in India, Nicholls' 175* in Wellington, COP31's last day in Antalya, missiles over Kyiv), 14 illustrated story cards and 15 more briefs across seven regions — 33 stories in all. A numbered world map sits beside the briefs; every story on the page happened, or was first reported, on Friday 20 November 2026, and the DATE CHECK band names 18 stories from 17–19 November that were left out on purpose.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## How the image was made

`compose_v2.py` composes `entry.png` (1024×1024) from the illustration assets in `assets/` plus text rendered from verified news strings (see `STORIES.md`, research cutoff 20 Nov 2026 afternoon WIB). All 18 illustrations share one flat editorial house style — no copied artwork, no photos, no text inside the illustrations; every word on the page is drawn by `compose_v2.py`. The frame is sketch 6 "CALM" (Kevin's pick from 6 sketches): navy masthead band, framed deck, hour-by-hour timeline (01:25–21:00) with gold dots, six framed number cards with gold bars, navy panel strips, sources folded inline into each summary, and a world map with numbered pins. `main.py` (Python 3.13, standard library only) copies `entry.png` to the output directory; it runs twice in grading and writes identical bytes both times.

---

<sub>Entered on [make.fun](https://make.fun/?ref=s4486c7v&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
