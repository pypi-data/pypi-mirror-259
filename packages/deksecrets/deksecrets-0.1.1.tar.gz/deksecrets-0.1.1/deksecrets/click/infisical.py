import sys
import typer
from getpass import getpass
from dektools.file import write_file
from ..tools.infisical import fetch_secrets

app = typer.Typer(add_completion=False)


@app.command()
def env(site_url, client_id, project, environment, path=None, out=None, client_secret=None):
    if not client_secret:
        client_secret = getpass('Please input the ClientSecret:')
    data = fetch_secrets(site_url, client_id, client_secret, project, environment, path)
    s = "\n".join(f"{k}={v}" for k, v in data.items())
    if out:
        write_file(out, s=s)
    else:
        out = write_file('.env', s=s, t=True)
        sys.stdout.write(out)
