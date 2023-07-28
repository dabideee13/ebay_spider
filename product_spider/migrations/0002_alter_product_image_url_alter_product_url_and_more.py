# Generated by Django 4.2.3 on 2023-07-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_spider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterModelTable(
            name='product',
            table='product_data',
        ),
    ]