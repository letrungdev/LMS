# Generated by Django 3.2.9 on 2021-11-12 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0013_auto_20211112_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 12, 18, 54, 30, 909287)),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='is_returned',
            field=models.CharField(default='No', max_length=100),
        ),
    ]
