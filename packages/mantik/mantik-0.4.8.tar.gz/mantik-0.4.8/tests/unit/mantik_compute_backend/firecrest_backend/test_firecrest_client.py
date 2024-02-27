import logging
import pathlib

import mantik.testing as testing
import mantik_compute_backend.firecrest as firecrest


def test_upload_files_to_run_directory(monkeypatch, caplog):
    caplog.set_level(logging.INFO)
    run_dir = pathlib.Path("/path/to/remote/mantik/mlflow-run-id")
    files = [
        pathlib.Path("/absolute/path/to/file1.py"),
        pathlib.Path("/absolute/path/to/folder/file2.py"),
    ]
    expected_source_and_target_paths = [
        "Uploading file /absolute/path/to/file1.py to "
        "/path/to/remote/mantik/mlflow-run-id",
        "Uploading file /absolute/path/to/folder/file2.py to "
        "/path/to/remote/mantik/mlflow-run-id/folder",
    ]
    client = testing.firecrest.FakeClient()
    client = firecrest.client.Client(
        client=client, machine="daint", account="test-account"
    )

    client._upload_files_to_run_directory(run_dir=run_dir, files=files)
    for path in expected_source_and_target_paths:
        assert path in caplog.text, f"Path '{path}' not found in caplog.text"
