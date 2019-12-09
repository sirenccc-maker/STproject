import csv
from django.core.management.base import BaseCommand
from ST.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self,*arg,**options):
        with open(options['csv_file']) as fp:
            reader=csv.DictReader(fp)
            data=list(reader)
            for item in data:
                item['Date']=item['Date'][-4:]+'-'+item['Date'][0:2]+'-'+item['Date'][-6:-4]
                s=Squirrel(
                        Latitude=item['Y'],
                        Longitude=item['X'],
                        Squirrel_ID=item['Unique Squirrel ID'],
                        shift=item['Shift'],
                        Date=item['Date'],
                        Age=item['Age'],
                        Primary_Fur_Color=item['Primary Fur Color'],
                        LOCATION=item['Location'],
                        Specific_location=item['Specific Location'],
                        Running=(item['Running']=='true'),
                        Chasing=(item['Chasing']=='true'),
                        Climbing=(item['Climbing']=='true'),
                        Eating=(item['Eating']=='true'),
                        Foraging=(item['Foraging']=='true'),
                        Other_Activities=item['Other Activities'],
                        Kuks=(item['Kuks']=='true'),
                        Quaas=(item['Quaas']=='true'),
                        Moans=(item['Moans']=='true'),
                        Tail_flags=(item['Tail flags']=='true'),
                        Tail_twitches=(item['Tail twitches']=='true'),
                        Approaches=(item['Approaches']=='true'),
                        Indifferent=(item['Indifferent']=='true'),
                        Runs_from=(item['Runs from']=='true'),
                        )
                s.save()

