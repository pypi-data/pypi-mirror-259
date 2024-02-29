"""Module about CodeQL databases."""

import os
import subprocess
import sys

import rich_click as click

from oxpecker import LANGUAGES, CODEQL_EXE


@click.command(
    help="Create a CodeQL database for a source tree that can be analyzed using one of the CodeQL "
    "products."
)
@click.option(
    "--source-root",
    default=".",
    type=click.Path(),
    help="""See `scan` help.""",
)
@click.option(
    "--database",
    required=True,
    type=click.Path(),
    help="""
        Path to the CodeQL database to create.
        This directory will be created, and must not
        already exist (but its parent must).

        If the --db-cluster option is given, this will not
        be a database itself, but a directory that will
        contain databases for several languages built
        from the same source root.

        It is important that this directory is not in a
        location that the build process will interfere
        with. For instance, the target directory of a
        Maven project would not be a suitable choice.
        """,
)
@click.option(
    "--db-cluster/--no-db-cluster",
    help="""
        Instead of creating a single database, create a
        "cluster" of databases for different languages,
        each of which is a subdirectory of the directory
        given on the command line.""",
)
@click.option(
    "--language",
    required=True,
    type=click.Choice(LANGUAGES, case_sensitive=False),
    help="""See `scan` help.""",
)
@click.option(
    "-c",
    "--command",
    help="""See `scan` help.""",
)
@click.option(
    "--overwrite/--no-overwrite",
    help="""
        If the database already exists, delete
        it and proceed with this command instead of
        failing. This option should be used with caution
        as it may recursively delete the entire database
        directory.
        """,
    default=True,
)
@click.option(
    "--codeql-options",
    multiple=True,
    help="""
    Other CodeQL options.
""",
)
@click.pass_context
def createdb(
    ctx, database, source_root, language, db_cluster, command, overwrite, codeql_options
):  # pylint: disable=too-many-arguments
    """Create a CodeQL database for a source tree that can be analyzed using one of
    the CodeQL products.
    """
    if not CODEQL_EXE:
        ctx.fail("FATAL: Codeql executable not found!")

    popen_args = (
        [
            CODEQL_EXE,
            "database",
            "create",
            "--language",
            language,
            "--db-cluster" if db_cluster else "--no-db-cluster",
            "--overwrite" if overwrite else "--no-overwrite",
        ]
        + (["--command={command}"] if command else [])
        + ["--no-run-unnecessary-builds", "-j0"]
        + ["--source-root", source_root]
        + ([" ".join(codeql_options)] if codeql_options else [])
        + ["--", os.path.expanduser(database)]
    )
    cp = subprocess.run(popen_args, capture_output=True, text=True, check=False)
    click.echo(cp.stdout)
    click.echo(cp.stderr, file=sys.stderr)
    if cp.returncode != 0:
        click.secho(
            f"Command {' '.join(cp.args)} failed with exit code {cp.returncode}.",
            fg="red",
            bold=True,
        )
        ctx.abort()
