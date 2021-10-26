from django.db import models

# Create your models here.
class Lead(models.Model):
    # SOURCES_CHOICES = (
    #     ('INST', 'INSTGRAM'),
    #     ('FB', 'FACEBOOK')
    # )
    # STATUS_CHOICE = (
    #     ('AT STORE','AT STORE'),
    #     ('IN STOCK','IN STOCK'),
    #     ('SHIPPING','SHIPPING'),
    #     ('DELIVERED','DELIVERED'),
    #     ('REJECTED','REJECTED'),
    #     ('PROBLEM','PROBLEM'),
    # )
    # TYPE_CHOICES = (
    #     ('GF','GIFTS'),
    #     ('BKS','BOOKS'),
    #     ('CLTHS','CLOTHES'),
    # )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    adress = models.CharField(max_length=100)
    phone = models.IntegerField(default= 0)
    price = models.IntegerField(default=0)
    # platform = models.CharField(choices=SOURCES_CHOICES, max_length=8, default=None)
    # status = models.CharField(choices=STATUS_CHOICE, max_length=9, default=None)
    # type = models.CharField(choices=TYPE_CHOICES, max_length=8, default=None) 
