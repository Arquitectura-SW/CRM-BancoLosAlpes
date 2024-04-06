from apps.client.models import Client

def get_all_clients():
    return Client.objects.all()

def get_client_by_id(id):
    return Client.objects.get(id=id)

def create_client(data):
    return Client.objects.create(**data)

def update_client(id, data):
    client = Client.objects.get(id=id)
    for key, value in data.items():
        setattr(client, key, value)
    client.save()
    return client