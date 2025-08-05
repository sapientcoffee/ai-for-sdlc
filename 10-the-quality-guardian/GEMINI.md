# Gemini Cookbook: The Quality Guardian

# These commands assist in the code review lifecycle, for both the
# author preparing the code and the teammate reviewing it.

## Slash Commands

# --- Author's Pre-Flight Check ---
- `/review:local`: Reviews your staged code changes against the project's style guide.
  - `> cat .gemini/styleguide.md`
  - `> git diff --staged`
  - `You are a senior software engineer performing a pre-flight code review. Your task is to check the staged code changes (the second block of text) against our project's style guide (the first block of text).`
  - `Please list any violations you find. If there are no violations, simply say "No violations found."`

# --- Reviewer's PR Workflow ---
- `/review:summarize`: Get a high-level summary of the changes in the current branch.
  - `> git diff --unified=0`
  - `Based on the diff above, provide a high-level summary of the changes.`

- `/review:check`: Check the code in the current branch for common issues.
  - `> git diff`
  - `You are a senior software engineer performing a code review. Analyze the diff above and check for the following common issues:`
  - `- Are there any obvious bugs or logic errors?`
  - `- Is the code well-documented with comments and docstrings?`
  - `- Are there corresponding unit tests for the new code?`
  - `- Are variable and function names clear and self-explanatory?`
  - `Provide your feedback in a bulleted list.`

- `/review:comment`: Generate a template for a code review comment.
  - `> git diff`
  - `Based on the diff above, I need to leave a code review comment about "{{arg1}}".`
  - `Please draft a polite and constructive comment that explains the issue and suggests a potential improvement.`