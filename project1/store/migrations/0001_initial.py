# Generated by Django 4.2.4 on 2023-08-28 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catogory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='products/')),
                ('catagory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.catogory')),
            ],
        ),
    ]
