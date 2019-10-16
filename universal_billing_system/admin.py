from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


class MerchantAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'amount', 'quantity')

class IndustryAdmin(admin.ModelAdmin):
    list_display =('name')

class RevstreamsAdmin(admin.ModelAdmin):
    list_display = ('name')

class BillsAdmin(admin.ModelAdmin):
    list_display = ('amount', 'quantity')

admin.site.register(Merchant);
admin.site.register(Industry);
admin.site.register(Revstreams);
# admin.site.register(Bills);
admin.site.register(Payments);
@admin.register(Bills)
class viewAdmin(ImportExportModelAdmin):
    exclude = ('id',)
# class Merchant(models.Model):
#     exclude = ('Merchant_id',)

