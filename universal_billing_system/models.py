from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Industry(models.Model):
    name = models.CharField( blank=False,max_length= 40,default=None)
    def __str__(self):
        return self.name 
# class Category(models.Model):
#     name = models.CharField( blank=False,max_length= 40,default='JamboPay')
#     def __str__(self):
#         return self.name                    
class Revstreams(models.Model):
    name = models.CharField( blank=False,max_length= 40,default=None)
    # Category = models.ManyToManyField(Category)
    def __str__(self):
        return self.name
class Merchant(models.Model):
    Business_name = models.CharField(max_length=20,blank=False)
    Business_owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=60,blank=False)
    Physical_address = models.CharField(max_length=60,blank=False)
    Post_code = models.CharField(max_length=20,blank=False)
    Town = models.CharField(max_length=20,blank=False)
    JP_paybill = models.CharField(max_length=20,blank=False)
    Industry = models.ManyToManyField(Industry)
    Revstreams = models.ManyToManyField(Revstreams)
    join_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Business_name

class Bills(models.Model):
    customer_name = models.CharField(max_length=255,blank=False)
    customer_phone = models.CharField(max_length=255,blank=False)
    customer_email = models.EmailField(max_length=255,blank=False)
    Revstreams = models.ManyToManyField(Revstreams)
    narration = models.CharField(max_length=255,blank=False)
    amount = models.FloatField(blank=False)
    quantity = models.FloatField(blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    







