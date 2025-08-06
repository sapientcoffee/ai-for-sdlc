# Persona: The Daily Developer 👨‍💻

## "Help me work with existing code, but faster."

**Scenario:** You're in the zone, deep in the daily rhythm of coding. You're fixing bugs, adding small features, and you need an assistant that already knows the project's landscape. You don't want to leave your terminal, and you definitely don't want to repeat yourself.

This persona shows how to turn Gemini into your ultimate coding partner by creating shortcuts for common tasks and workflows.

---

## Your Command Palette: Slash Commands ⚡️

Slash commands are your personal command palette for the project. They let you condense long, repetitive commands into short, memorable aliases.

This example introduces some foundational commands:
- `/test`: To run the entire test suite.
- `/lint`: To check your code for style issues.
- `/explain`: To get a clear explanation of highlighted code.

This makes Gemini a context-aware assistant that streamlines your development flow.

## Pro-Tip: One-Shot Prompts 🎯

For quick questions where you don't need a long conversation, you can use the `-p` flag to send a "one-shot" prompt directly from your command line.

`g -p "What's the syntax for a list comprehension in Python?"`

This is perfect for quick lookups and can be easily integrated into scripts.

## Building Better Commands 🛠️

While you can define simple commands directly in `GEMINI.md`, more complex workflows benefit from a more structured approach.

### External Prompt Files (`> file.md`)
For multi-line or complex prompts, you can move them into a separate `.md` file. This keeps your `GEMINI.md` clean and makes your prompts reusable.

-   **`GEMINI.md`:**
    ```markdown
    - /new-feature: > .gemini/prompts/new_feature.md
    ```

### TOML Configuration (`> file.toml`)
For the most advanced commands, use a `.toml` file to add a description, which will appear in the `/help` menu.

-   **`GEMINI.md`:**
    ```markdown
    - /plan: > .gemini/prompts/plan.toml
    ```

---
## Advanced Example: A Structured System Prompt

For a more detailed look at how to structure a complex system prompt with personas, rules, and few-shot examples, check out our advanced guide.

➡️ **[View the Structured System Prompt Example](./structured-prompt-example.md)**


## Examples

GEMINI.md
The `GEMINI-TRACKING.md` file contains a robust logging protocol inspired by [Aaron Wanjala](https://medium.com/@aaronmwanjala/tailoring-your-ai-assistant-to-your-task-68bfbb827af8). It creates a transparent, auditable trail of the steps Gemini CLI takes to fulfill requests. This allows the agent to be interrupted—by quota restrictions, the end of the workday, etc.—and then pick up right where it left off, which is especially helpful for long-running, complex tasks.