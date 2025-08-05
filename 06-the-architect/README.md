# Persona: The Architect 🏛️

## "Help me enforce standards and build custom tools."

**Scenario:** You are a tech lead or senior developer. Your role goes beyond writing code; you are responsible for the long-term health and consistency of the codebase. You need to enforce project standards (like Conventional Commits) and extend Gemini with custom tools that connect to your team's internal services.

This example demonstrates the most advanced capabilities:
1.  **Enforcing Standards:** The `/commit` command uses a prompt to guide the user (or Gemini) in writing a Conventional Commit message, ensuring all commits adhere to the project's standard.
2.  **Custom Tools:** The `/toggle-flag` command shows how Gemini can be extended with custom tools. This command executes a Python script that could, for example, interact with an internal feature flag API.

This allows a team to deeply integrate Gemini into their specific development ecosystem, enforcing standards and connecting it to proprietary tools.
