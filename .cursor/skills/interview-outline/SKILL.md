---
name: interview-outline
description: Generate podcast interview outlines for 破壁圆桌 from guest information and web research. Produces a guest profile, themed interview questions, and opening script — all in a casual, specific, human voice. Use when the user wants to prepare an interview, 采访大纲, 采访提纲, 播客准备, or 嘉宾调研.
---

# Podcast Interview Outline Generator

## Input

Guest information provided by the user: name, role, links, and a rough interview direction.

## Workflow

### Step 1: Collect guest information — Round 1

Ask the user the following 4 questions using AskQuestion (or conversationally). Present them together in one round.

**Q1: Guest name**
> "嘉宾的名字是什么？（中英文都写上，如果有的话）"

Free text input.

**Q2: Current identity**
> "用一句话描述嘉宾现在在做什么？"

Free text input.

**Q3: How you met**
> "你们是怎么认识/找到这个嘉宾的？"

Options:
- 嘉宾主动找上门的
- 朋友/听众推荐的
- 我们自己找到并邀请的
- 社交媒体上认识的
- 其他（自定义输入）

**Q4: Rough direction**
> "这次采访你最想聊的方向是什么？（可以很模糊，比如'聊聊她的创业经历'）"

Free text input.

### Step 2: Collect guest information — Round 2

Ask the user for reference materials. All fields are optional but encourage filling in as many as possible:

> "请提供嘉宾的相关链接和资料，越多越好——我会用这些来做调研，写出更有针对性的问题。没有的就跳过。"

- 个人网站 URL
- LinkedIn URL
- 社交媒体账号（小红书/Twitter/微博/Instagram 等）
- 过往采访/播客/YouTube 链接（可多个）
- 其他补充信息（如嘉宾发来的自我介绍、简历、作品集等）

If the user has files (PDF, text, etc.) with guest information, read them.

### Step 3: Web research

Conduct automated research using WebSearch and WebFetch.

#### 3a: Search queries

Run at least 3 searches, adapting keywords to the guest's field:

1. `"{guest_name_cn}" 采访 OR 播客 OR interview OR 对话`
2. `"{guest_name_en}" podcast OR interview OR keynote OR talk`
3. `"{guest_name}" {industry_keyword} {role_keyword}`

If initial results are thin, try additional queries:
- `"{guest_name}" site:linkedin.com`
- `"{guest_name}" site:xiaohongshu.com OR site:weibo.com`
- `"{guest_name}" {company_name}`

#### 3b: Fetch provided links

Use WebFetch to extract content from every URL the user provided (personal website, LinkedIn, past podcasts, etc.). If a URL is inaccessible, note it and move on.

#### 3c: Compile research brief

Synthesize all findings into a structured internal brief (shown to the user for review, not part of the final output):

- **核心履历** — education, career timeline, key roles
- **关键转折点** — career pivots, bold decisions, failures and comebacks
- **嘉宾原话/金句** — quotes the guest said themselves (interviews, social media, talks). Mark each as "嘉宾本人说的" vs "媒体转述"
- **与破壁圆桌的契合点** — how this guest connects to the podcast's themes (overseas Chinese experience, breaking barriers, career growth, tech, personal growth)
- **空白区域** — things you couldn't find that might be worth asking about

**Credibility filter:** Before including any detail, ask: "Is this something the guest themselves said or shared, or is it a journalist's paraphrase/embellishment?" Discard anything that looks like gossip, exaggeration, tabloid spin, or creative retelling by media. Prefer the guest's own words and verifiable facts (dates, awards, institutions). When in doubt, leave it out — it's better to ask the guest directly than to repeat something inaccurate.

Present this brief to the user before proceeding.

### Step 4: Confirm interview direction

Based on the research brief, ask the user 4 follow-up questions using AskQuestion. Present them together.

**Q1: Angle selection**

Extract 3-4 possible interview angles from the guest's story and present them:
> "根据调研，我觉得以下几个角度比较有意思，你想以哪个为主线？可以多选，也可以自定义。"

Options: 3-4 angles derived from the research + "自定义输入"

**Q2: Depth preference**
> "你想怎么安排深度？"

Options:
- 深聊 1-2 个主题，把故事讲透
- 均匀覆盖 3-4 个话题
- 先深后广：一个核心主题 + 几个快问快答
- 自定义

