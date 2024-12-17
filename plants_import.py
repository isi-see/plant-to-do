# !!do not execute this script; instead copy the code into shell directly! more reliable; access to settings.

#import os
#import django
import csv
from plants.models import Houseplant

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planttracker.settings')
#django.setup()
#print(os.environ.get('DJANGO_SETTINGS_MODULE'))


def import_houseplants(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        print(f"CSV headers: {headers}")  # Check the headers
        for row in reader:
            print("i am working")
            Houseplant.objects.create(
                latin_name=row['latin_name'],
                common_name=row['common_name'],
                description=row['description'],
                plant_image=row['plant_image'],
                light_needed=row['light_needed']
    )

#if __name__ == '__main__':
csv_file_path = '/home/iseeger/django_projects/planttracker/plants/static/plants/common-houseplants-data.csv'
import_houseplants(csv_file_path)





