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


class GenerateBillSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Revstreams
        fields='__all__'