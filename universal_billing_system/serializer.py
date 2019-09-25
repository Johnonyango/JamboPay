from rest_framework import serializers
from .models import *

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields='__all__'
        # fields = ('name', 'description', 'price')