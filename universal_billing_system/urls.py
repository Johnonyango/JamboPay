from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns=[
<<<<<<< HEAD
    url(r'^$',views.index,name='home'),
    
    #API Endpoints
    url(r'^api/GetMerchants/$', views.MerchantList.as_view()),
    url(r'^api/GetRevenueStreams/$', views.RevenueStreamsList.as_view()),
=======
    url(r'^$',views.index,name='Index'),
    url(r'^api/Merchants/$', views.MerchantList.as_view()),
    url(r'^api/BillsDetails/$', views.BillsDetails.as_view()),
    url(r'^index/$', views.index, name='home'),
    url(r'^bills/$', views.bills, name='bills'),
>>>>>>> cc45389c61b6940f2c6e1316381aeb1fb981ccf2
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)