# Generated by Django 2.0 on 2020-06-12 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('benefit1', models.CharField(max_length=50)),
                ('benefit2', models.CharField(max_length=50)),
                ('benefit3', models.CharField(max_length=50)),
                ('benefit4', models.CharField(max_length=50)),
                ('benefit5', models.CharField(max_length=50)),
                ('benefit6', models.CharField(max_length=50)),
                ('benefit7', models.CharField(max_length=50)),
                ('benefit8', models.CharField(max_length=50)),
                ('benefit9', models.CharField(max_length=50)),
                ('benefit10', models.CharField(max_length=50)),
                ('benefit11', models.CharField(max_length=50)),
            ],
        ),
    ]
