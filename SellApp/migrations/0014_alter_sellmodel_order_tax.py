# Generated by Django 4.0 on 2022-01-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellApp', '0013_alter_sellmodel_order_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellmodel',
            name='order_tax',
            field=models.CharField(choices=[('GST @5%', 'GST @5%'), ('No tax', 'No tax'), ('VAT @10%', 'VAT @10%')], max_length=50),
        ),
    ]
