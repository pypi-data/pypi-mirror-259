from __future__ import annotations

import json
from pathlib import Path

import requests

from workstream_dbt_core.exception import WorkstreamError
from workstream_dbt_core.http import post_dbt_files

MANIFEST = "manifest.json"
RUN_RESULTS = "run_results.json"
SOURCE_RESULTS = "sources.json"


def report_invocation(
    target_path: Path,
    client_id: str,
    client_secret: str,
    root_url: str = "https://api.workstream.io/",
) -> list[tuple[Path, requests.Response]]:
    """
    Reports an invocation of dbt-core to Workstream.

    Args:
        - target_path (pathlib.Path): The path to the `target` directory created by
            an invocation of dbt.
        - client_id (str): The Client ID provided by Workstream for this integration.
        - client_secret (str): The Client Secret provided by Workstream for this
            integration.
        - root_url (str): The root url for the API endpoint provided by Workstream for
            this integration.

    Returns: list[tuple[Path, requests.Response]]: A (file_path,
        Response) pair for each attempted upload of the file at file_path.

    Raises: WorkstreamError if the process does not successfully complete for all files.
    """
    _validate_target_path(target_path)
    project_id, invocation_id = _get_project_and_invocation_id_from_manifest(
        target_path
    )
    files = _get_files_from_invocation(target_path, invocation_id)
    responses = post_dbt_files(
        files, project_id, invocation_id, client_id, client_secret, root_url
    )
    _validate_responses(responses)
    return responses


def _validate_target_path(target_path: Path) -> None:
    """
    Raise a WorkstreamError if target_path does not contain at least a manifest.json and
    one of a run_results.json or sources.json.
    """
    try:
        assert target_path.exists()
        manifest_path = target_path / MANIFEST
        assert manifest_path.exists()
        run_path = target_path / RUN_RESULTS
        source_path = target_path / SOURCE_RESULTS
        assert run_path.exists() or source_path.exists()
    except AssertionError as e:
        raise WorkstreamError(
            e,
            title="Target path does not contain required files.",
            help_text=(
                "target_path must contain at least a manifest.json and one of a "
                "run_results.json or sources.json."
            ),
        ) from e


def _get_project_and_invocation_id_from_manifest(target_path: Path) -> tuple[str, str]:
    """
    Introspect manifest.json to find latest IDs. All dbt commands create/update
    manifest.json, so the invocation_id from that file should be the ID for the
    most recent dbt run.

    Args:
        - target_path (Path)

    Returns: tuple of (project_id, invocation_id)
    """
    manifest_path = target_path / MANIFEST
    try:
        with manifest_path.open("r") as f:
            manifest = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        raise WorkstreamError(
            e, title="Could not load manifest.json", help_text=str(e)
        ) from e

    try:
        project_id = manifest["metadata"]["project_id"]
        invocation_id = manifest["metadata"]["invocation_id"]
    except KeyError as e:
        raise WorkstreamError(
            e,
            title="manifest.json missing critical metadata",
            help_text=f"Could not find key metadata.{e}",
        ) from e

    return project_id, invocation_id


def _get_files_from_invocation(
    target_path: Path, invocation_id: str
) -> list[tuple[str, Path]]:
    """
    Finds all manifest, sources, and run_results (.json) files in target_path that match
    invocation_id.

    Returns: A list of (file_type, path) pairs for relevant files.
    """
    candidates = [MANIFEST, RUN_RESULTS, SOURCE_RESULTS]
    found_files: list[tuple[str, Path]] = []
    for fn in candidates:
        p = target_path / fn
        try:
            with p.open("r") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError):
            continue

        try:
            file_invocation_id = data["metadata"]["invocation_id"]
        except KeyError:
            continue
        else:
            if file_invocation_id == invocation_id:
                found_files.append((p.stem, p))

    return found_files


def _validate_responses(responses: list[tuple[Path, requests.Response]]) -> None:
    """
    Print success or fail message for each attempted upload. Raise a
    WorkstreamError if any requests were unsuccessful.

    Args:
        - responses (list[tuple[pathlib.Path, requests.Response]]): A (file_path,
        Response) pair for each attempted upload of the file at file_path.

    Returns: None
    """
    for p, response in responses:
        if response.ok:
            print(f"Uploaded {p} successfully")
        else:
            print(f"Encountered an error while uploading {p}:")
            print(f"Status: {response.status_code}")
            print(response.text)
    if not all(response.ok for _, response in responses):
        raise WorkstreamError(
            title="Encountered an error while uploading a file.",
            help_text="See specific errors above.",
        )
