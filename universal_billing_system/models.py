from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Industry(models.Model):
    name = models.CharField( blank=False,max_length= 40,default=None)
    def __str__(self):
        return self.name 
                          
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
    Status=(
    (0,'Unpaid'),
    (1,'Paid'),
    )

    customer_name = models.CharField(max_length=255,blank=False)
    customer_phone = models.CharField(max_length=255,blank=False)
    customer_email = models.EmailField(max_length=255,blank=False)
    Revstreams = models.ManyToManyField(Revstreams,default=0)
    narration = models.CharField(max_length=255,blank=False)
    amount = models.FloatField(blank=False)
    quantity = models.FloatField(blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=Status,default=0)


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Payments(models.Model):
    bill_number = models.ForeignKey(Bills,on_delete=models.CASCADE,default=None)
    payers_name = models.CharField(max_length=255,blank=False)
    payers_phone = models.CharField(max_length=255,blank=False)
    narration = models.CharField(max_length=255,blank=False)
    amount = models.FloatField(blank=False)
    pay_date = models.DateTimeField(auto_now_add=True)

    def save_bill(self):
        self.save()
 
 