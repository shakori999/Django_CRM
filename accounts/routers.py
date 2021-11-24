from rest_framework import routers

from .viewsets import *


router = routers.DefaultRouter()
router.register('users', UserviewSet, basename='users')
router.register('orders', OrderViewSet, basename='orders')