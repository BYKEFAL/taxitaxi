import csv
from django.core.management.base import BaseCommand, CommandError
from etaxi.models import City

class Command(BaseCommand):
    help = 'Import CSV data into MyModel'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                mymodel = City()
                mymodel.name = row[0]
                mymodel.save()