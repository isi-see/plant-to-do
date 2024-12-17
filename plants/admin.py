from django.contrib import admin

from .models import Plant
from .models import Houseplant

# Register your models here.

class PlantAdmin(admin.ModelAdmin):
  list_display = ("nickname", "plant_type", "date_added",)


admin.site.register(Plant, PlantAdmin)

admin.site.register(Houseplant)