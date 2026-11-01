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

当前仓库名为 `xuchuanmin.github.io`，所属账号为 `xcai8698`。按 GitHub Pages 的项目站点规则，默认访问地址通常是：

`https://xcai8698.github.io/xuchuanmin.github.io/`

如需使用 `https://xuchuanmin.github.io/` 作为根域名，需要将仓库调整为账号对应的 `xcai8698.github.io` 并配置域名/DNS；当前仓库名本身不会自动成为该账号的根站点域名。
