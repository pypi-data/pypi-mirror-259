"""Module for managing Oxpecker tasks."""

import rich_click as click
from requests import codes

from oxpecker import API_ENDPOINTS, API_URL, LANGUAGES, session
from oxpecker.utils import print_resp


@click.command()
@click.option(
    "-l",
    "--language",
    type=click.Choice(LANGUAGES, case_sensitive=False),
    required=True,
    help="""The identifier for the language to create a task for.""",
)
@click.option(
    "-s", "--source-code", required=True, help="SHA256 checksum of the source code."
)
@click.option(
    "-c", "--codeql-db", required=True, help="SHA256 checksum of the CodeQL database."
)
@click.option(
    "-t",
    "--build-target",
    required=True,
    help="SHA256 checksum of the build target file.",
)
@click.option("--include-package", multiple=True, help="For pathfinder.")
@click.option("--sandbox-url", required=True, help="See `scan` help.")
@click.option("--sandbox-headers", help="See `scan` help.")
@click.option(
    "--poc-start-index",
    type=click.INT,
    default=0,
    help="See `scan` help.",
)
@click.option(
    "--poc-max-count",
    type=click.INT,
    default=1,
    help="See `scan` help.",
)
@click.option(
    "--poc-use-local-python",
    type=click.BOOL,
    default=False,
    help="Use local Python to generate POC.",
)
@click.pass_context
def create(
    ctx,
    language,
    source_code,
    codeql_db,
    build_target,
    include_package,
    sandbox_url,
    sandbox_headers,
    poc_start_index,
    poc_max_count,
    poc_use_local_python,
):  # pylint: disable=too-many-arguments
    """Create a new task."""
    if ctx.find_root().params["debug"]:
        click.echo(language)
        click.echo(source_code)
        click.echo(codeql_db)
        click.echo(build_target)
        click.echo(include_package)
    r = session.post(
        f"{API_URL}{API_ENDPOINTS['task_create']}",
        json={
            "lang": language,
            "sourceCode": source_code,
            "params": {
                "sast": {"codeqldb": codeql_db},
                "pf": {
                    "buildTargetFile": build_target,
                    "includePackages": include_package,
                },
                "poc": {
                    "sandboxUrl": sandbox_url,
                    "sandboxAuthHeaders": sandbox_headers,
                    "startIndex": poc_start_index,
                    "maxCount": poc_max_count,
                    "useLocalPython": poc_use_local_python,
                },
            },
        },
        verify=not ctx.find_root().params["insecure_skip_tls_verify"],
    )

    print_resp(ctx, r)
    if r.status_code == codes.ok:  # pylint: disable=no-member
        return r.json()["taskId"]


@click.command(name="list")
@click.pass_context
def list_command(ctx):
    """List tasks."""
    r = session.post(
        f"{API_URL}{API_ENDPOINTS['task_list']}",
        json={},
        verify=not ctx.find_root().params["insecure_skip_tls_verify"],
    )
    print_resp(ctx, r)


@click.command()
@click.argument("task_id", type=click.INT)
@click.pass_context
def inspect(ctx, task_id):
    """Return detailed information of a task."""
    r = session.get(
        f"{API_URL}{API_ENDPOINTS['task_inspect']}/{task_id}",
        verify=not ctx.find_root().params["insecure_skip_tls_verify"],
    )
    ctx.ensure_object(dict)
    ctx.obj["response"] = r
    print_resp(ctx, r)


@click.command()
def cancel():
    """Cancel a task."""
    raise NotImplementedError


@click.command()
@click.argument("task_id", type=click.INT)
@click.pass_context
def report(ctx, task_id):
    """Get vulnerability report about a task."""
    r = session.get(
        f"{API_URL}{API_ENDPOINTS['task_inspect']}/{task_id}/result",
        verify=not ctx.find_root().params["insecure_skip_tls_verify"],
    )
    print_resp(ctx, r)
