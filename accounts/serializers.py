from django.db.models import fields
from rest_framework import serializers 

from .models import *

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # user = serializers.RelatedField(read_only=True)
    # name = serializers.CharField(required=False, allow_blank=True, max_length=30)
    # address = serializers.CharField(required=False, allow_blank=True, max_length=500)
    # gifts = serializers.IntegerField(read_only=True)
    # phone = models.CharField( max_length=11)
    # email = models.CharField(max_length=20, null=True)
    # profile_pic = serializers.ImageField(default='logo.png', )
    # orders = serializers.StringRelatedField(many=True)
    class Meta:
        model = Customer 
        fields = ('name','address', 'phone','gifts', 'email' )

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
        order.user = self.context['request'].user
        order.save()
        return order