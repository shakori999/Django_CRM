from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import ModelForm 
from django import forms
# from django.contrib.auth.models import User

from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class UpdateOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'status',
        ]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

class CreateClientForm(ModelForm):
    class Meta:
        models = Client
        fields = [
            'name',
            'phone',
            'location',
            'platform',
        ]