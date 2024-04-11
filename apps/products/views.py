from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from .logic import crud_logic 

@api_view(['GET', 'POST'])
def product(request: Request):
    if request.method == 'GET':
        products = crud_logic.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        product = crud_logic.create_product(**request.data)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 

@api_view(['GET', 'PUT', 'DELETE'])
def product_by_id(request: Request, id):
    try:
        if request.method == 'GET':
            product = crud_logic.get_product_by_id(id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        elif request.method == 'PUT':
            product = crud_logic.update_product(id, request.data)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        elif request.method == 'DELETE':
            crud_logic.delete_product(id)
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e: 
        return Response(e.args[0], status=e.args[1])
