# 🧑‍✈️ Persona: The Git Steward

## The Order (Scenario)
You want to evolve the AI from a simple tool into a true co-developer. You have a feature request in a GitHub issue and you want the AI to manage the entire development lifecycle—from planning to implementation and testing—and deliver a complete feature branch ready for your review.

## The Recipe (How it Works)
This persona uses a single, powerful command (`/git:feature`) to kick off a fully automated, four-stage agentic workflow:
1.  **Plan:** Fetches the GitHub issue and creates a detailed `PLAN.md`.
2.  **Approval:** Pauses and asks for human approval of the plan.
3.  **Implement & Test:** Executes the plan, making atomic commits and generating tests.
4.  **Commit & Branch:** Commits the final code to a new feature branch.

## On the Menu (Key Commands)
*   `/git:feature --issue <issue_number>`: Kicks off the full, automated feature development workflow.
