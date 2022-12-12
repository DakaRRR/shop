# Generated by Django 4.1.4 on 2022-12-12 07:09

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('sku', models.CharField(max_length=255, unique=True, verbose_name='sku')),
                ('price', models.IntegerField(verbose_name='price')),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=products.models.upload_to, verbose_name='image')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['title'],
            },
        ),
    ]
