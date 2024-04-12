from .serializer import ClientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .logic.crud_logic import get_all_clients, get_client_by_id, create_client, update_client, delete_client, get_client_by_id_number


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
def client_by_id(request, id_or_id_number):
    try:
        if request.method == 'GET':
            if id_or_id_number.isdigit():
                client = get_client_by_id(int(id_or_id_number))
            else:
                client = get_client_by_id_number(id_or_id_number)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        elif request.method == 'PUT':
            client = update_client(id_or_id_number, request.data)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        elif request.method == 'DELETE':
            delete_client(id_or_id_number)
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(e.args[0], status=e.args[1])

