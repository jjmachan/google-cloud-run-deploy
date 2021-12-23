OPERATOR_NAME = "gcp-cloud-run"

OPERATOR_MODULE = "google_cloud_run_deploy"

OPERATOR_SCHEMA = {
    "project_id": {
        "required": True,
        "type": "string",
        "help_message": "Your project_id will be a unique ID for each of your projects on GCP. It defines how your app interacts with Google services and what resources it uses. Read more https://developers.google.com/workspace/marketplace/create-gcp-project.",
    },
    "region": {
        "required": True,
        "type": "string",
        "help_message": "The GCP region where you want to deploy the service. Check the official list to know more about regions available https://cloud.google.com/run/docs/locations",
    },
    "port": {
        "required": True,
        "type": "integer",
        "coerce": int,
        "default": 5000,
        "help_message": "The port to which you will send API requests. Note: the port should be the same that the Bento Service is listening to (default: 5000)",
    },
    "min_instances": {
        "required": True,
        "type": "integer",
        "coerce": int,
        "default": 0,
        "help_message": "Minimum number of instances the deployment should keep ready to serve requests. Note: keeping more than 0 minimum instances can incur billing costs. Read more https://cloud.google.com/run/docs/configuring/min-instances",
    },
    "max_instances": {
        "required": True,
        "type": "integer",
        "coerce": int,
        "default": 1,
        "help_message": "Maximum number of instances the deployment should scale to serve traffic. Note: keeping a reasonable number of instances can help control billing costs. Read more https://cloud.google.com/run/docs/configuring/max-instances",
    },
    "memory": {
        "required": True,
        "type": "string",
        "coerce": str,
        "default": "512Mi",
        "help_message": "RAM for each available instance. Note: if your bento exceeds this amount, GCP will terminate the container instance. Read more https://cloud.google.com/run/docs/configuring/memory-limits",
    },
    "cpu": {
        "required": True,
        "type": "integer",
        "coerce": int,
        "default": 1,
        "help_message": "CPU cores for each available instance. Note: container instances only get CPU during request processing and startup. Read more https://cloud.google.com/run/docs/configuring/cpu-allocation",
    },
    "allow_unauthenticated": {
        "required": True,
        "default": True,
        "type": "boolean",
        "help_message": "Specifies if the service should receive public API requests. Read more https://cloud.google.com/run/docs/authenticating/public?hl=en",
    },
    "platform": {
        "required": True,
        "type": "string",
        "default": "managed",
        "help_message": "Target platform for running commands. Note: the opperator only supports `managed`. Read more https://cloud.google.com/sdk/gcloud/reference/run/deploy#--platform",
    },
}
