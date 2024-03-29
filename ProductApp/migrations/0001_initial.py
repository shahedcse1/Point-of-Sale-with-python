# Generated by Django 4.0 on 2021-12-28 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_image', models.ImageField(blank=True, upload_to='products/', verbose_name='Category Image')),
                ('cate_name', models.CharField(max_length=100, verbose_name='Category name')),
                ('cate_shot_des', models.CharField(blank=True, max_length=200, verbose_name='Category short description')),
                ('cate_des', models.TextField(blank=True, verbose_name='Category description')),
                ('slug', models.SlugField(unique=True)),
                ('code', models.CharField(max_length=50, verbose_name='Category code')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_related', to='ProductApp.category', verbose_name='Parent Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('standart', 'standard'), ('conbo', 'combo'), ('digital', 'digital')], default='standard', max_length=50)),
                ('name', models.CharField(max_length=60)),
                ('code', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('tax_mathod', models.CharField(choices=[('Edclusive', 'Edclusive'), ('Inclusive', 'Inclusive')], default='Exclusive', max_length=50)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('product_image', models.ImageField(blank=True, upload_to='products/', verbose_name='Product Image')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductApp.category')),
            ],
        ),
    ]
