# Generated by Django 3.2.9 on 2022-01-06 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0021_auto_20220106_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='available',
            name='total',
        ),
        migrations.AlterField(
            model_name='borrow',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 7, 14, 40, 48, 642218)),
        ),
    ]
