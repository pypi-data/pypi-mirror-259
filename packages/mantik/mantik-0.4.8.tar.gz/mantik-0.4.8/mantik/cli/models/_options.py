import uuid

import click

_PROJECT_ID_ENV_VAR = "MANTIK_PROJECT_ID"
_MODEL_ID_ENV_VAR = "MANTIK_MODEL_ID"

PROJECT_ID = click.option(
    "--project-id",
    type=uuid.UUID,
    required=True,
    envvar=_PROJECT_ID_ENV_VAR,
)

MODEL_ID = click.option(
    "--model-id", type=uuid.UUID, required=True, envvar=_MODEL_ID_ENV_VAR
)
