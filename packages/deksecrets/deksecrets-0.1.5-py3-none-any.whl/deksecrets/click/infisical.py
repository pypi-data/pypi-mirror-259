import sys
import json
import typer
from getpass import getpass
from dektools.file import write_file
from ..tools.infisical import fetch_secrets

app = typer.Typer(add_completion=False)


@app.command()
def fetch(site_url, client_id, project, environment, path=None, out=None, client_secret=None, fmt=None):
    _fetch(site_url, client_id, client_secret, project, environment, path, out, fmt)


@app.command()
def fetch_shortcut(url, out=None, fmt=None):
    site_url, client_id, client_secret, project, environment, path = url.split('@')
    _fetch(site_url, client_id, client_secret, project, environment, path, out, fmt)


def _fetch(site_url, client_id, client_secret, project, environment, path, out, fmt):
    if not client_secret:
        client_secret = getpass('Please input ClientSecret:')
    data = fetch_secrets(site_url, client_id, client_secret, project, environment, path)
    fmt = fmt or 'env'
    if fmt == 'env':
        s = "\n".join(f'{k}="{v}"' for k, v in data.items())
    elif fmt == 'json':
        s = json.dumps(data)
    else:
        raise TypeError(f'Please provide a correct format: {fmt}')
    if out:
        write_file(out, s=s)
    else:
        out = write_file(f'.{fmt}', s=s, t=True)
        sys.stdout.write(out)
