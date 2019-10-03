from rest_framework import serializers
from .models import *

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields='__all__'

class RevenueStreamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revstreams
        fields='__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields='__all__'      

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields='__all__'      
