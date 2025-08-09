# 🚀 Persona: The Power User

## The Order (Scenario)
You've mastered the basics of Gemini and now you want to bend it to your will. You want to create sophisticated, reusable, and shareable commands that encapsulate complex workflows, turning multi-step processes into a single, elegant command.

## The Recipe (How it Works)
This persona is focused on leveraging the full power of slash commands, from simple aliases to complex, multi-step generative workflows using prompt files and TOML configuration for detailed descriptions. It also shows how to use arguments (`{{arg1}}`) and context variables (`{{selection}}`) to make commands dynamic.

## On the Menu (Key Commands)
*   `/test-all`: A "meta" command that chains other commands to run all test suites.
*   `/refactor`: An interactive command that finds all Python files and asks you which one to refactor.
*   `/conventional-commit`: A command that uses your `git diff` as context to generate a commit message.