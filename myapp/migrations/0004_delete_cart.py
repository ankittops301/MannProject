# Generated by Django 4.0.4 on 2022-05-13 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_order_orderdetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
