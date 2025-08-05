# Persona: The Toolsmith 🛠️

## "Help me package and share my commands."

**Scenario:** You've created a powerful set of custom slash commands, prompts, and tools for your project. They're so good, your teammates want to use them too. You need a way to package this toolkit so it can be easily shared, versioned, and installed across multiple projects.

This is where **Gemini CLI Extensions** come in.

---


Extensions allow you to bundle tools, context, and configurations. Each extension is a directory with a gemini-extension.json file.

Global extensions: ~/.gemini/extensions/
Project-specific extensions: <workspace>/.gemini/extensions/
Example Extension
An extension is defined by a gemini-extension.json file inside its own directory, for example <workspace>/.gemini/extensions/my-extension/gemini-extension.json:

{
  "name": "my-extension",
  "version": "1.0.0",
  "mcpServers": {
    "my-server": {
      "command": "node my-server.js"
    }
  },
  "contextFileName": "GEMINI.md",
  "excludeTools": ["run_shell_command"]
}
For more details, see the extensions guide.



## Understanding Gemini CLI Extensions

An extension is a **shareable, versionable toolkit** for Gemini. It allows you to bundle a collection of custom commands, prompts, and tools into a single package that can be easily installed and used in any project.

Think of it like a `pip` package or `npm` module, but for your Gemini commands.

### Key Concepts

1.  **Packaging:** An extension is a directory containing a `gemini-extension.toml` manifest file, along with optional `prompts` and `tools` subdirectories. This manifest file is the entry point that tells Gemini what the extension provides.

2.  **Distribution:** Extensions are designed to be distributed via Git repositories. You can create a dedicated repository for your extension, allowing for versioning and collaboration.

3.  **Installation:** Users can install an extension into their local Gemini environment using the `gemini extension install <git_repo_url>` command. Once installed, the extension's commands are available globally in any project.

### Example Plan for this Directory

To demonstrate this, we will create a simple but practical "Conventional Commit Helper" extension.

1.  **`gemini-extension.toml`:** A manifest file that defines our extension's name and version.
2.  **`prompts/`:** A directory containing a `conventional_commit.md` prompt that knows how to generate a commit message from a `git diff`.
3.  **`GEMINI.md`:** A file within the extension that defines the `/commit` slash command, which will be made available globally after installation.

This example will show you how to structure an extension and how a user would install it, turning a project-specific tool into a reusable asset for your entire team.

---

## Managing Your Extensions

Once an extension is created and hosted in a Git repository, users can manage it with the following commands:

