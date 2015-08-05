from django.contrib import admin

# Register your models here.

from .models import Diagnosis, Disease, Area, Organization, Employee, Record

admin.site.register(Diagnosis)
admin.site.register(Disease)
admin.site.register(Area)
admin.site.register(Organization)
admin.site.register(Employee)
admin.site.register(Record)
