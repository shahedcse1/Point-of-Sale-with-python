# Generated by Django 4.0 on 2022-01-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellApp', '0020_alter_sellmodel_order_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellmodel',
            name='payment_status',
            field=models.CharField(choices=[('Payment', 'Payment'), ('Pending', 'Pending'), ('Dew', 'Dew')], max_length=50),
        ),
    ]
