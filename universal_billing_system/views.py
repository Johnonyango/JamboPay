from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout


# Create your views here.

def index(request):
    
    return render(request,'index.html')

def login(request):
    return render(request, 'register/login.html')

@login_required(login_url='register')
def logout_view(request):
   logout(request)
   return redirect('login')