# Gemini Cookbook: The Architect

This project uses Conventional Commits.

## Slash Commands
- `/commit`: Generate a conventional commit message.
  - `> .gemini/prompts/conventional_commit.md`
- `/toggle-flag`: Toggle a feature flag using our internal service.
  - `> python .gemini/server/main.py --toggle {{arg1}}`
