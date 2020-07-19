from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    #url(r'^$', views.order_confirmation, name='order_confirmation'),
    path('orders/<order>/', views.order_confirmation, name='order_confirmation'),
]

#^\/\S+\s[0-9]*\/$
#r'^(?P<order>[^\/]*)/$'