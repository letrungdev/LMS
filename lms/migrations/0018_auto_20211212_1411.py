# Generated by Django 3.2.9 on 2021-12-12 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0017_auto_20211211_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 14, 11, 20, 11910)),
        ),
    ]
