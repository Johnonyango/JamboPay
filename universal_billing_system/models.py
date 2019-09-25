from django.db import models

# Create your models here.
class Merchants(models.Model):
    Business_name = models.TextField(max_length=60,blank=False)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=60,blank=False)
    Physical_address = models.TextField()
    Post_code = models.CharField(max_length=20,blank=False)
    Town = models.TextField(max_length=30,blank=False)
    Industry = models.TextField(max_length=30,blank=False)
    JP_paybill = models.CharField(max_length=10,blank=False)
 