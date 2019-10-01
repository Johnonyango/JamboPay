from django.contrib import admin
from .models import *



class MerchantAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'amount', 'quantity')

class IndustryAdmin(admin.ModelAdmin):
    list_display =('name')

class RevstreamsAdmin(admin.ModelAdmin):
    list_display = ('name')

class BillsAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_phone')

admin.site.register(Merchant);
admin.site.register(Industry);
admin.site.register(Revstreams);
admin.site.register(Bills);
admin.site.register(Payments);

