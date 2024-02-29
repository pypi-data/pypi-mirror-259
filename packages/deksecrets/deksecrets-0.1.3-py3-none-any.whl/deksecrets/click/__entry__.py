from . import app
from .infisical import app as infisical_app

app.add_typer(infisical_app, name='infisical')


def main():
    app()
