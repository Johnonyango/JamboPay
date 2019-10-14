from django.db import models
from django.contrib.auth.models import User


class NewsLetterRecipientss(models.Model):
    name = models.CharField(max_length = 30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
