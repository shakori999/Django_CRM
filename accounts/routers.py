from rest_framework import routers

from .viewsets import *


router = routers.DefaultRouter()
router.register('customers', CustomerViewSet, basename='customers')
router.register('clients', ClientViewSet, basename='clients')
router.register('orders', OrderViewSet, basename='orders')