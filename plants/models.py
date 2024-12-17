from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime


class Houseplant(models.Model):
    """This is the reference model- stores different plant types and properties to be accessed via Plant
    source of Houseplant data: https://github.com/anjelicasilva/ispeakplantish/blob/master/seed_data/common-houseplants-data.csv
    """
    latin_name = models.CharField(max_length=50)
    common_name = models.CharField(max_length=50)
    description = models.TextField(max_length=800)
    plant_image_url = models.URLField(blank=True, null=True)
    light_needed = models.CharField(max_length=15)

    def __str__(self):
        return self.common_name

class Plant(models.Model):
    """Stores the individual plants added to the list and all their details. """
    ROOM_CHOICES = [
        ("BEDROOM", "Bedroom"),
        ("BATHROOM", "Bathroom"),
        ("LIVINGROOM", "Living room"),
        ("OFFICE", "Office"),
        ("HALLWAY", "Hallway"),
        ]

    SHORT_CADENCE = [
        ("1w", "1 week"),
        ("2w", "2 weeks"),
        ("4w", "4 weeks"),
        ("6w", "6 weeks")
        ]

    LONG_CADENCE = [
        ("1m", "1 month"),
        ("2m", "2 months"),
        ("4m", "4 months"),
        ("6m", "6 months"),
        ("1y", "1 year"),
        ]

    #create a dropdown selection from Houseplant to select what kind of plant it is
    plant_type = models.ForeignKey('Houseplant',
                                     on_delete=models.CASCADE,
                                     blank=True,
                                     null=True)
    nickname=models.CharField(
        max_length=200,
        validators=[MinLengthValidator(
                    3, "Plant name must contain at least 3 characters")])
    description=models.TextField(max_length=500)

    image = models.ImageField(upload_to='plants/', blank=True, null=True)

    room = models.CharField(max_length=15, choices=ROOM_CHOICES)

    # selecting the required schedule for tasks (dropdown):
    water_schedule = models.CharField(max_length=15, choices=SHORT_CADENCE,blank=True)

    fertilize_schedule = models.CharField(max_length=15, choices=LONG_CADENCE,blank=True)

    repot_schedule = models.CharField(max_length=15, choices=LONG_CADENCE, blank=True)

    # dates for when tasks were last completed, to be updated by user:
    date_last_watered = models.DateField(blank=True, null=True)

    date_last_fertilized = models.DateField(blank=True, null=True)

    date_last_repotted = models.DateField(blank=True, null=True)

    #when the new plant entry was created:
    date_added = models.DateField(default=datetime.now)

    #when the plant entry was last updated:
    date_last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.nickname} ({self.plant_type})"

