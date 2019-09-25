from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  *
from .serializer import *
from .permissions import IsAdminOrReadOnly
from rest_framework import status
import requests



# Create your views here.

def index(request):
    # if request.method == "GET":
    #         form = SubmitEmbed(request.POST)
    #         if form.is_valid():
    #             url = form.cleaned_data['url']
    #             r = requests.get('http://api.embed.ly/1/oembed?key=' + settings.EMBEDLY_KEY + '&url=' + url)
    #             json = r.json()
    #             serializer = EmbedSerializer(data=json)
    #             if serializer.is_valid():
    #                 embed = serializer.save()
    #                 return render(request, 'embeds.html', {'embed': embed})    return render(request,'index.html')
    pass

class MerchantList(APIView):
    def get(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        all_merchants = Merchant.objects.all()
        serializers = MerchantSerializer(all_merchants, many=True)
        return Response(serializers.data)
