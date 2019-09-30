from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns=[
    url(r'^$',views.merchants,name='merchants'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)