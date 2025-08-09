# 🔌 Persona: The Integrator

## The Order (Scenario)
Your team has a whole ecosystem of internal tools: a feature flag API, a deployment service, a custom metrics database. You want to extend Gemini's capabilities by connecting it to these services, creating a seamless bridge between the AI assistant and your team's unique environment.

## The Recipe (How it Works)
This is achieved by creating a tool that follows the **Model Context Protocol (MCP)**. This persona shows how to create a simple MCP server (a Python script) that Gemini can execute. The script performs a custom action and prints a result to standard output, which Gemini then injects back into the prompt as context.

## On the Menu (Key Commands)
*   `/add-note`: Adds a note to an internal notes service by running a local Python script.