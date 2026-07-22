# ADR-0002: Use the `src` Layout

## Status

Accepted

## Context

Python projects can place importable packages directly in the repository root or under a dedicated `src/` directory.

A flat layout is initially simpler, but it can allow tests and development commands to import code directly from the repository instead of from the installed package. This can hide packaging errors and create differences between local development and production installations.

This repository is intended to serve as a reusable foundation for production-grade Python and AI projects. It therefore needs a structure that validates packaging behavior and scales cleanly as the codebase grows.

## Decision

All importable Python packages will be placed under the `src/` directory.

The primary package currently lives at:

```text
src/ai_python_project_template/
```

Tests will import the package from the environment created and managed by `uv`.

Pytest will not modify `PYTHONPATH` or inject `src/` directly into the import path.

## Consequences

### Positive

* Tests exercise the installed package rather than importing directly from the repository root.
* Packaging configuration errors are more likely to be detected during development.
* Application code is clearly separated from tests, documentation, configuration, and repository tooling.
* The structure scales well for larger applications and multiple internal packages.
* The layout follows modern Python packaging guidance.

### Negative

* The package must be installed before it can be imported.
* Packaging configuration is required earlier in the project lifecycle.
* Developers unfamiliar with the `src/` layout may initially find it less intuitive.

## Alternatives Considered

### Flat package layout

Example:

```text
ai_python_project_template/
tests/
```

Rejected because local imports can succeed even when the package is not installed correctly.

### Application code inside a generic directory

Example:

```text
app/
tests/
```

Rejected because it does not provide the same packaging guarantees and is less conventional for reusable Python packages.

## Verification

The decision is verified when the following commands succeed:

```bash
uv sync
uv run python -c "import ai_python_project_template"
uv run pytest
```
