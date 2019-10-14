from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .models import  *
from rest_framework import status
from .models import *
import requests
from django.http import HttpResponse,Http404,HttpResponseRedirect
from jamboAdmin.forms import SignUpForm
from .email import *
from .forms import *


def signup(request):
    if request.method == 'POST':
        form = merchantUSers(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            recipient = NewsLetterRecipientss(name=name, email=email)
            recipient.save()
            send_message(name, email)
            return redirect('indexone')
    else:
        form = merchantUSers()

    return render(request, 'registration/registration_form.html', {'form': form})

def indexone(request):
    return render(request, 'indexone.html')

@login_required(login_url='/accounts/login/')
def merchants(request):
    url = ('http://127.0.0.1:8000/api/GetMerchants')
    headers = {'Authorization': 'Token 88ead485afc9666e1c6a3367ad90fde8a2889e7a'}
    response = requests.get(url, headers=headers)
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
        Revstreams = detail.get('Revstreams')

    return render(request, 'merchants.html', {'details': details})

@login_required(login_url='/accounts/login/')
def revenueStreams(request):
    url = ('http://127.0.0.1:8000/api/GetRevenueStreams')
    headers = {'Authorization': 'Token 88ead485afc9666e1c6a3367ad90fde8a2889e7a'}
    response = requests.get(url, headers=headers)
    details = response.json()
    for detail in details:
        id= detail.get('id')
        name = detail.get('name')
    return render(request, 'revenueStreams.html', {'details': details})


def payments(request):
    url = ('http://127.0.0.1:8000/api/GetPayments/')
    headers = {'Authorization': 'Token 88ead485afc9666e1c6a3367ad90fde8a2889e7a'}
    response = requests.get(url,headers=headers)
    details = response.json()
    for detail in details:
        id = detail.get('id')
        bill_number = detail.get('bill_number')
        payers_name = detail.get('payers_name')
        payers_phone = detail.get('payers_phone')
        narration = detail.get('narration')
        amount = detail.get('amount')
        pay_date = detail.get('pay_date')
    return render(request, 'payments.html', {'details': details})



def merchantBills(request):
    url = ('http://127.0.0.1:8000/api/BillsDetails/')
    headers = {'Authorization': 'Token 88ead485afc9666e1c6a3367ad90fde8a2889e7a'}
    response = requests.get(url,headers=headers)
    details = response.json()
    for detail in details:
        id = detail.get('id')
        customer_name = detail.get('customer_name')
        customer_phone = detail.get('customer_phone')
        customer_email = detail.get('customer_email')
        narration = detail.get('narration')
        quantity = detail.get('quantity')
        amount = detail.get('amount')
        post_date = detail.get('post_date')
        due_date = detail.get('due_date')
        generated_by = detail.get('generated_by')
        status = detail.get('status')
    return render(request, 'merchant_bills.html', {'details': details})
