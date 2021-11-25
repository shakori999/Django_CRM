from rest_framework import viewsets 
from rest_framework import permissions
from rest_framework.decorators import action 

from .models import *
from .serializers import *

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-date_created')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAdminUser]
    

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=True, permission_classes=[permissions.IsAdminUser])
    def get_queryset(self):
        return Client.objects.all()




class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.customer.order_set.all()
     