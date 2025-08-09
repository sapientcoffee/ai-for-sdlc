# 🤖 Persona: The Automator

## The Order (Scenario)
You're a developer who believes that if you have to do something more than twice, it should be automated. You want to streamline common, multi-step workflows, like creating all the boilerplate files for a new feature, into a single, interactive command.

## The Recipe (How it Works)
This example shows how a slash command can reference an external prompt file. This allows for more complex, multi-step instructions that go beyond simple one-liners. The `/new-feature` command triggers a generative flow that asks for a feature name and then creates the necessary source and test files from a template.

## On the Menu (Key Commands)
*   `/new-feature`: Kicks off an interactive workflow to create a new feature and its test file.