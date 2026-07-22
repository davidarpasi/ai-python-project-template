# ADR-0001: Use `uv` for Python Management

**Status:** Accepted

## Context

The project requires a single tool for:

* Python version management
* virtual environments
* dependency management
* lockfiles
* package installation
* running commands
* package building

Historically, these responsibilities have often been split across multiple tools, increasing complexity and maintenance overhead.

## Decision

Use **uv** as the standard Python project manager for every repository generated from this template.

All generated projects will:

* use `uv` for dependency management;
* commit `uv.lock`;
* execute commands through `uv run`;
* avoid introducing additional package managers unless there is a project-specific requirement.

## Consequences

### Benefits

* Fast dependency resolution.
* Modern Python workflow.
* Reduced tooling complexity.
* Excellent reproducibility.
* Single primary interface for Python projects.

### Trade-offs

* Developers unfamiliar with `uv` must learn a new workflow.
* Some legacy tutorials assume `pip` or Poetry.

These trade-offs are acceptable because the long-term maintenance benefits outweigh the initial learning cost.
