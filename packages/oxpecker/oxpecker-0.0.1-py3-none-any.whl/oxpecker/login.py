"""Module for login to the server."""

from json import JSONDecodeError
import os
import rich_click as click
from requests import codes

from oxpecker import API_ENDPOINTS, API_URL, session, WORK_DIR


@click.command()
@click.option("--username", "-u", required=True, help="""Username of the service.""")
@click.option("--password", "-p", required=True, help="""Password of the service.""")
@click.pass_context
def login(ctx, username, password):
    """Login to Oxpecker service."""
    if ctx.find_root().params["debug"]:
        click.echo(username)
        click.echo(password)
    r = session.post(
        f"{API_URL}{API_ENDPOINTS['login']}",
        json={"userName": username, "password": password},
        verify=not ctx.find_root().params["insecure_skip_tls_verify"],
    )
    if r.status_code == codes.ok:  # pylint: disable=no-member
        try:
            print(r.json())
        except JSONDecodeError:
            print(r.text)
        with open(
            token_file_path := WORK_DIR / "token", mode="w", encoding="utf-8"
        ) as cf:
            cf.write(r.json()["token"])
        os.chmod(token_file_path, 0o600)
    else:
        print(f"{r.status_code}: {r.request.method} {r.url}")
        print(r.text)
