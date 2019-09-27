from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns=[
    # url(r'^$',views.index,name='home'),
    url(r'^$',views.merchants,name='merchants'),
    #API Endpoints
    url(r'^api/GetMerchants/$', views.MerchantList.as_view()),
    url(r'^api/GetRevenueStreams/$', views.RevenueStreamsList.as_view()),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)