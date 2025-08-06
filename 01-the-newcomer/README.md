# Persona: The Newcomer

**Scenario:** A developer has just joined a team and cloned a repository for the first time. Their goal is to quickly get oriented with the project's structure, purpose, and basic commands without having to read all the documentation.

This is accomplished by providing project-specific context to Gemini via a `GEMINI.md` file, which acts as the **System Prompt**.

---

## What is a System Prompt? (The Digital Soul of Your Project)

If you've ever tweaked a `.bashrc` to create a custom alias or a `.gitconfig` to set your user name, you already understand the concept of a System Prompt. In the command-line world, we use simple text files (often called "dotfiles") to teach our tools how to behave in a specific context.

The `GEMINI.md` file is exactly that, but for your AI assistant. It's the **System Prompt**: a configuration file that gives Gemini the context, rules, and personality for your specific project. It's how you turn a general-purpose AI into *your* specialized coding partner.

Think of it as a cheat sheet for the AI. Here are some great things to put into your `GEMINI.md`:

*   **Set a Persona:** Define how the AI should behave.
    *   *Example:* `You are a senior Go developer. You are friendly, helpful, and provide concise explanations.`
*   **Core Project Details:** Point out the most important files, frameworks, or utility functions.
    *   *Example:* `This is a Python Flask project. The main application file is 'app.py'. All database logic is in 'src/db.py'.`
*   **Code Style Guidelines:** Describe the project's coding conventions.
    *   *Example:* `This project follows the Google Python Style Guide. All functions must have a docstring.`
*   **Testing Instructions:** Explain how to run the test suite.
    *   *Example:* `Run tests with 'pytest'.`
*   **Folder Etiquette:** Describe the purpose of different directories.
    *   *Example:* `The 'scripts/' directory is for one-off utility scripts. The 'src/' directory is for core application code.`
*   **Solutions to Common Model Failures:** If you notice Gemini making a recurring mistake, you can add a directive to correct it.
    *   *Example:* `When writing a new test, always import 'pytest' at the top of the file.`

---

## Don't Write It, Generate It! 🚀 (The `/init` command)

Manually creating a `GEMINI.md` file is great, but what if you could get a running start? That's where the `/init` command comes in.

This magical command will:
1.  **Read your project files:** It scans your `README`, your source code, and your dependency files (`pyproject.toml`, `package.json`, etc.).
2.  **Analyze the contents:** It identifies the project's purpose, the primary language, the key frameworks, and the commands used to build and run it.
3.  **Generate a `GEMINI.md` file:** It creates a tailored, project-specific `GEMINI.md` file that summarizes everything it learned.

This gives you an amazing starting point for your System Prompt. It's like having an AI assistant do the initial project orientation *for* you. You can then take the generated file and tweak it to add your own specific rules and personality.

It's the ultimate way to bootstrap your project's "digital soul."

---

## How Gemini Finds `GEMINI.md`

Just like your shell loads a series of startup files, Gemini CLI has a specific search order to find and load context files. It aggregates all the `GEMINI.md` files it finds, allowing you to have global, per-project, and even per-directory context.

The search order is:
1.  **Global Config:** From your `~/.gemini` folder.
2.  **Installed Extensions:** From your `~/.gemini/extensions` subfolders.
3.  **Parent Directories:** It checks all directories from the root of your filesystem down to your current working directory.
4.  **Subdirectories:** It will check up to 200 subfolders from your current working directory.

## Example

An example file is [here](./GEMINI.md).

