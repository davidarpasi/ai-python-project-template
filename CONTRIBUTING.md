# Contributing

Install Python 3.12+, uv and just. Run `uv sync --locked`, then `uv run pre-commit install`.

Create a branch, make a focused change and run `just check`. If it changes generated files, update `template/` and check a newly generated project as well.

Include the problem, the change and how you tested it in the pull request. Do not include real credentials or private logs in examples.
