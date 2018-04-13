# Generated by Django 2.0.4 on 2018-04-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0008_auto_20180412_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='testname', max_length=30, unique=True)),
                ('description', models.CharField(blank=True, max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]