from django.contrib import admin
from .models import *
from .forms     import *
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import PasswordResetForm
# from django.utils.crypto import get_random_string
# from authtools.admin import NamedUserAdmin


# User = get_user_model()

# class UserAdmin(NamedUserAdmin):
#     """
#     A UserAdmin that sends a password-reset email when creating a new user,
#     unless a password was entered.
#     """
#     add_form = UserCreationForm
#     add_fieldsets = (
#         (None, {
#             'description': (
#                 "Enter the new user's name and email address and click save."
#                 " The user will be emailed a link allowing them to login to"
#                 " the site and set their password."
#             ),
#             'fields': ('email', 'name',),
#         }),
#         ('Password', {
#             'description': "Optionally, you may set the user's password here.",
#             'fields': ('password1', 'password2'),
#             'classes': ('collapse', 'collapse-closed'),
#         }),
#     )


# admin.site.unregister(Merchant)
admin.site.register(Merchant)
admin.site.register(Industry)
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)