from collections import OrderedDict
from infisical_client import ClientSettings, InfisicalClient, ListSecretsOptions


def fetch_secrets(site_url, client_id, client_secret, project, environment, path=None):
    client = InfisicalClient(ClientSettings(
        site_url=site_url,
        client_id=client_id,
        client_secret=client_secret,
    ))
    secrets = client.listSecrets(options=ListSecretsOptions(
        project_id=project,
        environment=environment,
        path=path
    ))
    return OrderedDict(((s.secret_key, s.secret_value) for s in secrets))
