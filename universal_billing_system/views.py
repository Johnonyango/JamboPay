from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  *
from .serializer import *
from .permissions import IsAdminOrReadOnly
from rest_framework import status
import requests



# Create your views here.

def index(request):
        url = 'http://127.0.0.1:8000/api/Merchants/'
        response = requests.get(url.format(merchant)).json
        merchant = {
          "id": 
        "Business_name": 
        "Email": 
        "Phone_number":
        "Physical_address": 
        "Post_code": 
        "Town":
        "JP_paybill":
        "Industry": 
        }
        return render(request,'index.html')

class MerchantList(APIView):
    def get(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        all_merchants = Merchant.objects.all()
        serializers = MerchantSerializer(all_merchants, many=True)
        return Response(serializers.data)
