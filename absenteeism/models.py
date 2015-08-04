from django.db import models

# Create your models here.
class Diagnosis(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(max_length=600)
    def __unicode__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    diagnosis = models.ForeignKey(Diagnosis,null=False)
    def __unicode__(self):
        return u'<Disease: %s (diagnosis: %S)>'%(self.name,self.diagnosis.name)

class Area(models.Model):
    name = models.CharField(max_length=200,unique=True)
    def __unicode__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=200)
    area = models.ForeignKey(Area,null=False)
    def __unicode__(self):
        return self.name

class Employee(models.Model):
    personal_number = models.CharField(max_length=12)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    age = models.CharField(max_length=2)
    organization = models.ForeignKey(Organization)
    def __unicode__(self):
        return u'Nombre: %s  Apellido: %s'%(self.name,self,last_name)

class Record(models.Model):
    employee = models.ForeignKey(Employee,null=False)
    date = models.DateTimeField()
    disease = models.ForeignKey(Disease,null=False)
    def __unicode__(self):
        return u'N: %s E: %s'%(self.employee.name,self.disease.name)
