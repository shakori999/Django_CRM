# Generated by Django 3.2.9 on 2021-11-07 07:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_order_date_delivered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_delivered',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 7, 7, 11, 9, 576940, tzinfo=utc), null=True),
        ),
    ]
