from django.core.management.base import BaseCommand
from apps.client.models import Client
import json

class Command(BaseCommand):
    help = 'Load a clients JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file'], 'r') as file:
            clients = json.load(file)
            for client_data in clients:
                Client.objects.create(**client_data)