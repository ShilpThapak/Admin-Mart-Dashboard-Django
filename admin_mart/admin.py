from django.contrib import admin
from django.db.models.lookups import In
from .models import Incident

# Register your models here.
admin.site.register(Incident)