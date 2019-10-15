from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .models import  *
from rest_framework import status
# from .models import *
from universal_billing_system.models import *
import requests
from django.http import HttpResponse,Http404,HttpResponseRedirect
from jamboAdmin.forms import SignUpForm
from .email import *
from universal_billing_system.emails import *
from .forms import *
from universal_billing_system.forms import *
from django.contrib import messages
# from django.shortcuts import get_object_or_404, redirect, render

# @login_required(login_url='/accounts/login/')
# def new_bill(request):
#     current_user = request.user
#     if request.method == "POST":
#         form = BillsForm(request.POST, request.FILES)
#         if form.is_valid():
#             bill = form.save(commit=False)
#             bill.generated_by=current_user
#             bill.save()

#         # if request.method=="POST":
#         # form =BillsForm(request.POST)
#         # if form.is_valid():
#             name = form.cleaned_data.get('customer_name')
#             email = form.cleaned_data.get('customer_email')
#             amount = form.cleaned_data.get('amount')
#             quantity = form.cleaned_data.get('quantity')

#         #     name = request.POST.get('customer_name')
#         #     email = request.POST.get('customer_email')
#             recipient = NewsLetterRecipients(name=name, email=email,amount=amount,quantity=quantity)
#             recipient.save()
#             send_notification(name, email,amount=amount,quantity=quantity)
#             # recipient = NewsLetterRecipients(name = name,email =email)
#             # send_notification(name = name, email = email)


#         return HttpResponseRedirect('/index')

#     else:
#         form = BillsForm()

#     return render(request, 'bills/new-bill.html', {"form": form})



def signup(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            # user = form.save()
            # auth_login(request, user)

            name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password1') 
            form.save()

            # amount=1
            # quantity=1
            # recipient = NewsLetterRecipients(name=name, email=email,amount=amount,quantity=quantity)
            # recipient.save()
            send_message(name, email)
            return redirect('indexone')
    else:
        form = merchantUSers()

#     return render(request, 'registration/registration_form.html', {'form': form})

def indexone(request):
    return render(request, 'indexone.html')

@login_required(login_url='/accounts/login/')
def merchants(request):
    url = ('http://127.0.0.1:8000/api/GetMerchants')
    headers = {'Authorization': 'Token 03e98652e6a64747f2bfa4f3896f1b52a76aaa44'}
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
        
    return render(request, 'merchants.html', {'details': details})

@login_required(login_url='/accounts/login/')
def revenueStreams(request):
    url = ('http://127.0.0.1:8000/api/GetRevenueStreams')
    headers = {'Authorization': 'Token 03e98652e6a64747f2bfa4f3896f1b52a76aaa44'}
    response = requests.get(url, headers=headers)
    details = response.json()
    for detail in details:
        id= detail.get('id')
        name = detail.get('name')
    return render(request, 'revenueStreams.html', {'details': details})


def payments(request):
    url = ('http://127.0.0.1:8000/api/GetPayments/')
    headers = {'Authorization': 'Token 03e98652e6a64747f2bfa4f3896f1b52a76aaa44'}
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
    headers = {'Authorization': 'Token 03e98652e6a64747f2bfa4f3896f1b52a76aaa44'}
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




@login_required
def addEmployee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            
            name=form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1') 
            form.save()

            welcome_email(name,email, password)

            messages.success(request,'Employee added succesfully')
            return redirect('managersite')

    else:

        form=AddEmployeeForm()

    return render(request, 'admin/add_employee.html', {'form': form})
