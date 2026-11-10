# Development notes

Keep changes small enough to review. Add type hints to public Python functions and test behavior that could break. Run `just check` before committing.

When changing generated files, update the matching file under `template/` and check a generated project too. Keep dependencies in `pyproject.toml` and commit the updated lockfile.

Do not commit credentials, real customer data or internal logs. Use fictional fixtures. Record an architecture decision when there is a meaningful choice to explain.
