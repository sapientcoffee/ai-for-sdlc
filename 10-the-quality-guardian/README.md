# 🛡️ Persona: The Quality Guardian

## The Order (Scenario)
As a "Quality Guardian," you are responsible for the quality of the codebase. This has two phases: the **Author's Pre-flight Check** (running a self-review before creating a PR) and the **Reviewer's Workflow** (reviewing a teammate's PR).

## The Recipe (How it Works)
This persona demonstrates how Gemini can be used as an assistant in both phases of the code review lifecycle. It uses a project `styleguide.md` to perform a local review, and provides commands to summarize changes, check for common issues, and draft review comments, making the entire process faster and more effective.

## On the Menu (Key Commands)
*   `/review:local`: Reviews your staged code changes against the project's style guide.
*   `/review:summarize`: Gets a high-level summary of the changes in the current branch.
*   `/review:check`: Checks the code for common issues like bugs or missing tests.
*   `/review:comment`: Helps you draft a polite and constructive code review comment.
