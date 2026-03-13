# ai-stacks

[![Repo PR Review](https://github.com/mtsanaissi/ai-stacks/actions/workflows/repo-pr-review.yml/badge.svg)](https://github.com/mtsanaissi/ai-stacks/actions/workflows/repo-pr-review.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

`ai-stacks` is a library of reusable AI-oriented project templates, skills, and repo-local tooling.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution expectations and [LICENSE](LICENSE) for licensing.

Support paths:
- [Issues](https://github.com/mtsanaissi/ai-stacks/issues)
- [Support guide](SUPPORT.md)
- [GitHub Sponsors](https://github.com/sponsors/mtsanaissi)
- [Buy Me a Coffee](https://buymeacoffee.com/mtsanaissi)

The repo serves two purposes:

- It stores scaffolding material for future AI-assisted projects, agent skills and tools.
- It acts as its own proof of concept for AI-friendly repository practices.

## Repository Structure

- `specs/`: standalone project-root templates for `common`, `typescript`, `nextjs`, `python`, and `powerbi`
- `skills/`: reusable agent skills, including `task-ledger`
- `tools/agent_docs/`: sync and validation scripts for `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`
- `tools/template_checks/`: shared template completeness checks
- `tools/mcp_server/`: local MCP server, setup docs, and smoke-test client
- `.agents/checks/`: vendor-neutral review criteria used by humans, agents, and workflows

## What Lives Here

This repo is not meant to host real application code.

Instead, it packages reusable project-starting material and repo-local support assets:

- `specs/` contains standalone stack templates meant to be copied into the root of a new project and customized there
- `skills/` contains reusable agent skills that can be inspected, adapted, and reused across projects
- `tools/` contains maintenance and validation utilities used to keep this repo and its templates consistent

The stack templates are intentionally standalone and do not depend on each other.

For repo-local usage, `skills/` is the canonical source and `.agents/skills/` is a managed mirror for only the skills listed in [.agents/skills/selected-skills.txt](.agents/skills/selected-skills.txt).

## Template Model

Each stack template should be:

- standalone
- copy-ready
- opinionated enough to be useful
- easy to trim after copying

Each stack is expected to include:

- `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`
- ignore rules
- pre-commit config
- `.agents/checks/`
- workflow templates
- stack-specific docs
- a local `README.md` with copy/update guidance

## Agent Files

Every folder that has agent instruction files follows this rule:

- `AGENTS.md` is the canonical source
- `CLAUDE.md` and `GEMINI.md` are synced from it
- provider-specific differences should stay limited to the title, intro, and `## Tool-Specific Notes`

Useful commands:

```bash
python3 tools/agent_docs/sync_agent_files.py
python3 tools/agent_docs/validate_agent_files.py
```

## Local Skill Sync

If you want selected repo-owned skills to be usable inside this repo, keep the source in `skills/` and list the enabled subset in [.agents/skills/selected-skills.txt](.agents/skills/selected-skills.txt).

Sync the selected skills into `.agents/skills/` with:

```bash
python3 tools/skills/sync_selected_skills.py
```

Check for drift without writing files:

```bash
python3 tools/skills/sync_selected_skills.py --check
```

## Template Validation

Template completeness checks are intentionally independent from the MCP server.

Useful command:

```bash
python3 tools/template_checks/validate_templates.py
```

## Local MCP Server

The repo includes a local MCP server for repo-specific operations such as:

- listing stacks
- comparing stack files
- checking template completeness
- rendering copy checklists
- validating all templates

Setup:

```bash
python3 -m venv tools/mcp_server/.venv
source tools/mcp_server/.venv/bin/activate
python3 -m pip install -r tools/mcp_server/requirements.txt
python3 tools/mcp_server/server.py
```

Smoke test:

```bash
python3 tools/mcp_server/test_client.py
```

More detail is in [README.md](tools/mcp_server/README.md).

## Pre-commit

The root [.pre-commit-config.yaml](.pre-commit-config.yaml) includes:

- basic file hygiene hooks
- agent-file alignment validation
- selected local skill sync validation
- template completeness validation

Typical setup:

```bash
python3 -m pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## GitHub PR Review Workflow

The repo includes a real PR review workflow at [.github/workflows/repo-pr-review.yml](.github/workflows/repo-pr-review.yml).

It has two layers:

1. deterministic validation
2. AI review with Gemini for substantive repo changes

The workflow validates:

- agent-file alignment
- selected local skill sync
- template completeness

The AI review focuses on:

- template drift
- contradictory instructions
- stale placeholders
- misaligned commands, docs, and manifests
- skill contract regressions

### Required GitHub Secret

Add this repository secret:

- `GEMINI_API_KEY`

Path:

- `Settings -> Secrets and variables -> Actions -> Secrets`

### Optional GitHub Variable

You can set the Gemini model without editing the workflow by adding this repository variable:

- `GEMINI_MODEL`

Recommended initial value:

- `gemini-2.5-flash-lite`

Path:

- `Settings -> Secrets and variables -> Actions -> Variables`

If no variable is set, the workflow already falls back to `gemini-2.5-flash-lite`.

### Manual Workflow Testing

The workflow also supports `workflow_dispatch`, so you can test it without opening a PR.

In GitHub:

1. Go to `Actions`
2. Open `Repo PR Review`
3. Click `Run workflow`
4. Optionally provide `review_paths`

Example `review_paths` input:

```text
AGENTS.md
specs/nextjs/README.md
tools/template_checks/core.py
```

The AI review step is skipped when:

- the PR is draft
- `GEMINI_API_KEY` is missing
- the change set is classified as mechanical only

Mechanical-only examples include:

- generated `CLAUDE.md` / `GEMINI.md` sync output
- workflow-only changes
- prompt-only changes
- root `.gitignore` or root `.pre-commit-config.yaml` changes

## Support

For bugs, broken docs, or workflow issues:

- [Open an issue](https://github.com/mtsanaissi/ai-stacks/issues)
- [Read the support guide](SUPPORT.md)

If you want to support ongoing maintenance:

- [GitHub Sponsors](https://github.com/sponsors/mtsanaissi)
- [Buy Me a Coffee](https://buymeacoffee.com/mtsanaissi)

## Current Focus

The repo is still being shaped. The main active directions are:

- improving stack templates so they are realistically copy-ready
- expanding reusable skills
- growing repo-local tooling and validation
- making the repo itself a strong example of AI-oriented development workflow
