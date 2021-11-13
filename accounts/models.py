from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from djmoney.models.fields import MoneyField
# from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=500, null=True)
    wallet = MoneyField(max_digits=14,
                        decimal_places=0,
                        default_currency='IQD',
                        null=False,
                        editable=False,
                        default=0
                        )
    gifts = models.IntegerField(null=False, editable=False, default=0)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(default='logo.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    STATUS = (
        ('FB','Facebook'),
        ('IN','Insrgram'),
    )
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    location = models.CharField(max_length=200)
    platform = models.CharField(max_length=20, null=True, choices=STATUS)

class Order(models.Model):
    name = models.CharField(max_length=200)
    platform = (
        ('FB', 'Facebook'),
        ('IN', 'Instgram'),
    )
    phone = models.IntegerField()
    price = MoneyField(max_digits=14, decimal_places=0, default_currency='IQD')
    STATUS = (
        ('At Store', 'At Store'),
        ('In Stock', 'In Stock'),
        ('Shipping', 'Shipping'),
        ('Deliverd', 'Deliverd'),
        ('Rejected', 'Rejected'),
        ('Problem', 'Problem'),
    )
    type = (
        ('Books', 'Books'),
        ('Clothes', 'Clothes'),
        ('Makeup', 'Makeup'),
    )
    gifts = models.BooleanField(default=False)
    location = models.CharField(max_length=200)
    note = models.CharField(max_length=1000, null=True)
    customer = models.ForeignKey(Customer,
                                 null=True,
                                 on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # date_delivered = models.DateTimeField(auto_now=False, null=True, .now())
    platform = models.CharField(max_length=20, null=True, choices=platform)
    type = models.CharField(max_length=20, null=True, choices=type, default='Books')
    status = models.CharField(max_length=20, null=True, choices=STATUS, default='At Store')
    client = ForeignKey(Client,
                        null=True,
                        on_delete=models.SET_NULL,
                        )

    def __str__(self):
        return self.name
