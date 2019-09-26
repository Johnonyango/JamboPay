from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .models import  *
from .serializer import *
from .permissions import IsAdminOrReadOnly
from rest_framework import status
from . models import Merchant
# from .forms import *


# login
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

@login_required(login_url='register')
def logout_view(request):
   logout(request)
   return redirect('login')


def index(request):
    return render(request, 'index.html')
       

def bills(request):
    return render(request, 'bills.html')

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
class BillsDetails(APIView):
    def get(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        all_bills = Bills.objects.all()
        serializers = BillSerializer(all_bills, many=True)
        return Response(serializers.data)        