**Q3: Must-ask questions**
> "有没有你已经想好的问题，或者一定要聊到的点？（没有就跳过）"

Free text input.

**Q4: Off-limits**
> "有没有不该碰的话题或者需要注意的地方？（比如嘉宾不想聊前公司细节）"

Free text input.

### Step 5: Generate guest profile (optional)

The guest profile is primarily a reference for the interviewer, not a script to read aloud. Ask the user whether to include it in the output. If the user wants a concise outline (just questions + opening), skip this section entirely.

If included, read [style-guide.md](style-guide.md) for detailed rules. Structure:

1. **核心标签** — 3-5 slash-separated identity keywords (e.g., "前亚马逊 L8 总监 / 硅谷高管教练 / 职场非职权影响力专家")

2. **嘉宾亮点** — 3-4 bullet points, each with a bold sub-label:
   - Use specific numbers, names, and details
   - Highlight the contrast/surprise/story in each point
   - Only include facts you're confident are accurate — no journalist embellishments

3. **金句** — One impactful quote the guest themselves said (not journalist paraphrases). If none found, skip.

4. **相关链接** — All links (personal website, LinkedIn, social media, past interviews)

### Step 6: Generate interview questions

Read [style-guide.md](style-guide.md) and [examples.md](examples.md) before writing questions.

#### Section structure

Organize into 3-4 themed sections based on the user's chosen angles:

**第一部分：破冰暖场**（2-4 questions）

- Start with "自我介绍" — let the guest settle in naturally
- Follow with 1-2 simple, warm questions that ease into the conversation (current life, recent updates)
- Then 1-2 questions that use a specific, intriguing detail to spark a story — but only details you trust are accurate
- Include one question that lets the guest reveal personality (preferences, habits, hot takes)

**第二至四部分：主题讨论**（3-6 questions each）

For each themed section, **mix two kinds of questions:**

1. **Genuine, open questions** (~60%) — simple questions that help you truly understand the person. These don't need to reference any research. Examples: "你的偶像是谁？", "每天练多长时间？", "为什么选德国？", "什么时候开始独立创作的？". These questions work because the *answer* is specific to this guest, even if the question itself is universal.

2. **Research-backed questions** (~40%) — questions that reference a specific, verified detail (a quote the guest said, an award they won, a known career decision). These show you did your homework, but use them sparingly and only when the detail is trustworthy.

Additional guidance per section:
- End each section with a forward-looking or reflective question
- At least one question per section should touch the guest's inner world (feelings, motivations, doubts) rather than just facts

**Question writing rules:**

1. Use conversational tone — write questions as you would actually say them out loud
2. Keep simple questions simple. "你的吉他偶像是谁？" is a great question — don't add unnecessary preamble or research context to it
3. When referencing research, prefer the guest's own words over journalist paraphrases. Only cite external details you're confident are accurate
4. Add context/setup only for questions that need it: "听说你在深圳第一天就被问..." then the question
5. Mix question types: story prompts, opinion questions, simple factual questions, hypotheticals, quick-fire
6. Avoid multi-part questions with more than 2 sub-questions — split them up
7. The test for every question: "Does this help me genuinely understand who this person is?" If it's just trivia or gossip, cut it

#### Question count guide

- Icebreaker: 2-4 questions
- Each theme section: 3-6 questions
- Total: 12-20 questions for a 1.5-2 hour interview

### Step 7: Generate opening script and notes, then output

#### 7a: Opening script

Write the opening for 子鱼 and Lumi. Follow the established pattern:

```
子鱼：Hallo 大家好！欢迎回到破壁圆桌。我是子鱼。

Lumi：我是 Lumi。{一句话 hook — 用嘉宾最抓人的细节引出}

子鱼/Lumi：{补充嘉宾另一个亮点，制造好奇}

Lumi/子鱼：欢迎{嘉宾名}来参加我们的播客！首先邀请{嘉宾名}先跟听众朋友们打个招呼，也简单介绍一下自己。
```

Rules:
- 子鱼 and Lumi alternate lines — who says which depends on what sounds natural
- The hook should be specific and intriguing, not a resume summary
- Keep it under 5 lines total

#### 7b: Recording notes

Append the standard notes block verbatim:

