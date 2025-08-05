# Persona: The Power User 🚀

## "Help me build sophisticated, reusable commands."

**Scenario:** You've mastered the basics of Gemini and now you want to bend it to your will. You want to create sophisticated, reusable, and shareable commands that encapsulate complex workflows, turning multi-step processes into a single, elegant command.

This persona is focused on leveraging the full power of slash commands, as detailed in the [Gemini CLI custom slash commands blog post](https://cloud.google.com/blog/topics/developers-practitioners/gemini-cli-custom-slash-commands).

---

## Understanding Slash Commands

Slash commands are user-defined shortcuts that execute a predefined series of instructions. They can range from simple one-line shell commands to complex, multi-step generative workflows. This allows you to create a library of reusable commands tailored to your project's specific needs.

### Ways to Define a Command

There are three primary ways to define a slash command:

1.  **Inline in `GEMINI.md`:** For simple, one-line commands.
    ```markdown
    - `/test`: Run all python tests.
      - `pytest`
    ```

2.  **Prompt File (`.md`):** For complex, multi-step generative prompts. The `>` symbol tells Gemini to use the content of the specified file as the prompt.
    ```markdown
    # In GEMINI.md
    - `/new-feature`: Launch a workflow to create a new feature.
      - `> .gemini/prompts/new_feature.md`
    ```

3.  **TOML Configuration File (`.toml`):** For commands with detailed configuration, such as a long description or default arguments.
    ```markdown
    # In GEMINI.md
    - `/plan`: > plan.toml
    ```
    ```toml
    # In plan.toml
    description="Investigates and creates a strategic plan to accomplish a task. Example: /plan How can I make the project more performant?"
    prompt = """
    Your primary role is that of a strategist...
    """
    ```

### Using Arguments & Advanced Context

You can make your commands dynamic by using arguments and other context variables.

-   `{{args}}`: Passes all arguments provided after the command as a single string.
-   `{{arg1}}`, `{{arg2}}`, etc.: Passes the Nth argument.
-   `{{selection}}`: Passes the text you have highlighted in your terminal.
-   `{{clipboard}}`: Passes the current content of your system clipboard.

**Example:** Create a `/explain` command that uses the `{{selection}}` variable.
```markdown
- /explain: Explain the following code.
  - `{{selection}}`
```
Now you can highlight a block of code in your terminal and type `/explain` to get an explanation.

### Adding File Context from the Command Line
For one-shot prompts, you can add the content of a file to the context using the `--context-from-file` flag. This is a convenient alternative to using `cat` and a pipe.

`g -p "Summarize this file" --context-from-file long_document.md`

### Hierarchical Naming

For better organization, you can group related commands using a colon (`:`). This creates a command namespace.

-   `/git:commit`: A command for committing changes.
-   `/git:push`: A command for pushing changes.
-   `/git:rebase`: A command for rebasing the current branch.

---

This example demonstrates several of these advanced techniques, showing how slash commands can transform Gemini from a helpful assistant into a powerful, programmable platform for any development task.

## Command Reference

Here is a list of helpful slash commands, combining general-purpose utilities with the specific commands created for this persona.

| Command | Description | Definition File |
| :--- | :--- | :--- |
| `/explain` | Explains the highlighted code selection. | Inline in `GEMINI.md` |
| `/test` | Runs tests against the codebase. | Inline in `GEMINI.md` |
| `/lint` | Lints the codebase to check for style issues. | Inline in `GEMINI.md` |
| `/commit` | Generates a Conventional Commit message based on staged changes. | `prompts/conventional_commit.md` |
| `/new-feature` | Kicks off a workflow to create a new feature file. | `prompts/new_feature.md` |
| `/planing` | Creates a high-level strategic plan to accomplish a task. | `planing.toml` |
| `/plan:new` | Generates a detailed, step-by-step implementation plan for a new feature. | `plan/new.toml` |
| `/plan:impl` | Executes a feature implementation based on a pre-existing plan file. | `plan/impl.toml` |
| `/git:fix` | Generates a code fix for a given GitHub issue based on staged changes. | `.gemini/commands/git/fix.toml` |
| `/git:review` | Performs a detailed review of a pull request using the `gh` CLI. | `.gemini/commands/git/review.toml` |
