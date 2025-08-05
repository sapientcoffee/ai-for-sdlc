# Gemini Cookbook: The Daily Operator

# These commands are designed for interacting with cloud infrastructure.
# Replace placeholders like `my-project` and `us-central1` with your actual values.

## Slash Commands

# --- Google Cloud Operations ---
- `/gcloud:run:status`: Get the status of a Cloud Run service.
  - `gcloud run services describe {{arg1}} --project=my-project --region=us-central1 --format=json`

- `/gcloud:run:logs`: Get the latest logs for a Cloud Run service.
  - `gcloud logging read "resource.type=\"cloud_run_revision\" AND resource.labels.service_name=\"{{arg1}}\"" --project=my-project --limit=50 --format=json`

# --- Kubernetes Operations ---
- `/kubectl:pods`: List all pods in the specified namespace.
  - `kubectl get pods -n {{arg1}}`

# --- Safe Rollback Workflow ---
# This command first lists available revisions before allowing a rollback.
# This is a safer pattern than a direct rollback command.
- `/gcloud:run:revisions`: List available revisions for a Cloud Run service.
  - `gcloud run revisions list --service={{arg1}} --project=my-project --region=us-central1`
- `/gcloud:run:rollback`: Roll back a service to a specific revision.
  - `echo "You are about to roll back {{arg1}} to revision {{arg2}}. This is a production change."`
  - `echo "Please confirm the revision by re-typing it."`
  - `gcloud run services update-traffic {{arg1}} --to-revisions={{response[2]}}=100 --project=my-project --region=us-central1`

