from django.db.models.signals import post_save
from absenteeism.keenio import get_keen_client

def send_record(sender, instance, created, **kwargs):
    """ Send the event collected data through the keen client

    If is a new object, the data will send to keen as a new record.
    If the object is already created, the data will be send to keen as an update
    """
    if created:
        client = get_keen_client()
        client.add_event("absenteeism_records",
                        {"pk":instance.pk,
                         "employee":{
                             "name":instance.employee.name,
                             "last_name":instance.employee.last_name,
                             "organization":{"name":instance.employee.organization.name,
                                             "area":instance.employee.organization.area.name},
                             "age":instance.employee.age
                         },
                         "disease":{
                             "name":instance.disease.name,
                             "diagnosis":instance.disease.diagnosis.name},
                         "date":{
                             "year":instance.date.year,
                             "month":instance.date.month,
                             "day":instance.date.day}
                     }
        )
        print "It is created"
    else:
        ## Do an update to the collection
        pass
