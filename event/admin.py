from django.contrib import admin

# Register your models here.
from .models import Event,Contributer
admin.site.register(Event)
admin.site.register(Contributer)