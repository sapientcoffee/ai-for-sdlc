# Gemini CLI Cookbook: A Practical Guide 🧑‍🍳

Welcome, intrepid developer! Grab your favorite mug of liquid ambition ☕️, because you've just stumbled upon the ultimate cookbook for the Gemini CLI.

This isn't your grandma's recipe book (unless your grandma was a command-line wizard). It's a collection of practical, real-world examples designed to take you from a curious newcomer to a seasoned Gemini CLI power user. We believe that the best way to learn is by doing, so we've structured this cookbook around different **personas**. Each directory is a self-contained "recipe" for solving a real problem.

Just pick a persona that resonates with you and start exploring!

This is a combination of personal experiments and also crowd sourcing. I have tried to cite any inspiration I can recieved from others.

## Getting Started: Setup & Configuration

Before you dive into the recipes, here are a few one-time setup steps to make your life easier.

1.  **Login to Google Cloud:**
    `gemini auth login`
    This will open a browser window to authenticate your account. You can see all authenticated accounts with `gemini auth list`.

2.  **Create the `g` alias:**
    Typing `gemini` is for the birds. Real pros use a shorter alias. Add this to your `.bashrc` or `.zshrc`:
    `alias g='gemini'`
    Now you can just type `g` for all commands!

3.  **Set your default model:**
    To avoid specifying the model every time, you can set it globally:
    `g config set model gemini-1.5-pro`

## The Philosophy: Why the CLI? 🤔

You might be wondering, "Why all the fuss about the command line?" Great question! The short answer is: **power, speed, and flow.** The long answer is a caffeinated love letter to the terminal that explains my personal workflow philosophy.

➡️ **[Read all about it here: My IDE is the Linux Terminal](./why-cli.md)**

## What is a Coding Agent?

An agent is a system that can perceive its environment and act upon it to autonomously accomplish tasks. The **Gemini CLI** is a **coding agent that lives in your terminal**. It has access to your local file system and can execute commands, allowing it to help with complex software development workflows.

The same agent technology that powers the Gemini CLI is also leveraged by the **Agent Mode in the VS Code Gemini Code Assist extension**, providing a consistent experience across different interfaces.

## Official Documentation

For the nitty-gritty details, please refer to the [official Gemini CLI documentation](https://github.com/google-gemini/gemini-cli/blob/main/docs/index.md).

## The Personas (Our Recipes)

*   **[01-the-newcomer](./01-the-newcomer/README.md):** A developer new to a project who needs to get up to speed quickly.
*   **[02-the-daily-developer](./02-the-daily-developer/README.md):** A developer focused on day-to-day coding tasks.
*   **[03-the-daily-operator](./03-the-daily-operator/README.md):** A daily operator managing and monitoring live services.
*   **[04-the-academic](./04-the-academic/README.md):** An academic using LaTeX for their reports.
*   **[05-the-automator](./05-the-automator/README.md):** A developer who wants to streamline and automate repetitive workflows.
*   **[06-the-architect](./06-the-architect/README.md):** A senior developer or tech lead responsible for project standards and custom tooling.
*   **[07-the-power-user](./07-the-power-user/README.md):** A power user creating advanced, reusable slash commands.
*   **[08-the-integrator](./08-the-integrator/README.md):** An integrator connecting Gemini to custom internal tools.
*   **[09-the-toolsmith](./09-the-toolsmith/README.md):** A toolsmith packaging and sharing commands as a reusable extension.
*   **[10-the-quality-guardian](./10-the-quality-guardian/README.md):** A quality guardian ensuring code standards for both authors and reviewers.
