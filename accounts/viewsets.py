from types import prepare_class
from rest_framework import viewsets 
from rest_framework import permissions
from django.contrib.auth.models import User

from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.filter(id=self.request.user.customer.id)

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes =[permissions.IsAdminUser] 

    def get_queryset(self):
        return Client.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer 
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.customer.order_set.all()
     