# Generated by Django 4.2.5 on 2023-09-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_order_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
