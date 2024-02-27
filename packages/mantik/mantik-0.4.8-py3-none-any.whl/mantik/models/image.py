import logging

import requests

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def save_image(image_path: str, image_url: str):
    logger.info(
        f"Downloading image: {image_path}. This can take a few minutes..."
    )
    image = requests.get(image_url, stream=True)

    with open(image_path, "wb") as f:
        for chunk in image:
            f.write(chunk)
    logger.info(f"Image saved as zipped tarball at {image_path}")


def get_image_path(target_dir: str, filename: str) -> str:
    if not target_dir[-1] == "/":
        target_dir += "/"
    return target_dir + filename


def get_file_name(image_url: str) -> str:
    return image_url.split("/")[-1].split(".tar.gz")[0] + ".tar.gz"


def load_to_docker(image_path: str):
    try:
        import docker
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Install supported 'docker' version "
            "(`pip install mantik[docker]`)"
            "or any desired 'docker' python package version"
        ) from exc
    logger.info(
        "Unzipping and loading into docker. This can take a few minutes..."
    )

    client = docker.from_env()

    with open(image_path, "rb") as f:
        client.images.load(f)

    logger.info(
        "Run 'docker images', an image named "
        f"{get_file_name(image_path)[:-7]} should be present."
    )

    logger.info(
        f"Run 'docker run -p 8080:8080 {get_file_name(image_path)[:-7]}` to serve the model image for inference."  # noqa
    )
