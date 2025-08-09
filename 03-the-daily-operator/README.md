# 🔥 Persona: The Daily Operator

## The Order (Scenario)
You are an SRE, a DevOps engineer, or a platform operator. The pager might go off at any moment. You are responsible for the health of production and staging environments, and you need to inspect logs, check service status, and manage cloud resources, often under pressure.

## The Recipe (How it Works)
This persona demonstrates how Gemini can be used as a powerful "ops-in-a-box." It provides a centralized and simplified interface for complex infrastructure commands by wrapping long, hard-to-remember `gcloud` or `kubectl` commands into simple, memorable slash commands.

## On the Menu (Key Commands)
*   `/gcloud:run:status`: Gets the current status of a Cloud Run service.
*   `/gcloud:run:logs`: Fetches the latest logs from a running service.
*   `/kubectl:pods`: Lists running Kubernetes pods.
*   `/gcloud:run:rollback`: A safe rollback command that requires confirmation.