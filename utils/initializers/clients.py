import json
from apps.client.models import Client
def create_clients():
    print('Creating clients...')
    return
    with open('clients.json', 'r') as file:
        clients = json.load(file)
        for client in clients:
            Client.objects.create(**client)
create_clients()