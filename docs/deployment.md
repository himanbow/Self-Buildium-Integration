# Deployment Notes

This project exposes two runtimes:

* A Cloud Run service that listens for Buildium webhooks (default Docker `CMD`).
* A Cloud Run Job that replays Buildium automations on demand via `python -m my_app.jobs.processor`.

## Cloud Run Job Command

Configure the Cloud Run Job to invoke the job processor module instead of the Uvicorn server:

```sh
python -m my_app.jobs.processor --all-accounts --automation initiation --automation n1increase --event taskcreated
```

The repository also includes a convenience wrapper, `scripts/run_buildium_job.sh`, which forwards
all arguments to the module entrypoint.

The job entrypoint supports additional flags:

* `--account <ACCOUNT_ID>` – explicitly target one or more Buildium accounts.
* `--all-accounts` – enumerate every account in Firestore (`Buildium/buildium_accounts`).
* `--automation` – run a specific automation (`initiation`, `n1increase`). Provide multiple values to run more than one automation.
* `--event` – emulate a Buildium webhook event (`taskcreated`, `taskstatuschanged`).
* `--status` – optional status used with `taskstatuschanged` events (defaults to `Completed`).

## Required Environment Variables

Both the service and the job rely on Google Application Default Credentials for Firestore and
Secret Manager. Ensure the deployment environment defines the following variables:

* `GOOGLE_CLOUD_PROJECT` – the GCP project hosting Firestore and Secret Manager.
* `GOOGLE_APPLICATION_CREDENTIALS` – path to a service account JSON key when running locally. In Cloud Run, bind a service account with Firestore Document access and Secret Manager Secret Access instead.

The same service account permissions used by the webhook listener are required for the job:

* `roles/datastore.user` or equivalent Firestore read/write access.
* `roles/secretmanager.secretAccessor` to resolve Buildium secrets.

When running locally, export the variables before invoking the job:

```sh
export GOOGLE_CLOUD_PROJECT=<your-project-id>
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
python -m my_app.jobs.processor --account acct-123 --automation n1increase --event taskcreated
```

Configure Cloud Run Job revisions to use the same environment variables and service account as the webhook service so both workloads authenticate consistently.
