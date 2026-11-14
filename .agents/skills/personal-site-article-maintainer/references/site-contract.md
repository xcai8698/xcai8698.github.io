# Site contract: `XCAI 的 AI 空间站` (`xcai8698.github.io`)

The live repository is authoritative; fetch current files before editing.

## Visual language

- Light theme: warm off-white background (`--paper: #f7f7f4`), charcoal text (`--ink: #252824`), calm gray secondary text (`--muted: #777b74`), subdued blue-green accent (`--accent: #526d73`).
- Dark theme: deep charcoal-green background with soft off-white text and the same subdued blue-green accent; all surfaces, borders, and prose colors are CSS variables.
- System sans for interface/body and a serif stack for editorial titles.
- Narrow centered reading column (`.article-shell`, approximately 720px maximum width), generous whitespace, fine borders, restrained callouts.
- Quiet editorial style: avoid bright gradients, decorative cards, heavy shadows, dense sidebars, or unnecessary UI. For selected long-form essays, an optional magazine treatment is available through reusable `.zine-*` classes: serif cover title, masthead rules, numbered sections, balanced two-column text/panel layouts, pull quotes and a restrained source footer. The reference implementation is `notes/2026-11-10-ai-collaboration-as-assets.html`.
- A compact day/night toggle appears in the homepage navigation and every article header. First visit follows system preference; manual selection persists via `localStorage`.

## File map

```text
index.html
assets/site.css
assets/theme.js
notes/about-this-space.html
notes/template.html
```

The site brand is `XCAI 的 AI 空间站` (English descriptor: `XCAI · AI SPACE STATION`). New articles belong in `notes/`. Shared appearance belongs in `assets/site.css`; theme behavior belongs in `assets/theme.js`. Article work should not normally change shared files, but may add reusable `.zine-*` rules when the user explicitly requests the editorial magazine treatment.

## Article structure

Use the complete document scaffold from `notes/template.html`. Its article body should follow this pattern:

```html
<div class="article-shell">
  <header class="article-header">
    <a class="back-link" href="../index.html">← 返回首页</a>
    <button class="theme-toggle" type="button" data-theme-toggle aria-label="切换到黑夜模式" aria-pressed="false" title="切换到黑夜模式">
      <span class="theme-toggle-icon" aria-hidden="true">☾</span>
      <span class="theme-toggle-label">黑夜模式</span>
    </button>
  </header>
  <main>
    <header class="article-heading">
      <p class="eyebrow">NOTE / CATEGORY</p>
      <h1>文章标题</h1>
      <div class="article-meta">
        <time datetime="2026-11-01">2026.11.01</time>
        <span>分类名称</span>
        <span>阅读约 X 分钟</span>
      </div>
    </header>
    <article class="prose">
      <p class="article-lead">文章导语。</p>
      <h2>章节标题</h2>
      <p>正文。</p>
    </article>
  </main>
  <footer class="article-footer">
    <a class="back-link" href="../index.html">← 回到记录索引</a>
  </footer>
</div>
```

The full page must retain the doctype, Chinese language, UTF-8, viewport, title, description metadata, `../assets/theme.js` script and `../assets/site.css` link in the current template. Load the theme script before the stylesheet to reduce a flash of the wrong theme.

## Homepage index contract

The homepage `#journal` section contains `.writing-list`. Each item follows this pattern:

```html
<a class="writing-item" href="notes/YYYY-MM-DD-topic.html">
  <span class="writing-date">YYYY.MM.DD</span>
  <span class="writing-main">
    <span class="writing-title">文章标题</span>
    <span class="writing-excerpt">一句简短摘要。</span>
  </span>
  <span class="writing-tag">分类</span>
  <span class="writing-arrow" aria-hidden="true">↗</span>
</a>
```

Keep entries newest first. The displayed title, date, and summary must agree with the linked page.

## Content style

- Chinese by default unless requested otherwise.
- Clear, calm, precise, reflective; avoid marketing language and inflated claims.
- Start from a concrete question or experience. Preserve reasoning and trade-offs.
- For technical articles, include context, constraints, versions, steps, results, and verification status.
- Mark uncertainty and distinguish personal interpretation from established facts.
- Use lists only when they improve scanning; prefer connected prose for reflection.

## Change boundaries

- New article: normally one new `notes/*.html` plus one `index.html` update.
- Existing article edit: normally one article file and, only if needed, its homepage item.
- Do not modify styles, global navigation, domain settings, or deployment configuration during routine article maintenance.
