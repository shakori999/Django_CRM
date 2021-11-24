from rest_framework import viewsets 
from rest_framework import permissions

from .models import *
from .serializers import *

class UserviewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]



class OrderViewSet(viewsets.ModelViewSet):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.customer.order_set.all()