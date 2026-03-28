---
name: podcast-shownotes
description: Generate podcast show notes from a transcript PDF. Produces a catchy title, guest intro, main content summary, and topic-based timestamps — all written in a natural, human voice (not AI-sounding). Use when the user provides a podcast transcript and wants show notes, shownotes, 播客笔记, 节目笔记, or 时间戳.
---

# Podcast Show Notes Generator

## Input

A PDF file containing the full podcast transcript with timestamps.

## Workflow

### Step 1: Read and parse the transcript

Read the PDF file. Extract:
- All spoken text and speaker identifications
- All timestamps present in the transcript
- Episode number (if mentioned)

### Step 2: Identify guests and key topics

From the conversation content, extract for each guest:
- Name (Chinese + English if applicable)
- Current role / identity
- Background and key experiences mentioned in the conversation
- Notable achievements or credentials
- Any links mentioned (website, social media)

Also identify 3-5 candidate highlight topics from the transcript that could serve as title hooks or content focus points. These should be the most specific, surprising, or emotionally compelling moments.

### Step 3: Interactive — ask the user 3 questions

Before drafting, ask the user the following questions. Use the AskQuestion tool if available; otherwise ask conversationally. Present all 3 questions together in one round.

**Question 1: Title focus**

Present the 3-5 candidate highlight topics identified in Step 2 as options, and ask:
> "以下是我从转录中提取的几个最有亮点的细节，你希望标题围绕哪个点来写？也可以自己输入想强调的内容。"

Options: the 3-5 candidate topics + a "自定义输入" option.

**Question 2: Main content angle**

Ask the user about the main content's focus. Provide options based on the episode's themes, plus a custom input option:
> "主要内容的侧重点你希望放在哪里？"

Options (adapt to the actual episode content, below are examples):
- 嘉宾的个人经历和故事
- 方法论和可操作的建议
- 行业观察和趋势分析
- 轻松有趣的对话和互动
- 自定义输入

**Question 3: Style preference**

Ask the user about their preferred writing style:
> "你希望这期 show notes 用什么风格来写？你也可以上传一个你喜欢的 show notes 示例作为参考。"

Options:
- 新闻联播戏仿体（正经语言写不正经内容，反差幽默）
- 故事悬念体（用"从...到..."叙事弧线，提问制造好奇）
- 直接吐槽体（主持人视角的主观评价和感受）
- 上传自己的示例作为参考
- 使用默认风格（参考内置示例）

If the user uploads a custom example, read it and extract its style characteristics (tone, structure, vocabulary patterns) to guide the writing in subsequent steps.

### Step 4: Draft the title

Using the user's title focus preference from Step 3, craft the title.

Generate 3 candidate titles incorporating the user's preferred emphasis point. For each, check:
- Does it contain a specific detail (number, name, place)?
- Would someone scroll-stopping to read more?
- Does it avoid all phrases listed in the anti-pattern section below?

Pick the best one. Format: `EP{N}：{hook}`

Before finalizing, read [style-guide.md](style-guide.md) section "标题写作" for detailed rules and examples.

### Step 5: Write guest introductions

Write in narrative style, not resume style. One concise summary line, then a short story of their journey. End with a human touch. Include links if available.

Read [examples.md](examples.md) for reference on guest intro style.

### Step 6: Write main content

Apply the user's chosen style from Step 3. Apply the user's chosen content angle from Step 3.

If the user chose a built-in style:
- **News-anchor parody**: formal language for informal content, creating contrast humor
- **Story + suspense**: use "从...到..." arcs, end with questions
- **Direct commentary**: personal reactions, behind-the-scenes details

If the user uploaded a custom example, match that example's tone, structure, and vocabulary.

Include:
- A narrative arc focused on the user's chosen angle (not a topic list)
- Host's subjective reactions and feelings
- Recording details if interesting (location, atmosphere, funny incidents)

### Step 7: Create timestamps

#### Step 7a: Identify major topics

Go through the transcript chronologically and identify the **major discussion topics** — not individual sub-points, quotes, or anecdotes within a topic.

A "major topic" is a coherent segment of conversation that usually lasts 3–8 minutes, where the discussion revolves around one theme before transitioning to the next. For example, "如何跟老板建立关系" is one major topic; the sub-points within it ("partner关系", "怕老板", "角色逆转", "提供价值的时机") should NOT each get their own timestamp.

#### Step 7b: Locate exact timestamps

