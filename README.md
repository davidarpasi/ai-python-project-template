# AI Python Project Template

A production-ready Python template for building AI applications, automation tools, APIs, and services using modern Python engineering practices.

The goal of this repository is to provide a consistent, high-quality starting point for new projects so that development can begin immediately without repeatedly configuring tooling, packaging, testing, and code quality.

---

## Features

* Modern Python packaging (`src/` layout)
* `uv` for dependency and environment management
* Ruff for linting and formatting
* Basedpyright for static type checking
* Pytest for testing
* Pre-commit hooks
* `just` task runner
* Architecture Decision Records (ADRs)
* Opinionated engineering standards
* Clean, atomic Git history

---

## Requirements

* Python 3.12 or newer
* `uv`
* `just`
* Git

---

## Getting Started

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

## Daily Workflow

Format the project:

```bash
just format
```

Run all quality checks:

```bash
just check
```

Run the test suite:

```bash
just test
```

Automatically fix formatting and lint issues where possible:

```bash
just fix
```

---

## Repository Structure

```text
.
├── docs/
│   ├── architecture.md
│   ├── development-standards.md
│   ├── definition-of-done.md
│   └── decisions/
├── src/
│   └── ai_python_project_template/
├── tests/
│   ├── integration/
│   └── unit/
├── pyproject.toml
├── justfile
└── README.md
```

---

## Quality Standards

Every change should satisfy the complete quality pipeline:

```bash
just check
```

This executes:

* Ruff (linting)
* Ruff (format validation)
* Basedpyright
* Pytest

Pre-commit hooks run automatically before each commit to enforce basic repository hygiene.

---

## Documentation

Additional documentation is available in the `docs/` directory:

* Architecture overview
* Engineering standards
* Definition of Done
* Architecture Decision Records (ADRs)

---

## Roadmap

Planned improvements include:

* GitHub Actions CI
* Dependabot
* Coverage reporting
* Copier template generation
* Release automation

---

## License

This project is licensed under the MIT License.
