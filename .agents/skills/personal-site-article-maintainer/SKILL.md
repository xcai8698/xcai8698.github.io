---
name: personal-site-article-maintainer
description: Create, revise, quality-check, and publish articles for the personal site at https://xcai8698.github.io/. Use when the user asks to turn notes or AI conversations into a site article, edit an existing article, add an article to the homepage index, or publish changes to this HTML/CSS site. Preserve the site's editorial style and existing content; do not redesign the site unless explicitly asked.
---

# XCAI AI Space Station Article Maintainer

Maintain the user's personal knowledge and reflection site as a small, stable collection of hand-authored HTML pages. Optimize for editorial quality, factual care, readability, and design consistency—not volume or novelty.

## Site identity\n\n- Public-facing name: `xcai 的 AI 空间站`\n- English descriptor: `XCAI · AI SPACE STATION`

- Repository: `xcai8698/xcai8698.github.io`
- Default branch: `master`
- Public site: `https://xcai8698.github.io/`
- Stack: static HTML + shared CSS + one small local vanilla JavaScript file for theme behavior. No build step, framework, CMS, database, or external UI library.
- Homepage: `index.html`
- Shared styles: `assets/site.css`
- Theme behavior: `assets/theme.js`
- Article template: `notes/template.html`
- Articles: `notes/*.html`
- The homepage and every article share a light/dark theme toggle. First visit follows the operating-system preference; a manual choice is saved in `localStorage` and reused across pages.
- The site is public. Never publish credentials, personal secrets, confidential employer/customer information, non-public code, personal data about third parties, or material the user has not authorized for public release.

## When to use

Use for writing, refining, adding, updating, organizing, or publishing an article on this site. It also applies when the user provides raw notes, a chat transcript, a technical investigation, a decision record, or a reflection and asks to turn it into a durable article.

Do not use this workflow for a full website redesign, a new application, or changing deployment architecture unless explicitly requested.

## Required principles

1. **Preserve meaning.** Keep the user's core point of view, caveats, uncertainty, and first-person voice. Improve structure and expression without silently changing conclusions.
2. **Do not invent facts.** Separate confirmed facts, interpretation, and open questions. Do not turn a plausible AI-generated explanation into a verified statement. For externally verifiable or time-sensitive facts, verify with trustworthy sources when browsing is available and cite links in the article when useful.
3. **Write for later rereading.** Prefer a clear problem, context, reasoning, evidence/experience, conclusion, and unresolved questions over a transcript-like dump.
4. **Keep HTML and CSS stable.** Use the existing article template and shared classes. The default remains the narrow prose layout; when an editorial/magazine presentation is requested, use the reusable `.zine-*` classes in `assets/site.css` (as demonstrated by `notes/2026-11-10-ai-collaboration-as-assets.html`). Add reusable shared CSS only when needed, never one-off inline styling. Preserve the local `../assets/theme.js` script and theme toggle. Do not add custom fonts, frameworks, or CDN dependencies.
5. **Make the smallest safe change.** Do not alter `assets/site.css`, homepage design, existing articles, navigation, or deployment settings as part of an ordinary article update.
6. **Protect the public site.** A commit to `master` publishes. A request to “draft” or “help me write” means prepare content for review, not publish it. A request to “update the site”, “add this article”, or “publish” authorizes repository edits after validation. If intent is unclear, prepare a draft and ask before committing.

## Workflow

### 1. Understand the request and source

- Classify the task: new article, edit, correction, or index-only change.
- Gather supplied notes and relevant context already in the conversation. Never ask for information already provided.
- For an existing article, fetch the current HTML first; preserve useful material and links unless asked otherwise.
- If the target article is ambiguous, ask one concise question. Otherwise propose a reasonable title and filename.
- If content may expose private/company information, flag it and prepare a public-safe version before publication.

### 2. Shape the article

Use a structure appropriate to the topic; do not force identical headings into every article. The site supports two reading treatments: a restrained prose article (default) and an editorial zine layout with serif display headings, masthead, numbered sections, fine rules, two-column copy/panel modules, pull quotes, muted panels, and source notes. Choose the zine treatment when the user asks for a magazine/editorial layout; keep it responsive and compatible with both light and dark themes.

- Title: specific and understandable without chat context.
- Lead: one short paragraph explaining the question, significance, or takeaway.
- Body: meaningful sections with `h2`; use `h3` only when needed.
- Evidence: concrete examples, decisions, trade-offs, references, or lessons when present in the source.
- Conclusion: what is now understood, what changed, or what remains unresolved.

Keep first-person reflection when valuable. Remove conversational filler, repeated prompts, and unsupported claims. For technical articles, preserve context, constraints, versions, key steps, failure modes, and verification status. For reflections, preserve nuance and avoid turning opinions into universal advice.

### Visual communication

Choose the visual form according to the information being explained; do not add imagery decoratively.

