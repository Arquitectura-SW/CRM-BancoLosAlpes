from .serializer import ClientSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
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
            client = get_client_by_id(id_or_id_number)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        elif request.method == 'PUT':
            client = get_client_by_id(id_or_id_number)
            if not client:
                return Response({"error": "Client not found."}, status=status.HTTP_404_NOT_FOUND)
            
            is_valid, error_message = validate_client_data(request.data)
            if not is_valid:
                return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

            client = update_client(id_or_id_number, request.data)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        elif request.method == 'DELETE':
            delete_client(id_or_id_number)
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(e.args[0], status=e.args[1])

# Auxiliary function 
def validate_client_data(client_data):
    birth_date_str = client_data.get('birth_date', None)
    if birth_date_str:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        today = datetime.now().date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if age < 18:
            return False, "The client must be of legal age to register in the system."
    else:
        return True, None

    id_number = client_data.get('id_number', None)
    if id_number:
        if len(id_number) != 10:
            return False, "The document number (cedula) must have 10 digits."

    return True, None