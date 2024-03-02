import typer
from getpass import getpass
from dektools.shell import shell_wrapper

app = typer.Typer(add_completion=False)


@app.command()
def auth(server, token=None, cluster='deksecrets', context='deksecrets', user='deksecrets'):
    if not token:
        token = getpass('Please input token:')
    shell_wrapper(f"kubectl config set-cluster {cluster} --server={server}")
    shell_wrapper(f"kubectl config set-context {context} --cluster={cluster}")
    shell_wrapper(f"kubectl config set-credentials {user} --token={token}")
    shell_wrapper(f"kubectl config set-context {context} --user={user}")
    shell_wrapper(f"kubectl config use-context {context}")


@app.callback()
def callback():
    pass