- Use hand-authored inline SVG for technical architecture, event flows, state machines, sequence relationships, comparisons, and layered responsibility boundaries. It keeps labels precise, scales cleanly, supports light/dark themes, and remains editable in the static HTML site.
- Use CSS/HTML diagrams for simple cards, timelines, matrices, and editorial emphasis when SVG adds no value.
- Use React Flow only when the article genuinely needs interactive exploration, draggable nodes, zoomable large graphs, or user-editable topology. Do not add its runtime to ordinary static articles.
- Use generated raster images for conceptual illustrations, atmosphere, or visual metaphors—not for diagrams where exact labels, connections, or technical correctness matter.
- Prefer a small number of meaningful figures placed next to the explanation they clarify. Every figure needs a caption and, where useful, accessible SVG title/description. Check mobile readability and light/dark contrast.
- Diagrams must distinguish source-backed project behavior from the author's conceptual interpretation. Label reconstructed diagrams as explanatory redraws, not original project diagrams.

### 3. Follow the HTML contract

Read `references/site-contract.md` and use `assets/article-template.html` as the structural reference. Before repository changes, fetch the current `notes/template.html` and `assets/site.css`; repository files are authoritative.

Every article must:

- Be a complete HTML document with doctype, `lang="zh-CN"`, UTF-8, responsive viewport, title, non-empty description meta, and `../assets/site.css`.
- Use existing classes: `.article-shell`, `.article-header`, `.back-link`, `.article-heading`, `.eyebrow`, `.article-meta`, `.prose`, and `.article-footer` where appropriate.
- Contain exactly one primary `h1` agreeing with the page title.
- Include a valid ISO date in `<time datetime="YYYY-MM-DD">` and a readable date label.
- Include a concise lead paragraph, normally 1–3 sentences.
- Use semantic HTML: `h2`, `h3`, `p`, lists, `blockquote`, `pre`/`code`, and `a` as appropriate.
- Link back to `../index.html`, load `../assets/site.css` and `../assets/theme.js` correctly, and retain the accessible `[data-theme-toggle]` button in `.article-header`.
- Avoid empty headings, placeholders, broken links, invalid nesting, unnecessary wrappers, and inline visual styling.

New article naming: `notes/YYYY-MM-DD-short-topic.html`, with lowercase ASCII kebab-case topic. Do not rename an existing article solely for consistency; preserve inbound links.

### 4. Maintain the homepage index

When adding an article, update the “最近记录” list in `index.html`:

- Add exactly one `.writing-item` anchor to the correct relative file path.
- Include date, title, factual excerpt, and accurate category tag.
- Keep newest-first order. Never create duplicate entries.
- Do not alter hero text, topic cards, page layout, or CSS during routine article work.

When editing an article, update its index excerpt/title/date only if inaccurate. When deleting or renaming, find and update all inbound links; never silently orphan a page.

### 5. Editorial review

Check that:

- The title reflects the actual subject.
- The lead makes the article's value clear.
- The article can be understood without the original chat.
- Facts, opinions, assumptions, and open questions are distinguishable.
- Names, dates, versions, units, and numbers are accurate.
- Repetition is removed without losing important nuance.
- Headings are informative and not excessive.
- Links are relevant and trustworthy.
- No fabricated citations or unsupported claims remain.

When evidence is insufficient, narrow the wording or mark it as an assumption/open question. Never fill gaps with confident-sounding prose.

### 6. Validate

Run `scripts/validate_site.py` against a local checkout or downloaded site tree when available. Also verify:

- Homepage article links point to existing HTML files.
- Article stylesheet and home links resolve.
- Required metadata and exactly one `h1` exist.
- Local fragments resolve where checkable.
- No inline styles, CDN dependencies, or unapproved scripts were introduced; the shared local `../assets/theme.js` is present.
- No duplicate homepage entries exist.
- Only intended files changed.

State any validation limitation; do not claim a check passed if it was not run.

### 7. Publish safely through GitHub

When the user asks to update/publish and the GitHub connection is available:

1. Fetch current repository state and current blob SHAs.
2. Prepare the article and any homepage index change.
3. Validate before writing.
4. Commit only intended files to `master`, with clear commit messages. Never force-push or rewrite history.
5. Re-fetch changed files to confirm committed content.
6. Check the latest GitHub Pages Actions run for that commit and report build/deploy conclusions.
7. Do not claim the page is live merely because a commit succeeded. Confirm deployment success; if HTTP access is available, check the published page too.
8. If publication fails, diagnose the actual error; do not make unrelated changes.

Avoid parallel writes to the same file. If a file changed since it was fetched, re-fetch and reconcile rather than overwriting newer work.

## Response

Report the article title and path, whether the homepage index changed, checks performed and limitations, whether changes are draft-only or published, and commit/deployment links when available. Keep the report concise; do not repeat the whole article unless asked.
