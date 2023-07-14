from django.contrib import admin
# import your models here
from .models import Coffee, Maker

# Register your models here
admin.site.register(Coffee)
admin.site.register(Maker)