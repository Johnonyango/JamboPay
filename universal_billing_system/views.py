from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .models import  *
from .serializer import *
from .permissions import IsAdminOrReadOnly
from rest_framework import status
import requests
from .forms import *
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .email import send_welcome_email


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


@login_required
def profile(request):

   user = request.user
   images = Image.objects.filter(author=user.profile)

   context = {
      'user': user,
      'images': images
   }

   return render(request, 'timeline/profile.html', context)

# Create your views here.
# def index(request):
#     url = ('jpaye.herokuap.com/api/GetMerchants/')
#     response = requests.get(url)
#     print(response)
   
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
class GenerateBill(APIView):
    # def get(self, request, format=None):
    #     all_bills = Bills.objects.all()
    #     serializers = GenerateBillSerializer(all_bills, many=True)
    #     return Response(serializers.data)
    def post(self, request, format=None):
        serializers = BillSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)
class BillsDetails(APIView):
    def get(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        all_bills = Bills.objects.all()
        serializers = BillSerializer(all_bills, many=True)
        return Response(serializers.data)


class GetBillDetails(APIView):

    def get_bill(self, pk):
        try:
            return Bills.objects.get(pk=pk)
        except Bills.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        bill = self.get_bill(pk)
        serializers = BillSerializer(bill)
        return Response(serializers.data)


def search_results(request):
    if 'customer' in request.GET and request.GET["customer"]:
        search_term = request.GET.get("customer")
        searched_customers = Customer.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"customer": searched_customer})

    else:
        message = "You haven't searched for any term."
        return render(request, 'search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def merchants(request):
    url = ('http://127.0.0.1:8000/api/BillsDetails')
    response = requests.get(url)
    details = response.json()
    for detail in details:
        Business_name = detail.get('Business_name')
        Email = detail.get('Email')
        Phone_number = detail.get('Phone_number')
        Address = detail.get('Physical_address')
        Code = detail.get('Post_code')
        Town = detail.get('Town')
        Pay_bill = detail.get('JP_paybill')
        Industry = detail.get('Industry')
    return render(request, 'customers.html', {'details': details})


@login_required(login_url='/accounts/login/')
def new_bill(request):
    current_user=request.user
    if request.method=="POST":
        form =BillsForm(request.POST,request.FILES)
        if form.is_valid():
            bill = form.save(commit = False)
            bill.save()
        
        # if request.method=="POST":
        # form =BillsForm(request.POST)
        # if form.is_valid():
        #     name = form.cleaned_data['customer_name']
        #     email = form.cleaned_data['customer_email']

        #     name = request.POST.get('customer_name')
        #     email = request.POST.get('customer_email')
        #     recipient = NewsLetterRecipients(name=name, email=email)
        #     recipient.save()
        #     send_welcome_email(name, email)

        return HttpResponseRedirect('/index')
    

    else:
        form = BillsForm()
    
    

    return render(request,'bills/new-bill.html',{"form":form})

