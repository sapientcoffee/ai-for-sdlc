# 🛠️ Persona: The Toolsmith

## The Order (Scenario)
You've created a powerful set of custom slash commands, prompts, and tools for your project. They're so good, your teammates want to use them too. You need a way to package this toolkit so it can be easily shared, versioned, and installed across multiple projects.

## The Recipe (How it Works)
This is where **Gemini CLI Extensions** come in. An extension is a shareable, versionable toolkit for Gemini, defined by a `gemini-extension.toml` manifest file. This persona shows how to bundle commands and prompts into an extension that can be distributed via a Git repository and installed with `gemini extension install`.

## On the Menu (Key Commands)
*   `/commit`: A globally available command (after installing the extension) that generates a Conventional Commit message.