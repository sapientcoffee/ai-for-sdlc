# Persona: The Integrator 🔌

## "Help me connect Gemini to our custom tools."

**Scenario:** Your team has a whole ecosystem of internal tools: a feature flag API, a deployment service, a custom metrics database. You want to extend Gemini's capabilities by connecting it to these services, creating a seamless bridge between the AI assistant and your team's unique environment.

This is achieved by creating a tool that follows the **Model Context Protocol (MCP)**.

---

## What is the Model Context Protocol (MCP)?

The **Model Context Protocol (MCP)** is an open protocol that standardizes how applications provide context—such as tools, resources, or prompts—to large language models (LLMs).

For our purposes as integrators, the **tools** aspect is the most important. MCP defines a contract for how Gemini can discover and execute custom tools that you create.

It's important to distinguish between the protocol and its implementation:
*   **MCP is the protocol:** It defines the "rules of communication."
*   **An MCP Server/Tool is the implementation:** This is the actual script or service that Gemini runs. It can be a simple local process that communicates with Gemini through standard I/O (like the example in this directory), or it could be a full-fledged HTTP server running on a different machine.

## Understanding the MCP Prompt Flow

The power of an MCP tool comes from how it interacts with the Gemini prompt. It's a simple but powerful request-response cycle:

1.  **Slash Command Execution:** The user invokes a slash command (e.g., `/add-note "My new idea"`).
2.  **Tool Execution:** Gemini executes the command defined in `GEMINI.md`. This command runs your MCP script (e.g., `python .gemini/server/main.py --add-note "My new idea"`).
3.  **Action and Output:** Your script performs its custom action (calls an API, queries a database, writes to a file, etc.) and then **prints a result to standard output (stdout)**.
4.  **Prompt Enrichment:** Gemini captures the `stdout` from your script and injects it back into the prompt as context for the next step.
5.  **Chained Commands:** The next line in your slash command definition can then use this new context. For example, it could ask Gemini to summarize the result or ask the user a follow-up question.

This flow allows you to create tools that not only perform actions but also return information that can be used to drive a larger, more complex workflow.

### Example: The Internal Notes Service

In this directory, the `/add-note` command demonstrates this flow:
1.  The user runs `/add-note "A new note"`.
2.  Gemini executes `python .gemini/server/main.py --add-note "A new note"`.
3.  The Python script appends the note to `notes.txt` and prints `"Successfully added note: A new note"` to stdout.
4.  Gemini receives this output and, since it's the last step in the command, displays it to the user.

---

## Built-in & Custom MCP Tools

The Gemini CLI comes with a powerful set of built-in tools that are ready to use out of the box. You can also create your own custom tools, like the "Internal Notes Service" example in this directory.

Below is a summary of the available toolsets.

| Toolset | Description | # of Tools | Example Tools |
| :--- | :--- | :--- | :--- |
| **Firebase** | A comprehensive suite for managing your Firebase projects. | 32 | `firebase_create_app`, `firestore_query_collection`, `auth_list_users` |
| **GitHub** | Tools for interacting with GitHub repositories. | 26 | `create_pull_request`, `get_issue`, `search_code` |
| **Cloud Run** | A set of tools for deploying and managing Cloud Run services. | 9 | `deploy_container_image`, `get_service_log`, `list_services` |
| **Media Gen** | Tools for generative media, including video, images, and music. | 4 | `veo_t2v`, `imagen_t2i`, `lyria_generate_music` |
| **Audio Tools** | A suite of tools for audio processing and manipulation. | 9 | `chirp_tts`, `ffmpeg_combine_audio_and_video`, `ffmpeg_adjust_volume` |
| **Custom** | You can build your own tools to connect to any internal service. | 1 | `add_note` (from this example) |

