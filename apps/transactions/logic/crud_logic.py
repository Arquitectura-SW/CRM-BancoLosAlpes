from ..models import Transaction
from apps.products.logic import crud_logic as product_logic

def create_transaction(product_id,transaction_type, amount, balance_after, description) -> Transaction:
    product = product_logic.get_product_by_id(product_id)
    transaction = Transaction.objects.create(product=product, amount=amount, transaction_type=transaction_type, balance_after=balance_after, description=description)
    return transaction

def get_all_transactions() -> list:
    return Transaction.objects.all()

def get_transaction_by_id(id) -> Transaction:
    try:
        transaction = Transaction.objects.get(id=id)
        return transaction
    except Transaction.DoesNotExist:
        raise Exception({"error": "Transaction not found"}, 404)

def update_transaction(id, data) -> Transaction:
    transaction = get_transaction_by_id(id)
    for key, value in data.items():
        setattr(transaction, key, value)
    transaction.save()
    return transaction

def delete_transaction(id) -> None:
    transaction = get_transaction_by_id(id)
    transaction.delete()