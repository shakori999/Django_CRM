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

    class Meta:
        model = User 
        fields = ('username', )


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('name','platform', 'phone', 'price', 'location', 'type')