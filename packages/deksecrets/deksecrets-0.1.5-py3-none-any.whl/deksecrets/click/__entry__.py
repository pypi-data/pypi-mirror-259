from . import app
from .infisical import app as infisical_app
from .k8s import app as k8s_app

app.add_typer(infisical_app, name='infisical')
app.add_typer(k8s_app, name='k8s')


def main():
    app()
