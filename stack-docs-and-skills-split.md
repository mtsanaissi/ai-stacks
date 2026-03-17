# Stack Docs And Skills Split

Use this document to keep stack templates, agent instructions, and repo-owned skills aligned.

## Goal

Separate stack project-template conventions from deep agent operating guidance so copied specs stay useful for humans and agents load detailed stack behavior only when needed.

## Decisions

- Treat each stack skill as the primary agent-facing source for deep implementation guidance.
- Keep one primary skill per stack by default: `nextjs`, `python`, `typescript`, `powerbi`.
- Store deep specifics in `skills/<stack>/references/`.
- Keep `specs/*/AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` thin. They should route to the stack skill when available and keep only always-hot guardrails.
- Treat `specs/*/docs/` as the canonical project-template conventions for that stack.
- Keep `specs/*/docs/` copy-ready so a copied template still works even when the repo skill is unavailable.

## Responsibilities

### `skills/<stack>/SKILL.md`

- Define trigger rules for when the stack skill should be used.
- Define the workflow for inspecting versions, reading targeted references, implementing, validating, and reporting risk.
- Define which reference files to load for each task shape.
- Call out common AI-agent failure modes for that stack.

### `skills/<stack>/references/`

- Hold the deep stack-specific material for agents.
- Prefer small, task-shaped files over one large reference.
- Typical files:
  - `task-routing.md`
  - `security-rules.md`
  - `validation-matrix.md`
  - stack-specific boundary or review hotspot guides

### `specs/*/AGENTS.md`, `CLAUDE.md`, `GEMINI.md`

- Keep commands and a short scope section.
- Tell the agent to use the relevant stack skill when available and applicable.
- Keep only minimal, always-hot rules such as:
  - ask before auth, secret, deployment, or data-boundary changes
  - do not invent framework APIs or version-specific behavior
  - keep validation explicit
- Do not duplicate the full stack handbook.

### `specs/*/docs/`

- Stay useful as standalone template docs for teams adopting the stack.
- Act as the canonical source for project-template conventions, not as the deep agent playbook.
- Cover things such as:
  - folder and module structure
  - naming conventions
  - commenting and docstring rules
  - recommended project documentation
  - placeholders or kickoff templates for recommended docs
  - testing, config, and handoff conventions that a new project should inherit
- Remain thinner than the skill references.
- Do not assume the reader has the repo-local skill installed.

## Source Of Truth

- `skills/<stack>/references/` is the canonical source for deep agent operating guidance.
- `specs/*/docs/` is the canonical source for project-template conventions.
- `specs/*/AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` are routing layers with only minimal always-hot rules.

## Default Skill Shape

Each stack skill should include:

- Trigger contract
- Non-trigger cases
- Task router for which references to load
- Workflow
- Validation contract
- Output expectations

Each stack skill should avoid:

- Repeating entire framework manuals in `SKILL.md`
- Splitting into action-specific skills such as `read`, `write`, `review`, or `test`
- Depending on `specs/*/docs/` as the canonical deep source

## When To Split A Stack Into More Than One Skill

Do not split by action.

Split only when there is a real difference in:

- trigger language
- references loaded
- workflow
- output contract

Good later examples:

- `nextjs` and `nextjs-security-review`
- `powerbi-modeling` and `powerbi-governance`

If those differences are not clear, keep one skill.

## Naming And Layout

Use this layout for repo-owned stack skills:

```text
skills/
  <stack>/
    SKILL.md
    references/
      task-routing.md
      validation-matrix.md
      ...
```

Use this layout for stack spec folders:

```text
specs/
  <stack>/
    AGENTS.md
    CLAUDE.md
    GEMINI.md
    docs/
      ...
```

## Rollout Rules

- Edit the skill first when changing deep stack guidance.
- Edit stack spec docs first when changing project-template conventions.
- Keep spec docs intentionally shorter than skill references, but substantial enough to guide a new project kickoff.
- If a repo-owned skill is added, keep `.agents/skills/selected-skills.txt` and mirrored copies aligned with the sync mechanism.
- Do not make a copied spec depend on repo-local skills for correctness or safety.
- Validation for rollout work should include agent-file alignment, skill sync consistency, and template validation.
