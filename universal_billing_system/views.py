from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
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



# Create your views here.
def index(request):
    url = ('jpaye.herokuap.com/api/GetMerchants/')
    response = requests.get(url)
    print(response)
   
def index(request):
    return render(request, 'index.html')
        # url = 'http://127.0.0.1:8080/api/Merchants/'
        # r = requests.get(url.format()).json()
        # mechant = r['all_merchants']
        # print(r.all_merchants)
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
        # r = requests.get(url.format(Business_name)).json()
        # merchant_details = {
        # "Business_name":'r.main', 
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
        # return render(request,'index.html')

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
