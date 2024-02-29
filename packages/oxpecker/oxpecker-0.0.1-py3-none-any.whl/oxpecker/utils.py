"""Misc utilities."""

import hashlib
import json
import os
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

import click
from click import Context
from requests import Response, codes
import rich


def calculate_sha256(filename):
    """Calculate file sha256sum."""
    with open(filename, "rb") as f:
        bytes_ = f.read()
        readable_hash = hashlib.sha256(bytes_).hexdigest()
    return readable_hash


def print_resp(ctx: Context, r: Response) -> None:
    """Print requests response info and abort script for bad response."""
    try:
        parsed = json.loads(r.text)
    except json.JSONDecodeError:
        print(r.text)
    else:
        rich.print_json(json.dumps(parsed), indent=4)

    if r.status_code != codes.ok:  # pylint: disable=no-member
        click.secho(f"{r.status_code}: {r.request.method} {r.url}", fg="red", bold=True)
        ctx.abort()


def create_zip(file: str | Path, archive):
    """Create a ZIP archive from a path.
    :param file: file(s) or directory to create ZIP
    :param archive: ZIP archive path
    """
    with ZipFile(archive, "w", ZIP_DEFLATED) as zipf:
        if isinstance(file, str):
            file = Path(file)
        if file.is_file():
            zipf.write(file, file.name)
        elif file.is_dir():
            for root, _, files in os.walk(file):
                for f in files:
                    file_path = Path(root) / f
                    zipf.write(file_path, file_path.relative_to(file))
