# yourapp/management/commands/import_csv.py
import csv
from django.core.management.base import BaseCommand
from your_leads.models import TeleModel

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Specify the CSV file path')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        self.import_data(csv_file)

    def import_data(self, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                TeleModel.objects.create(
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    address=row['address'],
                    city=row['city'],
                    county=row['county'],
                    state=row['state'],
                    zip=row['zip'],
                    phone=row['phone'],
                    gender=row['gender'],
                    ethnicity=row['ethnicity'],
                    ownrent=row['ownrent'],
                    latitude=row['latitude'],
                    longitude=row['longitude'],

                    # ... map other fields accordingly
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
