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
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(default='logo.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def budget(self):
        orders = Order.objects.filter(customer=self)
        total_price = 0
        for order in orders:
            deleverd_order = orders.filter(status='Deliverd')
            if order in deleverd_order:
                total_price+= order.price
        return self.wallet + total_price

    def paid(self):
        orders = Order.objects.filter(Customer=self)
        paid_order = orders.filter(status='Deliverd&paid')
        paid = 0
        for order in paid_order:
            paid += order.price
        self.wallet -= paid
        return self.wallet



    def discount(self):
        orders = Order.objects.filter(customer=self)

        total_orders = orders.count()
        total_gifts = total_orders // 10
        for order in orders:
            if order.gifts is True:
                self.gifts -= 1
        return self.gifts + total_gifts

    def __str__(self):
        return self.name


class Client(models.Model):
    STATUS = (
        ('FB','Facebook'),
        ('IN','Insrgram'),
    )
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11,null=True)
    location = models.CharField(max_length=200, null=True)
    platform = models.CharField(max_length=20, null=True, choices=STATUS)
                

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=200)
    platform = (
        ('FB', 'Facebook'),
        ('IN', 'Instgram'),
    )
    phone = models.CharField(max_length=11)
    price = MoneyField(max_digits=14, decimal_places=0, default_currency='IQD')
    STATUS = (
        ('At Store', 'At Store'),
        ('In Stock', 'In Stock'),
        ('Shipping', 'Shipping'),
        ('Deliverd', 'Deliverd'),
        ('Rejected', 'Rejected'),
        ('Problem', 'Problem'),
        ('D&P', 'Deliverd&paid')
    )
    type = (
        ('Books', 'Books'),
        ('Clothes', 'Clothes'),
        ('Makeup', 'Makeup'),
    )
    gifts = models.BooleanField(default=False)
    location = models.CharField(max_length=100)
    note = models.CharField(max_length=1000, null=True, blank=True)
    customer = models.ForeignKey(Customer,
                                 null=True,
                                 related_name='order',
                                 on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # date_delivered = models.DateTimeField(auto_now=False, null=True, .now())
    platform = models.CharField(max_length=20, null=True, choices=platform)
    type = models.CharField(max_length=20, null=True, choices=type, default='Books')
    status = models.CharField(max_length=20, null=True, choices=STATUS, default='At Store')
    client = ForeignKey(Client,
                        null=True,
                        blank=True,
                        on_delete=models.SET_NULL,
                        )

    def __str__(self):
        return self.name
