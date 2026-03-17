# ai-stacks

[![Repo Validation](https://github.com/mtsanaissi/ai-stacks/actions/workflows/repo-validation.yml/badge.svg)](https://github.com/mtsanaissi/ai-stacks/actions/workflows/repo-validation.yml)
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
- `tools/agent_docs/`: validation scripts and guidance for canonical `AGENTS.md` files
- `tools/template_checks/`: shared template completeness checks
- `tools/mcp_server/`: local MCP server, setup docs, and smoke-test client
- `.continue/checks/`: vendor-neutral review criteria used by humans, agents, and workflows

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

- `AGENTS.md` as the checked-in canonical agent file
- ignore rules
- pre-commit config
- `.continue/checks/`
- starter workflow templates
- stack-specific docs
- a local `README.md` with copy/update guidance

Starter manifests, workflows, and review prompts are templates, not finished integrations. Copying teams are expected to replace placeholder values, commands, and workflow steps before relying on them.

## Agent Files

Every folder that has agent instruction files follows this rule:

- `AGENTS.md` is the only checked-in canonical instruction file in this repo
- copied templates may optionally copy or rename `AGENTS.md` to another entrypoint filename in the destination repo if a tool expects it
- stack templates should stay standalone and avoid implying one package manager, repo shape, or deployment target unless the file clearly marks it as a starter default

Useful commands:

```bash
python3 tools/agent_docs/validate_agent_files.py
```

## Local Skill Sync

If you want selected repo-owned skills to be usable inside this repo, keep the source in `skills/` and list the enabled subset in [.agents/skills/selected-skills.txt](.agents/skills/selected-skills.txt).

This repository intentionally mirrors only a small repo-operating subset there by default; stack-specific skills can remain repo-owned and unselected unless the manifest is deliberately expanded.

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
- canonical agent-file validation
- selected local skill sync validation
- template completeness validation

Typical setup:

```bash
python3 -m pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## GitHub Workflows

The repo includes a standalone validation workflow at [.github/workflows/repo-validation.yml](.github/workflows/repo-validation.yml).

The validation workflow runs deterministic checks for tracked repo changes on:

- pull requests
- pushes to the default branch (`main`)
- manual `workflow_dispatch`

It validates:

- canonical agent-file rules
- selected local skill sync
- template completeness

Repo-specific AI PR review is intentionally not enabled in this repository.

To run validation manually in GitHub:

1. Go to `Actions`
2. Open `Repo Validation`
3. Click `Run workflow`

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
