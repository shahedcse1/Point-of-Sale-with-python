# Generated by Django 4.0 on 2022-01-03 11:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseApp', '0005_alter_purchase_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='discount',
            field=models.IntegerField(default=0, max_length=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
