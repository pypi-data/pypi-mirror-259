import click
from prl.auth import get_auth_token, login

from .rag import rag
from .run import run
from .suite import suite


@click.group()
def cli():
    pass


cli.add_command(suite)
cli.add_command(run)
cli.add_command(login)
cli.add_command(rag)
