# 播客节目笔记生成器

基于 Cursor AI 的 skill，从播客转录稿 PDF 生成节目笔记（show notes）。面向任何播客制作者，可自定义模板和风格。

## 功能

- **标题生成** — 有吸引力、抓眼球，用具体数字、人名、反差做 hook
- **嘉宾介绍** — 叙事体，不是简历体
- **主要内容** — 多种风格：新闻联播戏仿体、故事悬念体、直接吐槽体
- **时间戳** — 按话题整理，适合小宇宙 / 苹果播客 / Spotify
- **人味写作** — 避免 AI 腔，多用具体事实、金句和主观感受

## 使用方法

1. 在 Cursor 中安装 skill（将 `.cursor/skills/podcast-shownotes/` 放到 Cursor 的 skills 目录）
2. 提供带时间戳的完整播客转录稿 PDF
3. 按交互流程选择：标题焦点、内容侧重、写作风格
4. 将生成的节目笔记复制到播客平台

## 项目结构

```
├── .cursor/skills/podcast-shownotes/
│   ├── SKILL.md          # Skill 定义与工作流
│   ├── style-guide.md    # 写作规则与禁用词
│   └── examples.md       # 参考示例
├── template.md           # 输出模板
├── example1.md           # 示例输出（EP15）
├── example2.md           # 示例输出
├── example3.md           # 示例输出
└── EP19_shownotes.md     # 生成示例
```

## 示例播客

本项目示例来自 **破壁圆桌**，一档来自慕尼黑的华人对话播客。欢迎收听：

- [小宇宙](https://www.xiaoyuzhoufm.com/podcast/67cdacc32deb5237c648049f)
- [苹果播客](https://podcasts.apple.com/de/podcast/%E7%A0%B4%E5%A3%81%E5%9C%86%E6%A1%8C/id1719475456?l=en-GB)
- [Spotify](https://open.spotify.com/show/6YfmptM1qzz9bmc7HLrzVQ?si=5060c1f2ea8148f0)

## License

MIT
