# Persona: The Automator 🤖

## "Help me automate the boring stuff."

**Scenario:** You're a developer who believes that if you have to do something more than twice, it should be automated. You want to streamline common, multi-step workflows, like creating all the boilerplate files for a new feature, into a single, interactive command.

This example shows how a slash command can reference a prompt file stored in the `.gemini/` directory. This allows for more complex, multi-step instructions that go beyond simple one-liner commands.

The `/new-feature` command now triggers a generative flow:
1. Gemini reads the instructions in `.gemini/prompts/new_feature.md`.
2. It asks the user for the feature name.
3. It then generates the necessary files (`src/feature_name.py` and `tests/test_feature_name.py`) based on the template.

This turns a repetitive, manual task into a single, interactive command.
