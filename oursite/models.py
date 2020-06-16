from django.db import models
from django.utils import timezone

# Create your models here.


class Contact_us(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    subject = models.CharField( max_length=50)
    message = models.CharField(max_length=500)
    def __str__(self):
        return (self.firstname,self.lastname,self.email,self.subject,self.message)


class SubscribeModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
    status = models.CharField(max_length=64, null=False, blank=True)
    created_date = models.DateTimeField(null=False, blank=True)
    updated_date = models.DateTimeField(null=False, blank=True)

    class Meta:
        app_label = "appname"
        db_table = "appname_subscribe"

    def __str__(self):
        return self.email



