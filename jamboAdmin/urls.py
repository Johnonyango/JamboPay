from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns=[
    url(r'^$',views.indexone,name='indexone'),
    # url(r'^signup/$', views.signup, name='signup'),
    url(r'^merchants/$',views.merchants,name='merchants'),
    url(r'^revenuestreams/$',views.revenueStreams,name='revenueStreams'),
    url(r'^payments/$',views.payments,name='payments'),
    url(r'^merchantbills/$',views.merchantBills,name='merchantBills'),
    url(r'^addEmployee/$',views.addEmployee,name='addEmployee'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)