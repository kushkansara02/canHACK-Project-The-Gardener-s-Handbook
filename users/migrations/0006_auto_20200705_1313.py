# Generated by Django 2.1.5 on 2020-07-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200705_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='flowers',
            field=models.ManyToManyField(to='users.Flower'),
        ),
    ]
