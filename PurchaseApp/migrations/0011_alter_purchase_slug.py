# Generated by Django 4.0 on 2022-01-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseApp', '0010_alter_purchase_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
