# Generated by Django 3.2.9 on 2021-12-11 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0016_auto_20211211_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('book', models.CharField(max_length=100)),
                ('return_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='borrow',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 19, 36, 46, 979355)),
        ),
    ]
