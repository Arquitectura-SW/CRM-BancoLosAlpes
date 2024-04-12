from apps.client.models import Client

def get_all_clients() -> list:
    return Client.objects.all()

def get_client_by_id(id) -> Client:
    try:
        client = Client.objects.get(id=id)
        return client
    except Client.DoesNotExist:
        raise Exception({"error": "Client not found"}, 404)
    
def get_client_by_id_number(id_number: str) -> Client:
    try:
        client = Client.objects.get(id_number=id_number)
        return client
    except Client.DoesNotExist:
        return None

def create_client(data) -> Client:
    return Client.objects.create(**data)

def update_client(id, data) -> Client:
    client=get_client_by_id_number(id)
    for key, value in data.items():
        setattr(client, key, value)
    client.save()
    return client

def delete_client(id) -> None:
    client = get_client_by_id_number(id)
    client.delete()