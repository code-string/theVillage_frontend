# Generated by Django 3.0 on 2020-07-06 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0015_booking_isexpired'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
