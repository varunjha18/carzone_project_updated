# Generated by Django 3.1.1 on 2021-05-25 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('car_id', models.IntegerField()),
                ('customer_needs', models.CharField(max_length=200)),
                ('car_title', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True, max_length=200)),
                ('user_id', models.IntegerField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2021, 5, 25, 12, 51, 50, 986219))),
            ],
        ),
    ]
