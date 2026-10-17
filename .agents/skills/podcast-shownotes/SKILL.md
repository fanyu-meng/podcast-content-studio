---
name: podcast-shownotes
description: Generate clear, natural podcast show notes from a transcript PDF, with restrained titles, fluent Chinese, guest introductions, episode summaries, and accurate timestamps. Use when the user asks for show notes, a podcast summary, or timestamps.
---

# Podcast Show Notes Generator

## Input

A transcript in PDF or another format. It may include speaker names and timestamps.

## Workflow

### Step 1: Read and parse the transcript

Read the full transcript. Extract:
- Speaker identities and the details they state about themselves
- The conversation and its topic changes
- Timestamps that appear in the transcript
- Episode number, if available

Do not treat an automatically generated opening summary as a substitute for reading the conversation.

### Step 2: Identify guests and key topics

For each guest, note only details supported by the transcript or user-provided context:
- Name and current role or identity
- Relevant background and experiences
- Achievements or credentials that matter to this episode
- Links mentioned in the source

Identify the episode's main themes and a few specific details that could help readers understand what makes this conversation worth hearing. Do not choose a hook solely because it sounds surprising or emotional.

### Step 3: Resolve editorial preferences

Follow any style, title, or focus instructions the user has already given. Otherwise, use the default style in this skill and make reasonable editorial choices without asking routine setup questions.

Ask a concise clarification only when an unresolved choice would materially change the result. Do not ask the user to choose among title, content-angle, and style options as a mandatory step.

### Step 4: Draft the title

Choose a title that is specific, easy to understand, and natural to say aloud. A clear detail or point of tension can make it engaging, but do not force a dramatic hook, a question, a number, or an emotional contrast when the episode does not call for one.

The format is `EP{N}：{标题}`. Consider a few alternatives internally, then provide the strongest fit. Avoid exaggeration, clickbait, and wording that promises more than the episode delivers.

### Step 5: Write the guest introduction

Introduce the guest in concise, readable Chinese. Start with the identity most relevant to the episode, then add a small number of meaningful experiences or career turns. Use a narrative sequence when it helps; do not force an “从A到B” arc or a personal ending. Include source-supported links when available.

Prefer natural Chinese word order and clear subjects. Keep credentials and English job titles from turning the introduction into a résumé or a string of nouns.

### Step 6: Write the main content

Summarize the episode as a coherent account of what the guest and hosts discuss. Give the reader the central question, the useful or revealing details, and how the conversation develops. Do not turn the section into a topic inventory.

Use the hosts' perspective when it adds a real observation, but do not invent reactions, recording anecdotes, setting, or opinions. The default tone is warm, measured, and conversational. A little literary quality should come from precise details, pacing, and well-shaped sentences—not ornate metaphors or heightened emotion.

Use parody, overt jokes, suspense questions, emphatic punctuation, or slang only when the user asks for that style or the recording itself clearly supports it. Never add drama just to make the copy sound lively.

### Step 7: Create timestamps

#### Step 7a: Identify major topics

Follow the conversation in order and mark coherent topic changes. A timestamp should represent a substantial segment, not every example, sub-point, or memorable sentence within one discussion.

#### Step 7b: Locate exact timestamps

- Use a timestamp that literally appears beside a speaker turn in the transcript.
- Never estimate, interpolate, or round a time.
- Choose the speaker-turn marker closest to the point where the topic begins. Check the surrounding text before using it.

#### Step 7c: Write timestamp descriptions

Use the format `MM:SS 话题：一句自然、具体的话` (`H:MM:SS` for episodes longer than 60 minutes).

- Keep each entry on its own plain-text line, with a blank line between entries.
- Write a compact, complete phrase or sentence with idiomatic Chinese word order.
- Include a specific name, example, number, or distinction when it helps identify the discussion; do not cram several unrelated details into one line.
- Use questions, exclamation marks, quotation marks, and dashes sparingly. Do not use them as a substitute for a clear description.
- Keep the description faithful to what is discussed, without turning it into a sensational claim.
- Timestamps must remain plain text, without bullets or numbering, for easy copying to podcast platforms.

#### Step 7d: Verify

Return to the transcript and check every timestamp against the speaker turn and nearby text. If the topic does not begin there, choose the closest valid marker that does.

#### Topic density guide

- Under 30 minutes: usually 5–8 timestamps
- 30–60 minutes: usually 8–12 timestamps
- Over 60 minutes: usually 10–15 timestamps
- Keep adjacent timestamps at least 2 minutes apart when the conversation allows.

Use judgment when a shorter episode has fewer substantial topic changes. Do not split a topic merely to reach a quota.

### Step 8: Assemble and output

Save the finished Markdown file under `output/shownotes/` using the episode number and guest name in the filename. Follow `templates/shownotes/template.md` for section order, fixed copy, and spacing. Keep the final document ready to publish.

Section headers (`**『xxx』**`) go on their own line. Keep timestamps as plain text and leave a blank line between each timestamp. Preserve the fixed podcast information exactly as it appears in the current template.

## Default writing principles

- Prefer accurate detail over inflated praise, and clarity over a forced hook.
- Read each sentence aloud mentally. Make the subject, action, and relationship between ideas easy to follow.
- Prefer idiomatic Chinese word order, concrete verbs, and varied sentence length. Break up sentences that carry too many clauses.
- Remove filler, repeated points, literal English phrasing, stacked modifiers, and abstract nouns that make the text hard to hear.
- Aim for a little literary texture through cadence and precise language. Avoid flowery wording, canned conclusions, and manufactured suspense.
- Keep all claims grounded in the transcript. If a detail is unclear, omit it rather than guess.

## Anti-patterns

Avoid generic or inflated phrases such as “深入探讨”“全面解析”“干货满满”“不容错过”“碰撞出思想的火花”“令人深思” and “收获颇丰”. Also avoid defaulting to “逆袭”“颠覆”“改变一切”“到底有多难？” or repeated exclamation marks when the transcript does not warrant them.

Replace general praise with a concrete fact. For example, name the actual design problem, explain what the AI could and could not do, or describe the trade-off the guest faced. Do not add unsupported numbers, achievements, quotes, or emotional reactions.

## Bilingual handling

- Write primarily in Chinese.
- Keep names, brand names, and technical terms in their commonly used original form.
- Explain an English term briefly on first use only when readers need the explanation.
- Avoid unnecessary code-switching and Chinese sentences that follow English syntax.

## References

- `style-guide.md` — Detailed tone, fluency, and section-specific guidance
- `examples.md` — Example copy and notes on adapting older, more stylized examples
