from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


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

