from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  *
from .serializer import *
from .permissions import IsAdminOrReadOnly
from rest_framework import status
from rest_framework.decorators import api_view

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def index(request):
    
    return render(request,'index.html')


class MerchantList(APIView):
    def get(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        all_merchants = Merchant.objects.all()
        serializers = MerchantSerializer(all_merchants, many=True)
        return Response(serializers.data)
    
class RevenueStreamsList(APIView):
    def get(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        all_revenue_streams = Revstreams.objects.all()
        serializers = RevenueStreamsSerializer(all_revenue_streams, many=True)
        return Response(serializers.data)
    



