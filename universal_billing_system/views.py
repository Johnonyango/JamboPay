from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  *
from .serializer import *
from .permissions import IsAdminOrReadOnly
from rest_framework import status
import requests
from . models import Merchant





# Create your views here.

def index(request):
        # url = 'http://127.0.0.1:8000/api/Merchants/'
        # r = requests.get(url.format()).json()
        # print(r.text)
        # merchant_details = []
        # for merchant_item in merchant:
        #     id = merchant_item.get('id')
        #     name = merchant_item.get('Business_name')
        #     email = merchant_item.get('email')
        #     Phone_number = merchant_item.get('Phone_number')
        #     address = merchant_item.get('Physical_address')
        #     code = merchant_item.get('Post_code'),
        #     Town = merchant_item.get('Town')
        #     paybill = merchant_item.get('JP_paybill')
        #     Industry = merchant_item.get('Industry')


        #     if name:
        #         merchant_object = Merchant(id,name,email,Phone_number,address,code,Town, paybill,Industry)
        #         merchant_details.append(merchant_object)
                
        # return render(request, "index.html", {"details": merchant_details})
        # url = 'http://127.0.0.1:8000/api/Merchants/'
        # Business_name = 'Vinka'
        # response = requests.get(url.format(Business_name)).json()
        # merchant = {
        # "Business_name":'', 
        # "Email": '',
        # "Phone_number":'',
        # "Physical_address":'',
        # "Post_code":'',
        # "Town":'',
        # "JP_paybill":'',
        # "Industry":'',
        # } 
        # context = {
        #     'merchant' :merchant}
        return render(request,'index.html')

class MerchantList(APIView):
    def get(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        all_merchants = Merchant.objects.all()
        serializers = MerchantSerializer(all_merchants, many=True)
        return Response(serializers.data)
