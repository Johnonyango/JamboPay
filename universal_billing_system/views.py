from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .models import  *
from .serializer import *
from .permissions import IsAdminOrReadOnly
from rest_framework import status
import requests
import openpyxl

# from .forms import *
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


# Create your views here.
# def index(request):
#     url = ('jpaye.herokuap.com/api/GetMerchants/')
#     response = requests.get(url)
#     print(response)
   
# def index(request):
#     return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv")
    else:
        form = UploadFileForm()
    return render_to_response('index.html', {'form': form}, context_instance=RequestContext(request))      

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
    return render(request, 'merchants.html', {'details': details})



def upload(request):
    if "GET" == request.method:
        return render(request, 'upload.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting all sheets
        sheets = wb.sheetnames
        # print(sheets)

        # getting a particular sheet
        worksheet = wb["Sheet1"]
        # print(worksheet)

        # getting active sheet
        active_sheet = wb.active
        # print(active_sheet)

        # reading a cell
        print(worksheet["A1"].value)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
                print(cell.value)
            excel_data.append(row_data)

        return render(request, 'upload.html', {"excel_data":excel_data})  
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

