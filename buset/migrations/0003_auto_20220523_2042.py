# Generated by Django 3.2.8 on 2022-05-23 13:42

import buset.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buset', '0002_auto_20220523_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=30)),
                ('shop_pp', models.ImageField(upload_to='static')),
                ('shop_created', models.DateTimeField(auto_now_add=True)),
                ('shop_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_password', models.CharField(default=buset.models._create_hash, max_length=16, unique=True)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_pp', models.ImageField(upload_to='static')),
                ('user_role', models.CharField(max_length=6)),
                ('user_created', models.DateTimeField(auto_now_add=True)),
                ('user_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='posting',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
