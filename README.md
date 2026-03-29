# 播客内容生成器

**仓库名：** `podcast-content-studio`（GitHub 仓库与本地克隆目录建议与此一致。）

基于 [Agent Skills](https://agentskills.io/) 规范的 skill 合集，覆盖播客制作里常见的**文字工作**：从**采访前的大纲与调研**，到**上线用的 show notes**，再到**小红书等社交平台的宣传文案**。面向播客制作者，可自定义模板和风格。支持 Cursor、Claude Code、Codex 等 AI 开发工具。

## 典型工作流

1. **录前**：用采访大纲 skill 做嘉宾调研、问题设计与开场白。  
2. **录后**：用 show notes skill 从转录稿 PDF 生成节目笔记与时间戳。  
3. **宣发**：用小红书文案 skill 从转录稿或已有 show notes 生成推广帖。

三步可独立使用，也可按顺序串起来。

## 包含三套 Skill

### Skill 1: 采访大纲 (`interview-outline`)

录前准备：根据嘉宾信息与网络调研，生成适合对话节目的采访素材。

- **嘉宾侧写** — 背景与亮点，便于你心里有数  
- **分主题问题** — 有递进、可追问，口语化  
- **开场白参考** — 自然引入话题，不是念简历  
- **人味写作** — 具体、好聊，避免清单式 AI 腔  

适用场景：采访大纲、采访提纲、嘉宾调研、播客录前准备。

### Skill 2: Show Notes (`podcast-shownotes`)

从转录稿生成播客平台节目笔记，用于小宇宙 / Apple Podcasts / Spotify。

- **标题** — 有吸引力，用具体数字、人名、反差做 hook  
- **嘉宾介绍** — 叙事体，不是简历体  
- **主要内容** — 多种风格：新闻联播戏仿体、故事悬念体、直接吐槽体  
- **时间戳** — 按话题整理，适合播客平台  
- **人味写作** — 避免 AI 腔，多用具体事实、金句和主观感受  

### Skill 3: 小红书文案 (`xiaohongshu-copywriting`)

从转录稿或已有 show notes 生成小红书宣传文案，吸引新听众。

- **纯文字帖** — Hook + 要点 + 金句 + CTA  
- **多角度文案** — 同一期 2～3 篇不同角度，适合分天发或 A/B  
- **图文笔记文案** — 为 carousel 提供每页文字 + 帖子正文  
- **Hook-first** — 前 2 行抓人，针对信息流优化  
- **Hashtag** — 通用 + 内容相关话题标签  

## 快速上手

1. 安装 skill（见下方「多平台支持」）。  
2. 按任务准备输入：嘉宾信息 / 转录稿 PDF（建议带时间戳）/ 已有 show notes。  
3. 对 AI 说一句简单指令即可，例如：

**采访大纲：**
```text
请根据这位嘉宾的信息帮我写一版采访大纲。
```

**Show notes：**
```text
请根据这份转录稿生成本期 show notes。
```

**小红书文案：**
```text
请根据这份转录稿生成小红书宣传文案。
```

或用已有 show notes 生成小红书：
```text
用这份 show notes 生成一篇小红书帖子。
```

4. 按交互提示完成选择，复制结果到对应平台使用。

## 示例

- 采访大纲：`output/interview-outlines/刘嘉卓_outline.md`  
- Show notes：`output/shownotes/EP21_Katie_Shownotes.md`  
- 小红书文案：`output/xiaohongshu/EP21_xiaohongshu_all.md`  
- 历史风格参考：`references/`  
- 小红书文案更多示例：`.cursor/skills/xiaohongshu-copywriting/examples.md`  

## 多平台支持

本项目遵循 Agent Skills 开放规范，可在以下平台使用：

| 平台 | 安装方式 |
|------|----------|
| **Cursor** | 将 `.cursor/skills/interview-outline/`、`podcast-shownotes/`、`xiaohongshu-copywriting/` 置于项目内对应路径 |
| **Claude Code** | 复制到 `.claude/skills/`（项目级）或 `~/.claude/skills/`（个人级） |
| **Codex** | 手动复制到 `~/.codex/skills/` 下对应目录 |

每个 skill 目录含 `SKILL.md`、`style-guide.md`、`examples.md`（部分 skill）。模板在 `templates/` 下按类型分目录。

## 项目结构

```
├── .cursor/skills/
│   ├── interview-outline/              # Skill 1: 采访大纲
│   │   ├── SKILL.md
│   │   ├── style-guide.md
│   │   └── examples.md
│   ├── podcast-shownotes/              # Skill 2: Show Notes
│   │   ├── SKILL.md
│   │   ├── style-guide.md
│   │   └── examples.md
│   └── xiaohongshu-copywriting/        # Skill 3: 小红书文案
│       ├── SKILL.md
│       ├── style-guide.md
│       └── examples.md
├── transcripts/                        # 转录稿 PDF
├── templates/
│   ├── interview-outline/
│   │   └── template.md
│   ├── shownotes/
│   │   └── template.md
│   └── xiaohongshu/
│       ├── text-post.md
│       ├── multi-angle.md
│       └── carousel.md
├── output/
│   ├── interview-outlines/             # 采访大纲输出
│   ├── shownotes/                      # Show Notes 输出
│   └── xiaohongshu/                    # 小红书文案输出
└── references/                         # 历史风格与参考
```

## 示例播客

本项目示例来自 **破壁圆桌**，一档来自慕尼黑的华人对话播客。欢迎收听：

- [小宇宙](https://www.xiaoyuzhoufm.com/podcast/67cdacc32deb5237c648049f)  
- [苹果播客](https://podcasts.apple.com/de/podcast/%E7%A0%B4%E5%A3%81%E5%9C%86%E6%A1%8C/id1719475456?l=en-GB)  
- [Spotify](https://open.spotify.com/show/6YfmptM1qzz9bmc7HLrzVQ?si=5060c1f2ea8148f0)  

## License

MIT
