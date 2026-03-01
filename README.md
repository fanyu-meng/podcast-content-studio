# 播客内容生成器

基于 Agent Skills 规范的 skill 合集，从播客转录稿 PDF 一站式生成 **show notes** 和 **小红书宣传文案**。面向播客制作者，可自定义模板和风格。支持 Cursor、Claude Code、Codex 等 AI 开发工具。

## 包含两套 Skill

### Skill 1: Show Notes 生成器 (`podcast-shownotes`)

从转录稿生成播客平台节目笔记，用于小宇宙 / Apple Podcasts / Spotify。

- **标题生成** — 有吸引力、抓眼球，用具体数字、人名、反差做 hook
- **嘉宾介绍** — 叙事体，不是简历体
- **主要内容** — 多种风格：新闻联播戏仿体、故事悬念体、直接吐槽体
- **时间戳** — 按话题整理，适合播客平台
- **人味写作** — 避免 AI 腔，多用具体事实、金句和主观感受

### Skill 2: 小红书文案生成器 (`xiaohongshu-copywriting`)

从转录稿或已有 show notes 生成小红书宣传文案，吸引新听众。

- **纯文字帖** — 一篇完整的推广文案，Hook + 要点 + 金句 + CTA
- **多角度文案** — 同一期生成 2-3 篇不同角度的帖子，适合分天发布或 A/B 测试
- **图文笔记文案** — 为 carousel slides 提供每页文字内容 + 帖子正文
- **Hook-first** — 前 2 行必须抓人，针对小红书信息流优化
- **Hashtag 生成** — 自动生成通用 + 内容相关的话题标签

## 快速上手

1. 安装 skill（见下方多平台支持）。
2. 上传播客转录稿 PDF（建议带时间戳）。
3. 对 AI 说一句简单指令即可：

**生成 show notes：**
```text
请根据这份转录稿生成本期 show notes。
```

**生成小红书文案：**
```text
请根据这份转录稿生成小红书宣传文案。
```

也可以用已有的 show notes 生成小红书文案：
```text
用这份 show notes 生成一篇小红书帖子。
```

4. 按交互提示完成选择，拿到最终文案后复制到平台发布。

## 示例

- Show notes 生成示例：`output/shownotes/EP19_shownotes.md`
- 小红书文案生成示例：`output/xiaohongshu/EP19_xiaohongshu_all.md`
- 历史风格参考：`references/`
- 小红书文案示例（内置于 skill）：`.cursor/skills/xiaohongshu-copywriting/examples.md`

## 多平台支持

本项目遵循 [Agent Skills](https://agentskills.io/) 开放规范，可在以下平台使用：

| 平台 | 安装方式 |
|------|----------|
| **Cursor** | 复制 `.cursor/skills/podcast-shownotes/` 和 `.cursor/skills/xiaohongshu-copywriting/` 到项目内对应路径 |
| **Claude Code** | 复制到 `.claude/skills/` 下对应目录（项目级）或 `~/.claude/skills/` 下（个人级） |
| **Codex** | 手动复制到 `~/.codex/skills/` 下对应目录 |

每个 skill 目录含 SKILL.md、style-guide.md、examples.md。模板在 `templates/` 下按类型分目录。

## 项目结构

```
├── .cursor/skills/
│   ├── podcast-shownotes/              # Skill 1: Show Notes
│   │   ├── SKILL.md
│   │   ├── style-guide.md
│   │   └── examples.md
│   └── xiaohongshu-copywriting/        # Skill 2: 小红书文案
│       ├── SKILL.md
│       ├── style-guide.md
│       └── examples.md
├── transcripts/                        # 转录稿 PDF
├── templates/
│   ├── shownotes/
│   │   └── template.md                # Show Notes 输出模板
│   └── xiaohongshu/
│       ├── text-post.md               # 纯文字帖模板
│       ├── multi-angle.md             # 多角度文案模板
│       └── carousel.md                # 图文笔记模板
├── output/                             # 生成结果
│   ├── shownotes/                     # Show Notes 输出
│   └── xiaohongshu/                   # 小红书文案输出
└── references/                         # 历史风格参考
```

## 示例播客

本项目示例来自 **破壁圆桌**，一档来自慕尼黑的华人对话播客。欢迎收听：

- [小宇宙](https://www.xiaoyuzhoufm.com/podcast/67cdacc32deb5237c648049f)
- [苹果播客](https://podcasts.apple.com/de/podcast/%E7%A0%B4%E5%A3%81%E5%9C%86%E6%A1%8C/id1719475456?l=en-GB)
- [Spotify](https://open.spotify.com/show/6YfmptM1qzz9bmc7HLrzVQ?si=5060c1f2ea8148f0)

## License

MIT
