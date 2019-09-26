from django.contrib import admin
from .models import *

# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import PasswordResetForm
# from django.utils.crypto import get_random_string
# from authtools.admin import NamedUserAdmin

admin.site.register(Merchant);
admin.site.register(Industry);
admin.site.register(Revstreams);
admin.site.register(Bills);
