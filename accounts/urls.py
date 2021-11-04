from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns =  [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>', views.customer, name='customer'),
]