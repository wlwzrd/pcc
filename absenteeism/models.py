from django.db import models

# Create your models here.
class Diagnosis(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)

class Disease(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    diagnosis = models.ForeignKey(Diagnosis)

class Area(models.Model):
    name = models.CharField(max_length=200)
    
class Organization(models.Model):
    name = models.CharField(max_length=200)
    area = models.ForeignKey(Area)

class Record(models.Model):
    employee__number = models.CharField(max_length=12)
    employee_name = models.CharField(max_length=20)
    employee_last_name = models.CharField(max_length=25)
    employee_age = models.CharField(max_length=2)
    #date = .... Complete me!
    disease = models.ForeignKey(Disease)
    organization = models.ForeignKey(Organization)
