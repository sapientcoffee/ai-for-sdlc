# 🧑‍✈️ 11. The Git Steward: Your AI Co-Developer

This persona transforms Gemini from a simple git enforcer into a true AI co-developer. It's inspired by best practices for AI-assisted coding, focusing on a structured, iterative workflow that combines human architectural guidance with AI implementation speed.

## The Scenario: Beyond Simple Commits

You're ready to move beyond just using an AI to *write* code. You want to partner with it to *build* features. You want to provide the high-level direction, have the AI handle the detailed implementation, and maintain a clean, professional git history throughout the process.

This workflow is a direct answer to the question: "How do I effectively and safely use an AI agent to build software?"

## The Co-Developer Workflow: Plan, Implement, Test, Review

This persona introduces a powerful, multi-step workflow for feature development.

### 1. `/git:plan "Your feature idea"`
It all starts with a conversation. You provide a high-level description of the feature you want to build. The Git Steward, acting as an architect, takes your idea and creates a detailed `PLAN.md` file. This plan includes:
- **The Goal:** A clear statement of the feature's purpose.
- **Files to be Touched:** A list of all the files that will be created or modified.
- **Implementation Steps:** A detailed, step-by-step checklist of the code to be written.
- **Testing Strategy:** An outline of the tests needed to ensure quality.

**Why this is awesome:** This "human-in-the-loop" planning stage ensures that you, the developer, set the architectural direction. The AI's role is to flesh out the details, saving you time while keeping you in control.

### 2. `/git:implement`
With the plan approved, the real magic begins. The Git Steward reads the `PLAN.md` and starts executing the implementation steps.

Crucially, after each logical step, it makes a small, atomic, conventional commit.

**Why this is awesome:** This is the "Gospel of Small Commits" in action. Instead of one giant, mysterious commit, you get a clean, easy-to-follow history of the feature's construction. Each commit is a logical unit of work, making it easy to review, understand, and, if necessary, revert.

### 3. `/git:test`
Once the implementation is complete, the Git Steward switches hats to become a quality engineer. It reads the `PLAN.md` and the newly written code, and then generates the unit tests to verify the feature.

**Why this is awesome:** This ensures that testing is not an afterthought. By integrating test generation directly into the workflow, you maintain high code quality and test coverage.

### 4. `/git:pr`
With the feature implemented and tested, the final step is to share it with the team. This command creates a pull request, using the `PLAN.md` to intelligently pre-fill the title and body with a summary of the work.

**Why this is awesome:** This automates the final step of the development process, creating a clear and informative pull request that's easy for your teammates to review.

## The Future of Development

This workflow represents a powerful new paradigm for software development, one where human creativity and AI-powered execution work in harmony. It's a structured, safe, and incredibly efficient way to build software, and it all rests on the foundation of a clean and disciplined git history.
