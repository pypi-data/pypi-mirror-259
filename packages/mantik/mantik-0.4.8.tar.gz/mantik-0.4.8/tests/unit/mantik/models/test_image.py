import pytest

import mantik.models.image as image


@pytest.mark.parametrize(
    "image_url, expected",
    [
        ("./something", "something.tar.gz"),
        ("https://cloud.mantik.ai/image", "image.tar.gz"),
        (
            "https://cloud.mantik.ai/image.tar.gz?signature-is-very-long",
            "image.tar.gz",
        ),
    ],
)
def test_get_file_name(image_url, expected):
    assert image.get_file_name(image_url=image_url) == expected


@pytest.mark.parametrize(
    "target_dir, filename, expected",
    [
        ("./something", "something.tar.gz", "./something/something.tar.gz"),
        ("./.././this/path/", "image.tar.gz", "./.././this/path/image.tar.gz"),
        ("/this/path", "image.tar.gz", "/this/path/image.tar.gz"),
    ],
)
def test_get_image_path(target_dir, filename, expected):
    assert (
        image.get_image_path(target_dir=target_dir, filename=filename)
        == expected
    )
