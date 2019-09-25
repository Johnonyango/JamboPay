from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  *
from .serializer import *


# Create your views here.

def index(request):
    
    return render(request,'index.html')


class MerchantList(APIView):
    def get(self, request, format=None):
        # all_merchants = Merchant.objects.all()
        serializers = MerchantSerializer(all_merch, many=True)
        return Response(serializers.data)
