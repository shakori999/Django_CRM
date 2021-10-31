from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns =  [
    path('', views.home),
    path('products/', views.products),
    path('customer/<str:pk>', views.customer),
]