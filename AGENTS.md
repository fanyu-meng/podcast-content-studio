# Sync Rule: UNIVERSAL_PROMPT.md

When any of the following files are modified, you **must** also update `UNIVERSAL_PROMPT.md` in the project root to reflect the same changes:

- `.cursor/skills/podcast-shownotes/SKILL.md`
- `.cursor/skills/podcast-shownotes/style-guide.md`
- `.cursor/skills/podcast-shownotes/examples.md`
- `templates/shownotes/template.md`

## How to sync

1. Identify what changed in the source file
2. Find the corresponding section in `UNIVERSAL_PROMPT.md` using the mapping below
3. Apply the equivalent change, with these adaptations:
   - Remove references to tool-specific features (AskQuestion tool, file output paths, etc.)
   - Keep the content self-contained — no relative file references like `[style-guide.md](style-guide.md)`
   - Preserve the "works with any AI chat product" framing
4. Confirm to the user: "已同步更新 UNIVERSAL_PROMPT.md"

## Section mapping

| Source file | UNIVERSAL_PROMPT.md section |
|---|---|
| `SKILL.md` Step 1-8 | 📋 工作流程 |
| `style-guide.md` 标题/嘉宾/主要内容/时间戳 | Step 4-7 中的写作规则和示例对比 |
| `style-guide.md` 禁用词汇 | 🚫 禁用词汇和表达 |
| `style-guide.md` 双语处理 | 💡 双语处理 |
| `examples.md` | 📚 完整示例 |
| `template.md` | 📄 输出模板 |
