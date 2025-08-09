# 🏛️ Persona: The Architect

## The Order (Scenario)
You are a tech lead or senior developer responsible for the long-term health and consistency of the codebase. You need to enforce project standards (like Conventional Commits) and extend Gemini with custom tools that connect to your team's internal services.

## The Recipe (How it Works)
This example demonstrates two advanced capabilities:
1.  **Enforcing Standards:** The `/commit` command uses a prompt to guide the user in writing a Conventional Commit message.
2.  **Custom Tools:** The `/toggle-flag` command shows how Gemini can execute a local script, allowing it to interact with internal services like a feature flag API.

## On the Menu (Key Commands)
*   `/commit`: Generates a Conventional Commit message from your staged changes.
*   `/toggle-flag`: Executes a custom script to toggle a feature flag.