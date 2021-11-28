from rest_framework import routers

from .viewsets import *


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('sign', SignViewSet, basename='sign')
router.register('customer', CustomerViewSet, basename='customer')
router.register('customers', CustomersViewSet, basename='customers')
router.register('clients', ClientViewSet, basename='clients')
router.register('orders', OrderViewSet, basename='orders')