# Gemini Cookbook: The Power User

This `GEMINI.md` showcases advanced, multi-step slash commands inspired by the [Gemini CLI custom slash commands blog post](https://cloud.google.com/blog/topics/developers-practitioners/gemini-cli-custom-slash-commands).

## Slash Commands

# --- 1. Basic Commands & Chaining ---
# Define a basic, reusable command to run tests in a specific directory.
- `/test`: Run python tests in a given directory.
  - `pytest {{arg1}}`

# Create a "meta" command that chains the basic /test command to run all tests.
- `/test-all`: Run all test suites.
  - `> /test src`
  - `> /test utils`

# --- 2. Interactive Feature Creation ---
# Use a prompt file to guide an interactive workflow for creating a new feature.
- `/new-feature`: Launch a workflow to create a new feature.
  - `> .gemini/prompts/new_feature.md`

# --- 3. Context-Aware Refactoring ---
# Find all python files and then ask the user which one to refactor.
- `/refactor`: Refactor a Python file.
  - `> find . -name "*.py"`
  - `Here are the project's Python files. Which one would you like to refactor?`
  - `> read_file {{response[2]}}`
  - `How would you like to refactor this file?`

# --- 4. Automated Commit Messages ---
# Use the git diff as context to generate a conventional commit message.
- `/conventional-commit`: Generate a conventional commit message from the git diff.
  - `> git diff`
  - `> .gemini/prompts/conventional_commit.md`