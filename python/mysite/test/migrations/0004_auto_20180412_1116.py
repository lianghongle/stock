# Generated by Django 2.0.4 on 2018-04-12 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0003_auto_20180412_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='created_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
