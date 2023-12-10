# Generated by Django 4.0 on 2022-01-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchaseApp', '0008_purchase_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='purchase',
            unique_together={('reference_no', 'slug')},
        ),
    ]