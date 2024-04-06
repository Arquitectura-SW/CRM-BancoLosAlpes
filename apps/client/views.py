from .serializer import ClientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .logic.crud_logic import get_all_clients, get_client_by_id, create_client, update_client


@api_view(['GET', 'POST'])
def client(request):
    if request.method == 'GET': 
        clients = get_all_clients()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        client = create_client(request.data)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def client_by_id(request, id):
    if request.method == 'GET':
        client = get_client_by_id(id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    elif request.method == 'PUT':
        client = update_client(id, request.data)
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        client = get_client_by_id(id)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
