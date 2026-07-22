# Definition of Done

## Purpose

This document defines the minimum conditions that must be satisfied before the AI Python Project Template can be considered complete and ready for stable use.

A feature, milestone, or release is not complete merely because code has been written. It must also be tested, documented, reviewed, and reproducible.

## Repository Requirements

Every generated repository must contain:

* `README.md`
* `LICENSE`
* `.gitignore`
* `CHANGELOG.md`
* `docs/`
* `src/`
* `tests/`

Additional project infrastructure must be included when enabled by the generator.

## Project Generation

A new project must be generated in under two minutes under normal local conditions.

The generator must:

* validate project names and package names;
* create the expected directory structure;
* replace all template placeholders;
* avoid leaving template-specific names behind;
* support documented configuration options;
* produce a usable Git repository;
* support future template updates where technically possible.

## Python Environment

The generated project must:

* declare its supported Python version;
* use `pyproject.toml`;
* use `uv` for dependency management;
* include and commit `uv.lock`;
* install successfully from a clean environment;
* build successfully as a Python package.

## Code Quality

The generated project must include:

* Ruff linting;
* Ruff formatting;
* static type checking;
* Pytest;
* test coverage reporting;
* pre-commit hooks.

The authoritative local validation command must succeed:

```bash
make check
```

Local validation and CI must use equivalent underlying commands.

## Testing

Tests must:

* run successfully from a clean checkout;
* be deterministic;
* avoid external network access unless explicitly classified as integration tests;
* include at least one working example test;
* produce a clear failure when intentionally broken.

A defined minimum coverage threshold must be enforced.

## Configuration

Application configuration must:

* use typed settings;
* be loaded from environment variables;
* fail clearly when required configuration is invalid or missing;
* include a documented `.env.example`;
* avoid exposing secrets through logs or error messages.

Real `.env` files must be excluded from Git.

## Logging

Generated applications must:

* use centralized logging configuration;
* produce readable logs;
* support configurable log levels;
* include useful context in error logs;
* avoid logging credentials, tokens, private keys, or other secrets.

## Docker

When Docker support is enabled:

* the image must build successfully;
* dependencies must be installed reproducibly;
* the final image must run as a non-root user;
* unnecessary files must be excluded from the build context;
* secrets must not be embedded in the image;
* the container must start using the documented command.

## Continuous Integration

GitHub Actions must validate:

* formatting;
* linting;
* type checking;
* tests;
* coverage;
* package build;
* Docker build when Docker support is enabled.

Workflow permissions must follow least-privilege principles.

A deliberately broken change must fail CI for the expected reason.

## Security

The repository must:

* exclude secrets and local environment files;
* include security-reporting instructions;
* include automated dependency update configuration;
* avoid unnecessarily privileged containers and workflows;
* document any security-sensitive defaults.

## Documentation

Documentation must explain:

* project purpose;
* installation;
* development setup;
* available commands;
* configuration;
* testing;
* architecture;
* Docker usage when enabled;
* contribution workflow;
* security reporting.

Major architectural decisions must be recorded as Architecture Decision Records.

## Versioning and Release

Before the first stable release:

* the template must use semantic versioning;
* the changelog must describe the release;
* the repository must have a version tag;
* release notes must exist;
* at least one generated example project must be verified;
* the GitHub repository must be configured as a template repository.

## Independent Usability

Another developer must be able to:

1. generate a new project;
2. install dependencies;
3. run the application;
4. execute tests;
5. run all quality checks;
6. build the container when enabled;

without needing information that exists only in this chat.

## Milestone Completion

A milestone is complete only when:

1. its objective has been implemented;
2. verification commands pass;
3. Git changes have been reviewed;
4. documentation has been updated;
5. the change has been committed with a meaningful message;
6. the commit has been pushed to the remote repository.
