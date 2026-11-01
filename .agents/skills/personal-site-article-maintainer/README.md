# Personal Site Article Maintainer

A reusable Agent Skill for writing, revising, quality-checking, and publishing articles to `https://xcai8698.github.io/`.

## Package contents

- `SKILL.md` — workflow instructions for ChatGPT/Codex.
- `references/site-contract.md` — design, HTML, index, and content conventions.
- `assets/article-template.html` — article structure reference.
- `scripts/validate_site.py` — lightweight HTML structure and local-link checker.

## Install and use

Where ChatGPT Skills are available: open **Skills → Create → Upload from your computer**, upload the ZIP package, review it, and install. Then invoke it with `@personal-site-article-maintainer` or allow ChatGPT to select it for relevant article work.

For Codex, place this directory under `.agents/skills/personal-site-article-maintainer/` in a project or `$CODEX_HOME/skills/personal-site-article-maintainer/` for a personal skill. Restart Codex if it does not detect the skill.

The skill expects the GitHub connection to be available for direct repository reads and writes. A skill provides workflow instructions; it does not grant repository permissions by itself.

## Safety

Committing article changes to `master` publishes the public website. Requests to draft content only produce a review draft; publish only when the user explicitly asks to update/add/publish the site.
