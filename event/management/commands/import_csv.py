import pandas as pd
from django.core.management.base import BaseCommand
from event.models import Organiser

class Command(BaseCommand):
    help = 'D:\Jigisha\Projects\EventPlanning\eventplanning\event_data.csv'

    def add_arguments(self, parser):
        parser.add_argument('D:\Jigisha\Projects\EventPlanning\eventplanning\event_data.csv', type=str, help='D:\Jigisha\Projects\EventPlanning\eventplanning\event_data.csv')

    def handle(self, *args, **options):
        csv_file_path = options['D:\Jigisha\Projects\EventPlanning\eventplanning\event_data.csv']

        # Read the CSV file using pandas
        df = pd.read_csv(csv_file_path)

        # Loop through the rows and create objects for the model
        for index, row in df.iterrows():
            Organiser.objects.create(
                name_of_event=row['name_of_event'],
                description=row['description'],
                department=row['department'],
                for_batch=row['for_batch'],
                event_date=row['event_date'],
                venue=row['venue'],
                time=row['time'],
                mode=row['mode'],
                event_type=row['event_type']
            )

        self.stdout.write(self.style.SUCCESS('CSV file imported successfully!'))
