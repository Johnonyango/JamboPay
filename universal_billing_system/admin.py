from django.contrib import admin
from .models import *

# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import PasswordResetForm
# from django.utils.crypto import get_random_string
# from authtools.admin import NamedUserAdmin

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
