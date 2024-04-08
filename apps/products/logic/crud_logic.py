from ..models import Product
from apps.client.logic import crud_logic as client_logic

def create_product(client_id, product_type, balance) -> Product:
    client = client_logic.get_client_by_id(client_id)
    return Product.objects.create(client=client, product_type=product_type, balance=balance)

def get_all_products() -> list:
    return Product.objects.all()

def get_product_by_id(id) -> Product:
    try:
        product = Product.objects.get(id=id)
        return product
    except Product.DoesNotExist:
        raise Exception({"error": "Product not found"}, 404)

def update_product(id, data) -> Product:
    product=get_product_by_id(id)
    for key, value in data.items():
        setattr(product, key, value)
    product.save()
    return product

def delete_product(id) -> None:
    product = get_product_by_id(id)
    product.delete()