For each major topic, find its **start time** in the transcript:
- The time **must** come from an actual `发言人X MM:SS` (or `发言人X HH:MM:SS`) marker in the transcript — pick the speaker-turn marker closest to where that topic begins
- **Never** estimate, interpolate, or round timestamps — only use times that literally appear in the transcript text
- When in doubt, prefer the speaker-turn marker immediately before the topic begins over one after

#### Step 7c: Write timestamp descriptions

For each topic timestamp, write a compelling mini-headline:
- Extract the most specific, surprising, or vivid detail from that topic segment as the hook
- A single timestamp description can reference multiple highlights within the topic (use dashes or semicolons)
- Follow all writing style rules in [style-guide.md](style-guide.md)

Format: `MM:SS 标题关键词：具体描述内容`

Rules:
- Use Chinese colon `：` to separate the topic label from the description
- Each timestamp on its own line, with a **blank line** between each timestamp
- Include names, numbers, quotes, and use punctuation (？！) to convey emotion
- Timestamp lines must stay as plain text (no bullets, no numbering, no extra markdown symbols) so they can be directly copy-pasted into 小宇宙 / Apple Podcasts / Spotify
- For episodes longer than 60 minutes, use `H:MM:SS` format instead of `MM:SS`

#### Step 7d: Verify

Go back to the transcript and verify **every** timestamp:
- Confirm that the text within 30 seconds of the timestamp actually corresponds to the described topic
- If there is a mismatch, replace the timestamp with the correct speaker-turn marker from the transcript
- Do not skip this step

#### Density guide (topic-level, not point-level)

- Under 30 min: 5–8 timestamps
- 30–60 min: 8–12 timestamps
- Over 60 min: 10–15 timestamps
- Minimum gap between adjacent timestamps: 2 minutes

### Step 8: Assemble and output

Output the final show notes in the exact template format below.

## Output Template

Output format: `.md` (Markdown). **Output directory: `output/shownotes/`** — always save the file into this folder relative to the workspace root.

Section headers (书名号 content) must be **bold** using `**`; all section content (especially timestamps) should remain plain text without markdown list syntax.

```
EP{N}：{标题}

**『本期嘉宾』**

{嘉宾1介绍}

{嘉宾链接（如有）}

**『主要内容』**

{主要内容描述}

**『时间戳』**

{MM:SS 标题关键词：具体描述}（超过60分钟的节目用 H:MM:SS）

{MM:SS 标题关键词：具体描述}

{MM:SS 标题关键词：具体描述}
...

**『播客渠道』**

小宇宙，苹果Podcast，Spotify

**『主播』**

子鱼：专业音频工程师，业余吉他手，业余脱口秀演员
Lumi：临床医学博士，光学博士后，开发生物医学用的光学设备，创业筹备中。排球队主力。

**『关于我们』**

破壁圆桌，与不同行业优秀华人的碰撞。
圆桌主播来自慕尼黑。定期邀请不同行业的优秀华人参与圆桌讨论，从AI和科技行业出发，探索我们认知之外的世界。
打破中西壁垒，行业壁垒，认知壁垒。
关注科技，以及海外华人生活职场和个人成长。
邀请优秀华人，参与圆桌讨论，拓宽认知边界。

**『联系我们』**

微信号：t-ransformer（备注：破壁圆桌 + 50字左右自我介绍）
```

Formatting rules:
- Each section title (`**『xxx』**`) is on its own line
- A blank line between the title and its content
- A blank line between each section

Important:
- Each timestamp entry has a blank line after it
- The fixed sections (播客渠道, 主播, 关于我们, 联系我们) are appended verbatim every time — do NOT modify their content
- The final output must be complete and ready to copy-paste without any user edits

## Anti-Patterns (NEVER use these)

**Banned title phrases:** 深入探讨, 深度解析, 全面剖析, 探索...的魅力, 干货满满, 不容错过, 赋能, 破圈

**Banned body phrases:** 在...的道路上, 让我们一起, 带您走进, 分享了宝贵的经验和见解, 碰撞出思想的火花, 令人深思, 满满的干货, 收获颇丰

**Instead:** Use specific facts, numbers, quotes, and personal reactions. Say "从0做到20亿" not "取得了巨大的商业成功".

For the complete anti-pattern list and replacement strategies, see [style-guide.md](style-guide.md).

## References

- [style-guide.md](style-guide.md) — Detailed writing style rules, good/bad comparisons, banned phrases
- [examples.md](examples.md) — 3 annotated real examples showing the target style
