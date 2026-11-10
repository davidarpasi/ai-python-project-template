# Python Project Template

I made this because I kept setting up the same tools whenever I started a Python project. It gives me a package layout, tests, linting, type checks and CI in one place.

The repository name still includes AI, but there is no AI dependency. I use the same setup for scripts, services and experiments.

## Create a project

Install Python 3.12+, [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/).

```bash
uvx copier copy --vcs-ref=main https://github.com/davidarpasi/ai-python-project-template.git my-service
cd my-service
uv sync
uv run pre-commit install
just check
```

Copier asks for the project and package names. `uv sync` creates the project's own lockfile; commit `uv.lock` before pushing so CI can use `uv sync --locked`.

The generated project is a starting point. Its command prints a ready message. It does not include an API, deployment, database or application logic.

## Work on the template

```bash
git clone https://github.com/davidarpasi/ai-python-project-template.git
cd ai-python-project-template
uv sync --locked
uv run pre-commit install
just check
```

`just check` runs Ruff, Basedpyright and pytest. The integration tests generate a project with different names, check that Copier saves its answers, and exercise an update from a temporary Git template. CI also installs, checks and builds a generated project.

## What is included

- A `src/` package layout and command-line entry point
- uv for environments and locked dependencies
- Ruff for formatting and linting
- Basedpyright for type checks
- pytest and coverage reporting
- Pre-commit hooks, enabled by running the install command above
- GitHub Actions and Dependabot configuration
- Short development notes and architecture decisions

Coverage is reported; there is no coverage percentage gate. I care more about testing useful behavior than making the greeting example score well.

## Updating a generated project

Commit your changes first, then run `uvx copier update --vcs-ref=main --overwrite` from the generated repository. Review the diff and resolve conflicts before committing the update. Keep `.copier-answers.yml`; Copier uses it to remember the source and answers.

MIT license.
