# Generated by Django 2.1.5 on 2020-07-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200705_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='flowers',
        ),
        migrations.AddField(
            model_name='flower',
            name='customers',
            field=models.ManyToManyField(to='users.Customer'),
        ),
    ]
