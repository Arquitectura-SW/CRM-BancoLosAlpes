import json
from apps.client.models import Client

def create_clients():
    with open('clients.json', 'r') as file:
        clients = json.load(file)
        for client in clients:
            Client.objects.create(**client)


if __name__ == '__main__':
    create_clients()