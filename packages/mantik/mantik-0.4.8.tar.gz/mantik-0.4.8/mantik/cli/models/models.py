import json
import typing as t
import uuid

import click

import mantik.authentication.auth
import mantik.cli.main as main
import mantik.cli.models._options as _options
import mantik.models.image as image
import mantik.utils.env
import mantik.utils.mantik_api.client
import mantik.utils.mantik_api.models

GROUP_NAME = "models"
_PROJECT_ID_ENV_VAR = "MANTIK_PROJECT_ID"
_MODEL_ID_ENV_VAR = "MANTIK_MODEL_ID"


def _access_token_from_env_vars() -> str:
    return mantik.authentication.auth.get_valid_access_token()


@main.cli.group(GROUP_NAME)
def cli() -> None:
    """Interaction with models through the mantik api."""


def mlflow_parameters_decoder(ctx, param, value) -> t.Optional[dict]:
    try:
        return json.loads(value) if value is not None else None
    except json.decoder.JSONDecodeError:
        raise TypeError(
            """MLflow parameters are in the wrong format. Try: '{"key": "value"}'"""  # noqa
        )


@cli.command("list")
@_options.PROJECT_ID
def get_all_project_models(project_id: uuid.UUID) -> None:
    """Print details of all trained models in project."""
    models = mantik.utils.mantik_api.models.get_all(
        project_id=project_id,
        token=_access_token_from_env_vars(),
    )
    click.echo(models)


@cli.command("get-one")
@_options.PROJECT_ID
@_options.MODEL_ID
def get_model(project_id: uuid.UUID, model_id: uuid.UUID) -> None:
    """Print details of specific trained model."""

    model = mantik.utils.mantik_api.models.get_one(
        project_id=project_id,
        model_id=model_id,
        token=_access_token_from_env_vars(),
    )
    click.echo(model)


@cli.command("delete")
@_options.PROJECT_ID
@_options.MODEL_ID
def delete_model(project_id: uuid.UUID, model_id: uuid.UUID) -> None:
    """Delete a trained model."""
    mantik.utils.mantik_api.models.delete(
        project_id=project_id,
        model_id=model_id,
        token=_access_token_from_env_vars(),
    )


@cli.command("add")
@_options.PROJECT_ID
@click.option("--name", type=str, required=True)
@click.option("--uri", type=str, required=True)
@click.option("--location", type=str, required=True)
@click.option("--connection-id", type=uuid.UUID, required=False)
@click.option(
    "--mlflow-parameters",
    type=str,
    required=False,
    help="""JSON data as a string.""",
    callback=mlflow_parameters_decoder,
)
@click.option("--run-id", type=uuid.UUID, required=False)
def create_model_entry(
    project_id: uuid.UUID,
    name: str,
    uri: str,
    location: str,
    connection_id: t.Optional[uuid.UUID],
    mlflow_parameters: t.Optional[dict],
    run_id: t.Optional[uuid.UUID],
) -> None:
    """Add a new trained model entry."""

    mantik.utils.mantik_api.models.add(
        project_id=project_id,
        new_model_schema=mantik.utils.mantik_api.models.PostPutModel(
            uri=uri,
            location=location,
            connection_id=connection_id,
            mlflow_parameters=mlflow_parameters,
            run_id=run_id,
            name=name,
        ),
        token=_access_token_from_env_vars(),
    )


@cli.command("update")
@_options.PROJECT_ID
@_options.MODEL_ID
@click.option("--name", type=str, required=True)
@click.option("--uri", type=str, required=True)
@click.option("--location", type=str, required=True)
@click.option("--connection-id", type=uuid.UUID, required=False)
@click.option(
    "--mlflow-parameters",
    type=str,
    required=False,
    help="""JSON data as a string.""",
    callback=mlflow_parameters_decoder,
)
@click.option("--run-id", type=uuid.UUID, required=False)
def update_model_entry(
    project_id: uuid.UUID,
    model_id: uuid.UUID,
    uri: str,
    name: str,
    location: str,
    connection_id: t.Optional[uuid.UUID],
    mlflow_parameters: t.Optional[dict],
    run_id: t.Optional[uuid.UUID],
) -> None:
    """Update details of existing trained model."""

    mantik.utils.mantik_api.models.update(
        project_id=project_id,
        model_id=model_id,
        updated_model_schema=mantik.utils.mantik_api.models.PostPutModel(
            uri=uri,
            location=location,
            connection_id=connection_id,
            mlflow_parameters=mlflow_parameters,
            run_id=run_id,
            name=name,
        ),
        token=_access_token_from_env_vars(),
    )


@cli.command("download")
@_options.PROJECT_ID
@_options.MODEL_ID
@click.option(
    "--target-dir",
    type=str,
    default="./",
    help="Path to directory where the zipped tarball image will be downloaded.",
    show_default=True,
)
@click.option(
    "--image-type",
    type=click.Choice(["docker", "apptainer"], case_sensitive=False),
    show_default=True,
    default="docker",
    help="Type of the image to fetch from the mantik platform.",
)
@click.option(
    "--load/--no-load",
    default=False,
    help="Load the tarball image into docker.",
    show_default=True,
)
def download_model(
    project_id: uuid.UUID,
    model_id: uuid.UUID,
    target_dir: str,
    image_type: str,
    load: bool,
) -> None:
    """Download the containerized version of the model."""
    if image_type.lower() == "docker":
        image_url = mantik.utils.mantik_api.models.get_image_url(
            project_id=project_id,
            model_id=model_id,
            token=_access_token_from_env_vars(),
        )

        filename = image.get_file_name(image_url=image_url)

        image_path = image.get_image_path(
            target_dir=target_dir, filename=filename
        )
        image.save_image(image_path=image_path, image_url=image_url)

        if load:
            image.load_to_docker(image_path=image_path)
        else:
            click.echo(
                "In order to load the image into docker, "
                f"you can run `docker load < {image_path}`"
            )
    else:
        raise click.ClickException(
            f"We are sorry, {image_type} is not supported yet!"
        )


@cli.command("build")
@_options.PROJECT_ID
@_options.MODEL_ID
def build_model(
    project_id: uuid.UUID,
    model_id: uuid.UUID,
) -> None:
    """Trigger model containerization."""
    mantik.utils.mantik_api.models.start_build(
        project_id=project_id,
        model_id=model_id,
        token=_access_token_from_env_vars(),
    )


@cli.command("build-status")
@_options.PROJECT_ID
@_options.MODEL_ID
def get_build_status(
    project_id: uuid.UUID,
    model_id: uuid.UUID,
) -> None:
    """Print container build status."""
    model = mantik.utils.mantik_api.models.get_one(
        project_id=project_id,
        model_id=model_id,
        token=_access_token_from_env_vars(),
    )
    click.echo(
        f"Build Status {model.status!r} for model with ID: {str(model_id)}"
    )
