from django.db import models
from absenteeism.signals import send_record
from django.db.models.signals import post_save

# Create your models here.
class Diagnosis(models.Model):
    """ A model to represent a diagnosis given by the doctor
    """
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(max_length=600)
    def __unicode__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    diagnosis = models.ForeignKey(Diagnosis,null=False)
    def __unicode__(self):
        return u'<Enf: %s (Dx: %s)>'%(self.name,self.diagnosis.name)

class Area(models.Model):
    """ A model to represent a department area inside the company
    """
    name = models.CharField(max_length=200,unique=True)
    def __unicode__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=200)
    area = models.ForeignKey(Area,null=False)
    def __unicode__(self):
        return self.name

class Employee(models.Model):
    """ A model to represent an employee. There is not employee
    authentication, is just a profile.
    """
    personal_number = models.CharField(max_length=12)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    age = models.CharField(max_length=2)
    organization = models.ForeignKey(Organization)
    def __unicode__(self):
        return u'Nombre: %s -  Apellido: %s'%(self.name,self.last_name)

class DiagnosisType(models.Model):
    """
    """
    TYPES = (('AT','Accidente de Trabajo'),('EC','Enfermedad Cronica'))
    name = models.CharField(max_length=2, choices=TYPES)
    def __unicode__(self):
        return self.name

class Record(models.Model):
    """ A model to represent a normal record when a employee go 
    to the physical condiotioning centre. The doctor gives diagnosis 
    according to the disease.
    """
    employee = models.ForeignKey(Employee,null=False)
    date = models.DateTimeField()
    disease = models.ForeignKey(Disease,null=False)
    diagnosis_type = models.ForeignKey(DiagnosisType, null=True, default=None)
    def __unicode__(self):
        return u'Nombre: %s Dx: %s'%(self.employee.name,self.disease.diagnosis.name)
post_save.connect(send_record, sender=Record)
