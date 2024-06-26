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
        #add verification of user, if the user is not legal and the digits of the cedula are not 10, return a message
        is_valid, message = validate_client_data(request.data)
        if not is_valid:
            return Response({'detail': message}, status=status.HTTP_400_BAD_REQUEST)
        client = create_client(request.data)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def client_by_id(request, id_or_id_number):
    try:
        if request.method == 'GET':
            client = get_client_by_id_number(id_or_id_number)
            if client is None:
                return Response({'detail': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        elif request.method == 'PUT':
            client = get_client_by_id_number(id_or_id_number)
            if client is None:
                return Response({'detail': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
            client = update_client(id_or_id_number, request.data)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        elif request.method == 'DELETE':
            client = get_client_by_id_number(id_or_id_number)
            if client is None:
                return Response({'detail': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
            delete_client(id_or_id_number)
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(e.args[0], status=e.args[1])
    
# Auxiliary function 
def validate_client_data(client_data):
    id_number = client_data.get('id_number', None)
    birth_date_str = client_data.get('birth_date', None)
    message = ''
    is_valid = True
    
    if id_number:
        client = get_client_by_id_number(id_number)
        if client is not None:
            message += "The client with the provided document number already exists in the system. "
            is_valid = False

    if birth_date_str:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        today = datetime.now().date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if age < 18:
            message += "The client must be of legal age to register in the system. "
            is_valid = False

    if id_number:
        if len(id_number) != 10:
            message += "The document number (cedula) must have 10 digits."
            is_valid = False

    return is_valid, message if message else None

