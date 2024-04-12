from django.core.management.base import BaseCommand
from apps.transactions.models import Transaction
import json

class Command(BaseCommand):
    help = 'Import transactions from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path) as f:
            transactions = json.load(f)
            for transaction in transactions:
                Transaction.objects.create(**transaction)
        self.stdout.write(self.style.SUCCESS('Transactions imported successfully'))