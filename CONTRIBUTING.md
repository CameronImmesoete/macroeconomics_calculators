# Contributing

This is a solo project maintained by [@CameronImmesoete](https://github.com/CameronImmesoete).

## Getting Started

```bash
# Clone the repository
git clone https://github.com/CameronImmesoete/macroeconomics_calculators.git
cd macroeconomics_calculators

# Install dependencies
uv sync

# Run tests
uv run pytest

# Run linting
uv run ruff check .

# Run type checking
uv run mypy .
```

## Development Workflow

1. Create a feature branch from `main`
2. Make your changes
3. Run the full test and lint suite
4. Open a draft PR against `main`
5. All PRs require squash merge

## Code Style

- Python 3.11+
- Formatting and linting via [Ruff](https://docs.astral.sh/ruff/)
- Type hints encouraged; checked via [mypy](https://mypy-lang.org/)
- Pre-commit hooks enforce style on commit

## Reporting Issues

Use the GitHub issue templates for bug reports and feature requests.
