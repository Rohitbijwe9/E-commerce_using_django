# Generated by Django 4.2.4 on 2023-08-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]