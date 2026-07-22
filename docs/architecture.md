# Architecture

## 1. Purpose

The AI Python Project Template is a reusable engineering foundation for building production-ready Python and AI applications.

Its purpose is to make it possible to create a new project with consistent structure, tooling, documentation, testing, automation, and deployment foundations in under two minutes.

This repository is both:

* a GitHub template repository;
* a Copier-based project generator.

It is not an AI application itself. It provides the infrastructure that future AI applications will inherit.

## 2. Goals

The template must:

* provide a consistent Python project structure;
* enforce code quality locally and in CI;
* support reproducible dependency installation;
* provide typed configuration and safe environment-variable handling;
* include testing, logging, documentation, and containerization;
* minimize setup work for future projects;
* remain understandable to engineers who did not build the template;
* support controlled evolution through versioned releases;
* allow generated projects to receive future template updates.

## 3. Non-goals

The initial version will not include:

* cloud-provider-specific infrastructure;
* Kubernetes configuration;
* Terraform modules;
* automatic production deployment;
* model-provider-specific integrations;
* database-specific implementations;
* complex documentation frameworks;
* unnecessary duplication between tools.

These capabilities may be added to individual projects when required.

## 4. Design Principles

### 4.1 Repository-first knowledge

Important decisions, standards, and operating instructions must be documented in the repository. Critical knowledge must not exist only in chat messages or developer memory.

### 4.2 Reproducibility

The same project revision should behave consistently across:

* local Ubuntu development;
* another developer's machine;
* GitHub Actions;
* Docker.

Dependencies will be locked and CI will use frozen installations.

### 4.3 Explicit configuration

Application configuration must be:

* defined in one clear location;
* validated at startup;
* typed where practical;
* supplied through environment variables;
* documented in `.env.example`.

Secrets must never be committed to Git or embedded in container images.

### 4.4 Fast feedback

Developers should detect formatting, linting, typing, and test failures before pushing code.

Local checks and CI checks should use the same underlying commands.

### 4.5 Minimal tool overlap

Each tool should have a clear responsibility. Tools that duplicate functionality without providing meaningful value should not be added.

### 4.6 Secure defaults

Generated projects should use safe defaults, including:

* non-root Docker execution;
* least-privilege GitHub Actions permissions;
* no committed secrets;
* pinned or locked dependencies;
* automated dependency updates;
* clear security-reporting instructions.

### 4.7 Incremental complexity

The template should provide a strong foundation without forcing infrastructure that every project may not need.

Optional features should be enabled through generator parameters where appropriate.

## 5. Technology Decisions

| Area                             | Selected technology             |
| -------------------------------- | ------------------------------- |
| Python and dependency management | uv                              |
| Project configuration            | pyproject.toml                  |
| Build backend                    | Hatchling                       |
| Project generator                | Copier                          |
| Source layout                    | src layout                      |
| Linting                          | Ruff                            |
| Formatting                       | Ruff Formatter                  |
| Type checking                    | Basedpyright                    |
| Testing                          | Pytest                          |
| Coverage                         | pytest-cov                      |
| Git hooks                        | pre-commit                      |
| Runtime configuration            | Pydantic Settings               |
| Logging                          | Python standard library logging |
| Containers                       | Docker and Docker Compose       |
| Continuous integration           | GitHub Actions                  |
| Dependency updates               | Dependabot                      |
| Developer commands               | Makefile                        |

Detailed rationale for significant choices is recorded under `docs/decisions/`.

## 6. Repository Structure

The template repository will evolve toward the following structure:

```text
.
├── .github/
│   ├── workflows/
│   ├── dependabot.yml
│   ├── pull_request_template.md
│   └── ISSUE_TEMPLATE/
├── .vscode/
├── docs/
│   ├── decisions/
│   ├── architecture.md
│   ├── configuration.md
│   ├── development.md
│   └── operations.md
├── src/
├── tests/
│   ├── integration/
│   └── unit/
├── .dockerignore
├── .editorconfig
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── SECURITY.md
├── compose.yaml
├── pyproject.toml
└── uv.lock
```

Generated projects will replace template placeholders with project-specific names and metadata.

## 7. Architectural Layers

### 7.1 Developer interface

Developers will interact with the project through a small, consistent command surface:

```bash
make install
make format
make lint
make typecheck
make test
make check
make run
make docker-build
```

The Makefile will delegate to the underlying tools rather than contain complex application logic.

### 7.2 Package foundation

Python source code will live under:

```text
src/<package_name>/
```

Tests will import the installed package rather than accidentally importing files directly from the repository root.

### 7.3 Runtime foundation

Generated projects will include:

* a minimal executable entry point;
* typed settings;
* centralized logging configuration;
* clear exception boundaries;
* configuration validation;
* environment-variable documentation.

### 7.4 Quality gates

The authoritative project validation command will be:

```bash
make check
```

It will eventually include:

* formatting validation;
* linting;
* type checking;
* unit tests;
* coverage validation;
* package build validation.

Pre-commit hooks will provide fast local feedback. GitHub Actions will remain the authoritative merge gate.

### 7.5 Container runtime

The Docker template will:

* use a multi-stage build;
* install locked dependencies;
* run as a non-root user;
* exclude unnecessary files from the build context;
* avoid embedding secrets;
* provide a standard runtime entry point.

### 7.6 Project generation

Copier will generate projects using answers such as:

* project name;
* Python package name;
* description;
* minimum Python version;
* application or library;
* Docker support;
* security workflow support;
* license type.

Generator inputs must be validated to prevent invalid package names or unsafe output.

## 8. Documentation Standards

Every generated repository must contain:

* `README.md`;
* `LICENSE`;
* `.gitignore`;
* `CHANGELOG.md`;
* `docs/`;
* `src/`;
* `tests/`.

Documentation must explain:

* how to install the project;
* how to run it;
* how to test it;
* how configuration works;
* how the architecture is organized;
* how to build and run the container;
* how to contribute;
* how to report security issues.

Major architectural decisions must be recorded as Architecture Decision Records.

## 9. Project Lifecycle

Each milestone follows this workflow:

1. Define the objective.
2. Explain why it matters.
3. Implement the smallest coherent change.
4. Verify the implementation.
5. Review the Git diff.
6. Commit with a meaningful message.
7. Update documentation.
8. Record lessons or architectural decisions where appropriate.

## 10. Definition of Done

The first stable release is complete when:

* a new project can be generated in under two minutes;
* all mandatory repository files are created;
* dependencies are locked;
* local quality checks pass;
* GitHub Actions passes;
* the Python package builds successfully;
* Docker builds successfully;
* the container runs as a non-root user;
* configuration is typed and validated;
* secrets are excluded from Git and container images;
* documentation covers development, configuration, architecture, and operations;
* the template has a versioned release;
* generated projects can receive future template updates;
* another engineer can use the template without relying on this chat.

## 11. Evolution Strategy

The template will use semantic versioning.

Changes will be classified as:

* patch: fixes or documentation improvements that do not alter generated project behavior significantly;
* minor: backward-compatible features or new optional capabilities;
* major: breaking changes to structure, commands, configuration, or update behavior.

The template should remain conservative. New tools will be added only when they solve a demonstrated problem and provide more value than maintenance cost.
