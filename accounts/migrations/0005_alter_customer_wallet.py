# Generated by Django 3.2.9 on 2021-11-12 05:22

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customer_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='wallet',
            field=djmoney.models.fields.MoneyField(decimal_places=0, default_currency='IQD', editable=False, max_digits=14, null=True),
        ),
    ]