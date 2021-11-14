# Generated by Django 3.2.9 on 2021-11-13 16:03

from decimal import Decimal
from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_order_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='wallet',
            field=djmoney.models.fields.MoneyField(decimal_places=0, default=Decimal('0'), default_currency='IQD', max_digits=14),
        ),
    ]
