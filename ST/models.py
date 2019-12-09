from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Latitude=models.FloatField(
            help_text=_('Latitude of sighting'),
            )
    Longitude=models.FloatField(
            help_text=_('Longtitude of sighting'),
            ) 
    Squirrel_ID=models.CharField(
            max_length=100,
            help_text=_('Uniqueid of sighting'),
            )
    AM='AM'
    PM='PM'
    
    SHIFT_CHOICES=(
            (AM,'AM'),
            (PM,'PM'),
            )
    shift=models.CharField(
            max_length=3,
            choices=SHIFT_CHOICES,
            )
    Date=models.DateField(
            help_text=_('sighting day'),
            )

    Adult='Adult'
    Juvenile='Juvenile'
    Question_mark='?'
    AGE_CHOICES=(
            (Adult,'Adult'),
            (Juvenile,'Juvenile'),
            (Question_mark,'?'),
            )

    Age=models.CharField(
            max_length=10,
            choices=AGE_CHOICES,
            )

    Gray='Gray'
    Cinnamon='Cinnamon'
    Black='Black'
    FUR_COLOR_CHOICES=(
            (Gray,'Gray'),
            (Cinnamon,'Cinnamon'),
            (Black,'Black'),
            )
    Primary_Fur_Color=models.CharField(
            max_length=30,
            choices=FUR_COLOR_CHOICES,
            )

    Ground_Plane='Ground Plane'
    Above_Ground='Above Ground'
    LOCATION_CHOICES=(
            (Ground_Plane,'Ground_Plane'),
            (Above_Ground,'Above_Ground'),
            )
    LOCATION=models.CharField(
            max_length=30,
            choices=LOCATION_CHOICES,
            )

    Specific_location=models.CharField(
            max_length=100,
            )

    Running=models.BooleanField()

    Chasing=models.BooleanField()

    Climbing=models.BooleanField()

    Eating=models.BooleanField()

    Foraging=models.BooleanField()

    Other_Activities=models.CharField(
            max_length=100,
            )

    Kuks=models.BooleanField()

    Quaas=models.BooleanField()

    Moans=models.BooleanField()

    Tail_flags=models.BooleanField()

    Tail_twitches=models.BooleanField()

    Approaches=models.BooleanField()

    Indifferent=models.BooleanField()

    Runs_form=models.BooleanField()

    def __str__(self):
        return self.Squirrel_ID
# Create your models here.
