from rest_framework import serializers 
from django.contrib.auth.models import User

from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                    'email', 'last_login', 'date_joined')
        read_only_fields = ('username','last_login', 'date_joined')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer 
        fields = ('name','address', 'phone','gifts', 'email' )
        read_only_fields = ('gifts',)



class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('name','phone','location', 'platform',)


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.StringRelatedField(many=False)
    client = serializers.StringRelatedField(many=False)
    class Meta:
        model = Order
        fields = ('customer','client','name','platform', 'phone', 'price', 'location', 'type')
    
    def create(self, validated_data):
        order = Order(**validated_data)
        order.customer = self.context['request'].user.customer
        try:
            order.client = Client.objects.get(
                                        phone = order.phone,
                                        )
        except Client.DoesNotExist:
            order.client = Client.objects.create(
                                            name=order.name,
                                            phone = order.phone,
                                            location = order.location,
                                            platform = order.platform,
                                        )
            order.client.save()    
        order.save()
        return order