# Generated by Django 4.0 on 2022-01-04 05:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseApp', '0006_alter_purchase_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='receiver_type',
            new_name='purchase_type',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='purchase_no',
            new_name='reference_no',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
