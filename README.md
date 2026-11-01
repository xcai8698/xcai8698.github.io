# 共建笔记 · Human × AI

一个极简、以阅读为中心的个人记录站点。使用原生 HTML + CSS 构建，无需 Node.js、构建工具、数据库或第三方前端框架。

## 站点结构

```text
.
├── index.html                 # 首页：主题介绍与文章索引
├── assets/
│   └── site.css               # 全站统一样式
└── notes/
    ├── about-this-space.html  # 关于本站
    └── template.html          # 新文章模板（复制后使用）
```

## 发布与更新

站点以静态文件方式运行。启用 GitHub Pages 后，提交到发布分支的文件会被直接发布。

### 新增一篇文章

1. 复制 `notes/template.html`，用日期和简短主题命名，例如 `notes/2026-11-12-agent-memory.html`。
2. 编辑新 HTML 文件中的标题、日期、分类、摘要和正文。
3. 打开根目录的 `index.html`，在“最近记录”区域的 `<div class="writing-list">` 中复制一条 `<a class="writing-item">...</a>`，修改文章标题、日期、摘要、分类和链接。
4. 提交（Commit）修改。GitHub Pages 会自动发布更新。

### 修改已有文章

直接编辑对应的 `notes/*.html` 文件并提交即可。文章样式由 `assets/site.css` 统一控制，通常不需要修改 CSS。

### 修改首页

直接编辑根目录的 `index.html`。主题卡片、介绍文字和文章列表都在这个文件中。

## 内容维护建议

- 一篇文章对应一个独立 HTML 文件，避免把所有内容堆在首页。
- 文件名使用 `YYYY-MM-DD-short-topic.html`，方便按时间查找。
- 文章尽量保留问题背景、关键证据、判断过程和结论。
- 尚未验证的内容明确标注，不把 AI 生成的猜测写成事实。
- 不要把密码、访问令牌、个人隐私或公司内部敏感信息提交到公开仓库。

## GitHub Pages 设置

在仓库 **Settings → Pages** 中，将 **Deploy from a branch** 设为发布方式，选择 `master` 分支和 `/ (root)` 目录并保存。

当前仓库名为 `xcai8698.github.io`，所属账号为 `xcai8698`。这是账号对应的 GitHub Pages 个人主页仓库，默认访问地址是：

`https://xcai8698.github.io/xcai8698.github.io/`

站点根地址：`https://xcai8698.github.io/`。


## 文章维护 Skill

仓库内置了可复用的 ChatGPT / Codex Skill：

- 入口：[`.agents/skills/personal-site-article-maintainer/SKILL.md`](.agents/skills/personal-site-article-maintainer/SKILL.md)
- 规范：[`references/site-contract.md`](.agents/skills/personal-site-article-maintainer/references/site-contract.md)
- 校验脚本：[`scripts/validate_site.py`](.agents/skills/personal-site-article-maintainer/scripts/validate_site.py)

它负责把笔记整理成文章、沿用现有 HTML/CSS、维护首页文章索引，并在提交前检查元数据和本地链接。提交到 `master` 即会公开发布；仅要求起草时不会自动提交。
