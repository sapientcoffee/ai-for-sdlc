# 🧑‍✈️ 11. The Git Steward: Your AI Co-Developer

This persona represents the pinnacle of AI-assisted development within this cookbook. It evolves the AI from a simple tool into a true co-developer, capable of managing the entire lifecycle of a feature request—from a GitHub issue to a new feature branch—through a sophisticated, agentic workflow.

## The Philosophy: Code is a Conversation

Great software development is a conversation. This persona structures that conversation, ensuring it is clear, logical, and safe, especially when one of the participants is an AI. It's built on two core principles:

1.  **Human-Led, AI-Driven:** You, the human developer, are the architect. You set the vision and make the critical decisions. The AI is the tireless builder, handling the detailed implementation and testing.
2.  **A Perfect Audit Trail:** Every action the AI takes is recorded as a small, atomic, conventional commit. This creates a crystal-clear git history that is not just a log, but a story of how the feature was built.

## The Agentic Workflow: From Issue to Feature Branch

The centerpiece of this persona is a single, powerful command that encapsulates the entire development process. You can provide a simple description, or, more powerfully, point it directly at a GitHub issue.

### `/git:feature --issue <issue_number>`

When you run this command, you kick off a fully automated, four-stage workflow:

#### **Stage 1: Plan from Reality 📝**

The Git Steward begins by fetching the specified GitHub issue, including its title, body, and labels. It uses this real-world context to create a detailed `PLAN.md` file. This blueprint outlines the goal, files to be changed, implementation steps, and a testing strategy, all grounded in the source of truth—the issue itself.

#### **Stage 2: Approve the Blueprint ✅**

This is the most critical step. The workflow pauses. The AI has presented its plan, and now it needs your approval. You review the `PLAN.md`, make any adjustments, and give the green light. This "human-in-the-loop" checkpoint ensures you are always in control of the architectural direction.

#### **Stage 3: Implement & Test 🛠️**

Once you approve the plan, the Git Steward gets to work. It executes the implementation steps from the `PLAN.md`, making a small, atomic commit after each step. Then, it seamlessly transitions to a quality engineering role, writing the unit tests to verify the new code.

#### **Stage 4: Commit & Branch 🌿**

With the feature implemented and tested, the Git Steward bundles all the work into a new feature branch, named logically after the issue number (e.g., `feat/issue-123`). It then announces that the work is complete and ready for you to create a pull request.

## The Future of Development, Today

This persona offers a glimpse into a new era of software development. It's a structured, safe, and incredibly efficient paradigm where human creativity is amplified by AI execution. By grounding this powerful agentic workflow in the proven best practices of a clean and disciplined git history, "The Git Steward" provides a model for building the future, one perfect commit at a time.