# Generated by Django 3.2.9 on 2021-11-09 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_admin_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='admin',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
    ]