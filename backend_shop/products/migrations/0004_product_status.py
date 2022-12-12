# Generated by Django 4.1.4 on 2022-12-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_image_url_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('1', 'В наличии'), ('2', 'Под заказ'), ('3', 'Ожидается поступление'), ('4', 'Нет в наличии'), ('5', 'Не производится')], default='1', max_length=1, verbose_name='status'),
        ),
    ]
