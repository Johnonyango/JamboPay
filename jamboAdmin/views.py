from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .models import *
from rest_framework import status
from universal_billing_system .models import *
import requests
from django.http import HttpResponse, Http404, HttpResponseRedirect
from jamboAdmin.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('indexone')
    else:
        form = SignUpForm()

    return render(request, 'registration/registration_form.html', {'form': form})


def indexone(request):
    return render(request, 'indexone.html')


@login_required(login_url='/accounts/login/')
def merchants(request):
    url = ('http://127.0.0.1:8000/api/GetMerchants')
    headers = {'Authorization': 'Token b76be7fe9c4ecd62b0e003661426ccbe6cd01d05'}
    response = requests.get(url,headers=headers)
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


def sign(request):
    current_user = request.user
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            merchant = form.save(commit=False)
            merchant.save()

            name = form.cleaned_data.get('Business_owner')
            email = form.cleaned_data.get('email')
        
            recipient = Merchant(name=Business_owner, email=email)
            recipient.save()
            send_message(name, email)
            
