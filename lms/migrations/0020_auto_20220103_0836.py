# Generated by Django 3.2.9 on 2022-01-03 01:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0019_auto_20220103_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 8, 36, 16, 633389)),
        ),
    ]