```
### Notes：

* 不想用真实姓名，可以用化名
* 和正常聊天一样，随时jump in
* 随便说，相信后期剪辑的力量
* 时长：1.5h - 2h
* 最好有耳麦/带麦克风的耳机；如果有的话，带线的比无线的更好
```

#### 7c: Assemble and output

Combine all sections into the output template format (see Output Template below). Save to `output/interview-outlines/` with filename `EP{N}_{guest_name}_outline.md`. If no episode number is known, use the guest name only: `{guest_name}_outline.md`.

## Output Template

Output format: `.md` (Markdown). **Output directory: `output/interview-outlines/`** — always save the file into this folder relative to the workspace root.

```
{如果用户要求包含嘉宾资料：}

# 嘉宾资料

**核心标签：** {slash-separated identity keywords}

**嘉宾亮点：**

* **{亮点标签1}：** {具体描述，带数字和细节}
* **{亮点标签2}：** {具体描述}
* **{亮点标签3}：** {具体描述}

{金句（如有）}

{所有相关链接，每个一行}

{如果用户不需要嘉宾资料，直接从采访大纲开始：}

# 采访大纲

**一、 暖场 + 访谈**

1. {破冰问题1}
2. {破冰问题2}
3. {破冰问题3}

**二、 {主题标题}**

1. {问题}
2. {问题}
...

**三、 {主题标题}**

1. {问题}
2. {问题}
...

**四、 {主题标题}**（如需要）

1. {问题}
2. {问题}
...

### Notes：

* 不想用真实姓名，可以用化名
* 和正常聊天一样，随时jump in
* 随便说，相信后期剪辑的力量
* 时长：1.5h - 2h
* 最好有耳麦/带麦克风的耳机；如果有的话，带线的比无线的更好

**开场：**

**子鱼：** {开场白}

**Lumi：** {开场白}

**子鱼/Lumi：** {开场白}
```

Formatting rules:
- `# 嘉宾资料`（if included）and `# 采访大纲` are H1 headings
- Section titles within 采访大纲 are bold: `**一、 暖场 + 访谈**`
- Questions are numbered lists within each section
- A blank line between each section
- Notes block uses `###` heading and `*` bullet points
- Opening script lines use bold speaker names: `**子鱼：**`

## Anti-Patterns (NEVER use these)

### Banned question openers
- "请您谈谈..." / "能否分享一下..."
- "您对...有什么看法？"（太空泛）
- "您觉得...的意义是什么？"
- "请问您是如何看待...的？"

### Banned descriptive phrases
- 深入探讨 / 深度解析 / 全面剖析
- 分享宝贵的经验和见解
- 碰撞出思想的火花
- 干货满满 / 收获颇丰
- 赋能 / 破圈 / 硬核
- 在...的道路上 / 在...的浪潮中

### Banned question patterns — gossip & over-research

- Treating unverified news details as fact: "听说你一怒之下从1楼弹到4楼" — unless the guest said this themselves
- Referencing trivial anecdotes from tabloid-style articles to seem "well-researched"
- Packing every question with researched details — this makes the outline read like a fact-check quiz, not a conversation
- Quoting numbers or stories from third-party articles without verifying the guest actually said or confirmed them

### Replacement strategy

Bad questions come in two flavors. Fix each differently:

**Type 1: Too vague** — add a concrete, verified detail:
- Bad: "请分享一下您的创业经历" → Good: "你一个人跑到深圳，第一天就被问'你凭什么'——当时怎么想的？"
- Bad: "请谈谈您的管理经验" → Good: "管过1000人的团队，到了你这个级别，最常被下属误解的是什么？"

**Type 2: Too gossip-y / trivial** — replace with a genuine question:
- Bad: "听说你逮着谁都问要不要听你弹琴，连收水电费的阿姨都不放过" → Good: "你的吉他偶像是谁？"
- Bad: "你爸月薪100多块花了1100给你拉网线" → Good: "退学那个决定是你自己提出来的，还是爸爸的主意？"
- Bad: "拿到冠军那天晚上第一个电话打给了谁？" → Good: "欧洲吉他奖冠军，这个奖项对你意味着什么？"

For the complete style guide and more examples, see [style-guide.md](style-guide.md).

## References

- [style-guide.md](style-guide.md) — Question design principles, good/bad comparisons, banned expressions
- [examples.md](examples.md) — Annotated examples from real 破壁圆桌 interview outlines
