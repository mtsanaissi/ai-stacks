# Memory Skill

`memory` is a reusable agent skill for capturing and recalling durable project knowledge across sessions.

It is designed for moments like:

- "Add this to memory"
- "Remember how we solved this"
- "Save this workaround for future sessions"
- "Keep this lesson learned"

The skill stores reusable knowledge in `docs/memory/` as one Markdown file per atomic memory plus a generated `_index.md`. That structure keeps entries easy to review, update, diff, and selectively recall without turning the memory store into one large noisy document.

## What It Covers

- Recall relevant memory before non-trivial work
- Capture reusable lessons, workflows, decisions, facts, and constraints
- Decide between creating a new memory and updating an existing one
- Keep memory concise and operational instead of narrative

## Storage Shape

The default layout is:

```text
docs/memory/
├── _index.md
├── some-memory-card.md
└── another-memory-card.md
```

This skill intentionally does not default to:

- a single `docs/memory.md` file, because it scales poorly for recall and updates
- bucket subfolders, because they add structure before there is enough content to justify it

## Included Files

- `SKILL.md`: trigger contract, recall/capture workflow, validation rules
- `references/card-template.md`: canonical template for memory cards
- `references/index-template.md`: canonical template for `_index.md`

## Inspirations

This skill draws ideas from two source skills, adapted for a model-agnostic repo workflow:

- [memory-management](https://skills.sh/anthropics/knowledge-work-plugins/memory-management)
- [lessons-learned](https://skills.sh/shihyuho/skills/lessons-learned)

From `memory-management`, it borrows the emphasis on durable file organization and templates.

From `lessons-learned`, it borrows the explicit recall/capture phases, create-vs-update discipline, and the idea that reusable memory capture is a non-replaceable step.
