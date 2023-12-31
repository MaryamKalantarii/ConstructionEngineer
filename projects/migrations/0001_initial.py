# Generated by Django 4.2.5 on 2023-09-27 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('schedule', models.DateTimeField(default=datetime.datetime(2023, 9, 27, 17, 9, 51, 794136))),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='projects.category')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]
