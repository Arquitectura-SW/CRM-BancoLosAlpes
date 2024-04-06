from apps.client.models import Client
from apps.client.serializer import ClientSerializer
from rest_framework.response import Response
from apps.client.logic.crud_logic import get_all_clients, get_client_by_id, create_client, update_client
from rest_framework.views import APIView

class ClientAPICRUD(APIView):
    
    def get(self, request):
        clients = get_all_clients()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=200, content_type="application/json")
    
    def get_by_id(self, request, id):
        client = get_client_by_id(id)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=200, content_type="application/json")
    
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            create_client(serializer.validated_data)
            return Response(serializer.data, status=201, content_type="application/json")
        return Response(serializer.errors, status=400, content_type="application/json")