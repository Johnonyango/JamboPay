from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .models import  *
from rest_framework import status
import requests
from django.http import HttpResponse,Http404,HttpResponseRedirect
from jamboAdmin.forms import SignUpForm
# from .forms import SignupForm
#sign up other users
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('indexone')
#     else:
#         form = SignUpForm()

#     return render(request, 'registration/register.html', {'form': form})

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
    headers = {'Authorization': "7ec8ee9b01c16dcc9a3df741570a790cc3501bda"}
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
