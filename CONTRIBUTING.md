# Contributing

Thanks for considering a contribution to `ai-stacks`.

This repository is still maintained in a fairly lightweight and informal way. The contribution process is real, but it is not highly polished yet: review turnaround may be inconsistent, issue triage is somewhat ad hoc, and contribution conventions are still evolving. It is better to state that directly than to pretend there is a mature OSS process here.

## Good Fits

Contributions are most useful when they improve:

- stack-template quality and copy readiness
- reusable skills
- repo-local validation and maintenance tooling
- documentation clarity and consistency
- drift reduction across `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`

## Before You Change Things

- Keep changes narrow and relevant.
- Prefer existing repo patterns over new abstractions.
- Avoid behavior-changing or user-visible assumptions unless they are clearly documented.
- When updating a stack template, keep it self-contained and do not make it depend on another folder in this repo.
- When changing shared expectations, check for drift across related agent files and docs.

## How To Contribute

1. Open an issue if the change is large, opinionated, or likely to affect multiple templates.
2. For smaller fixes, open a pull request directly.
3. Explain the problem being solved, not just the file edits.
4. Call out any tradeoffs, assumptions, or places where copy-after-edit guidance changed.

## Pull Request Notes

Please keep pull requests easy to review:

- separate unrelated work into different PRs
- mention any docs, template, or agent-file drift you checked
- include validation commands you ran
- note anything intentionally left out

## Validation

Use the lightest validation that matches the change:

- `python3 tools/agent_docs/validate_agent_files.py` after editing agent instruction files
- `python3 tools/skills/sync_selected_skills.py --check` to confirm enabled repo-local skills are mirrored correctly in `.agents/skills/`
- `python3 tools/template_checks/validate_templates.py` after changing stack template structure or required docs
- any targeted smoke test relevant to changed tooling

## Review Expectations

Review will usually focus first on:

- contradictions across docs and templates
- template drift
- unclear handoff or copy-after-edit instructions
- changes that make the repo less reusable or less inspectable

Because this is a small project, not every contribution will get immediate deep feedback. If a PR sits for a while, that is more likely to be maintainer bandwidth than a judgment on the change itself.

## License

By contributing to this repository, you agree that your contributions will be licensed under the MIT License in this repo.
