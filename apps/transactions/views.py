from .serializer import TransactionSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from .logic import crud_logic 

@api_view(['GET', 'POST'])
def transaction(request: Request):
    try:
        if request.method == 'GET':
            transactions = crud_logic.get_all_transactions()
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            transaction = crud_logic.create_transaction(**request.data)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(e.args[0], status=e.args[1])
    
@api_view(['GET', 'PUT', 'DELETE'])
def transaction_by_id(request: Request, id):
    try:
        if request.method == 'GET':
            transaction = crud_logic.get_transaction_by_id(id)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data)
        elif request.method == 'PUT':
            transaction = crud_logic.update_transaction(id, request.data)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data)
        elif request.method == 'DELETE':
            crud_logic.delete_transaction(id)
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(e.args[0], status=e.args[1])

