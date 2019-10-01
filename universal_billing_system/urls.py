from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns=[
    url(r'^$',views.index,name='Index'),
    url(r'^merchants/$',views.merchants,name='merchants'),
    url(r'^index/$', views.index, name='home'),
    url(r'^bills/$', views.bills, name='bills'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^new/bill/$', views.new_bill, name='new-bill'),




    #API Endpoints
    url(r'^api/GetMerchants/$', views.MerchantList.as_view()),
    url(r'^api/GetRevenueStreams/$', views.RevenueStreamsList.as_view()),
    url(r'^api/GenerateBill/$', views.GenerateBill.as_view()),
    url(r'^api/BillsDetails/$', views.BillsDetails.as_view()),
    url(r'api/GetBillDetails/bill-id/(?P<pk>[0-9]+)/$',views.GetBillDetails.as_view()),
    url(r'^api/GetPayments/$', views.GetPayments.as_view()),


    url(r'^notification/$', views.notification, name='noteform'),

    #moreurls
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)