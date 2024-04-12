from django.core.management.base import BaseCommand
from apps.products.models import Product
import json

class Command(BaseCommand):
    help = 'Import products from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path) as f:
            products = json.load(f)
            for product in products:
                Product.objects.create(**product)
        self.stdout.write(self.style.SUCCESS('Products imported successfully'))