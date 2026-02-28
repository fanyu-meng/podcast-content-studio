# Podcast Show Notes Generator

A Cursor AI skill for generating podcast show notes from transcript PDFs. Designed for **破壁圆桌** (Pobi Yuanzhuo), a podcast from Munich featuring conversations with outstanding Chinese professionals across industries.

## Features

- **Title generation** — Catchy, scroll-stopping titles with specific hooks (numbers, names, contrasts)
- **Guest introductions** — Narrative-style bios, not resume-style
- **Main content** — Multiple writing styles: news-anchor parody, story + suspense, direct commentary
- **Topic-based timestamps** — Chronological timestamps formatted for 小宇宙 / Apple Podcasts / Spotify
- **Human voice** — Avoids AI-sounding phrases; uses specific facts, quotes, and personal reactions

## How to Use

1. Install the skill in Cursor (place the `.cursor/skills/podcast-shownotes/` folder in your Cursor skills directory)
2. Provide a PDF file containing the full podcast transcript with timestamps
3. Follow the interactive workflow: choose title focus, content angle, and writing style
4. Copy the generated show notes into your podcast platform

## Project Structure

```
├── .cursor/skills/podcast-shownotes/
│   ├── SKILL.md          # Skill definition and workflow
│   ├── style-guide.md    # Writing rules and anti-patterns
│   └── examples.md       # Reference examples
├── template.md           # Output template
├── example1.md           # Example output (EP15)
├── example2.md           # Example output
├── example3.md           # Example output
└── EP19_shownotes.md     # Sample generated show notes
```

## 破壁圆桌 — Listen Here

- [小宇宙](https://www.xiaoyuzhoufm.com/podcast/67cdacc32deb5237c648049f)
- [Apple Podcasts](https://podcasts.apple.com/de/podcast/%E7%A0%B4%E5%A3%81%E5%9C%86%E6%A1%8C/id1719475456?l=en-GB)
- [Spotify](https://open.spotify.com/show/6YfmptM1qzz9bmc7HLrzVQ?si=5060c1f2ea8148f0)

## License

MIT
