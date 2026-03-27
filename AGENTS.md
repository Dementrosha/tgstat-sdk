# AGENTS.md

## Rules

- Async only.
- Python 3.11+ only.
- Use Pydantic v2 models.
- Keep the public API resource-oriented.
- Keep the low-level API minimal.
- Split models by endpoint into separate files.
- Enforce snake_case in the Python API.
- Keep the architecture readable and maintainable.
- Align fields in Pydantic models by type and `=` where reasonable.
- Align all fields in all Pydantic models by type and by `=` consistently, even in short models.
- Align fields in dataclasses by type and by `=` consistently.
- Align Enum members consistently by `=` for readability.
- Apply the same alignment style to other declarative classes with field-like assignments where practical.
- Align parameters in all `__init__` method signatures consistently, including short constructors and keyword-only parameters with defaults.
- The user often uses Russian. Preserve Russian text correctly in UTF-8 and never introduce mojibake or broken Cyrillic in README, examples, comments, docstrings, or code strings.

## Architecture

- `client.py` is the entry point.
- `config.py` owns configuration objects.
- `transport.py` owns HTTP, retries, parsing, and error mapping.
- `resources/` owns grouped endpoint accessors.
- `models/` owns shared and endpoint-specific schemas.
- `exceptions.py` owns the error system.
