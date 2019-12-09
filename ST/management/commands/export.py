# Create
import csv
from django.core.management.base import BaseCommand 
from ST.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
	    parser.add_argument('csv_path')

    def handle(self,*arg,**options):
        csv_path=str(options['csv_path'])

        csv_data=['Latitude','Longitude','Squirrel_ID','shift','Date','Age',
                    'Primary_Fur_Color','LOCATION','Specific_location','Running','Chasing',
                    'Climbing','Eating','Foraging','Other_Activities','Kuks','Quaas','Moans',
                    'Tail_flags','Tail_twitches','Approaches','Indifferent','Runs_from']
        fp=open(csv_path,'w')
        writer=csv.writer(fp)
        writer.writerow(csv_data)
        squirrels=Squirrel.objects.all()
        for squirrel in squirrels:
            row =writer.writerow([getattr(squirrel, field) for field in csv_data])
        fp.close()
