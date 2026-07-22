# Contributing

Thank you for contributing to this project.

The goal of this repository is to provide a production-ready Python template for AI and automation projects while maintaining consistent engineering standards.

---

## Development Setup

Clone the repository:

```bash
git clone https://github.com/davidarpasi/ai-python-project-template.git
cd ai-python-project-template
```

Install dependencies:

```bash
uv sync
```

Verify the environment:

```bash
just check
```

---

## Development Workflow

1. Create a feature branch.
2. Make a small, focused change.
3. Run the complete quality pipeline:

```bash
just check
```

4. Commit using a descriptive, atomic commit message.
5. Open a Pull Request.

---

## Code Quality

Every contribution must pass:

* Ruff linting
* Ruff formatting
* Basedpyright
* Pytest
* Pre-commit hooks

These are available through:

```bash
just check
```

Pre-commit hooks run automatically before each commit.

---

## Coding Standards

* Follow PEP 8 unless project tooling specifies otherwise.
* Prefer explicit, readable code over clever implementations.
* Add type hints to new code.
* Keep functions small and focused.
* Write tests for new behavior.
* Update documentation when behavior changes.

---

## Commit Guidelines

Keep commits:

* Atomic
* Descriptive
* Focused on a single logical change

Examples:

```text
build: add GitHub Actions workflow
docs: update architecture overview
feat: add OpenAI client wrapper
fix: handle missing configuration
test: add API client unit tests
```

---

## Architecture Decisions

Significant engineering decisions should be documented as Architecture Decision Records (ADRs) under:

```text
docs/decisions/
```

---

## Questions

If you're unsure about a change, prefer discussing the design before implementing a large feature.
