# Macroeconomics Calculators - Agent Guidelines

## Repository Overview

A collection of macroeconomics calculators in Python covering IS-LM, AD-AS, Phillips Curve, GDP, inflation, unemployment, fiscal multiplier, exchange rate, interest rate, and balance of payments models.

## Code Conventions

- **Language:** Python 3.11+
- **Dependencies:** numpy, matplotlib (for plotting calculators); stdlib-only for simple calculators
- **Style:** Ruff for formatting and linting, mypy for type checking
- **Pattern:** Each calculator is a standalone script with `argparse` CLI interface and a `main()` entry point

## Testing

```bash
uv run pytest           # Run tests
uv run ruff check .     # Lint
uv run mypy .           # Type check
```

## PR Guidelines

- All PRs target `main` via squash merge
- Use the PR template in `.github/pull_request_template.md`
- Include test coverage for new calculator functions
- PR titles should be clear, human-readable summaries

## Structure

Each calculator follows the pattern:
- Pure calculation functions (testable without CLI)
- Optional plotting via matplotlib
- CLI interface via argparse in `main()`

## Security

- No secrets or credentials in code
- No external API calls; all calculations are local
