from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='Index'),
<<<<<<< HEAD
    url(r'^api/Merchants/$', views.MerchantList.as_view()),
    url(r'^index/$', views.index, name='home'),
    url(r'^bills/$', views.bills, name='bills'),
=======

    #API Endpoints
    url(r'^api/GetMerchants/$', views.MerchantList.as_view()),
    url(r'^api/GetRevenueStreams/$', views.RevenueStreamsList.as_view()),
>>>>>>> bf621a909233d23a6c7d95334fbb43fac14d3c7c
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)