# Generated by Django 3.2.9 on 2022-01-03 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0018_auto_20211212_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Available',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=100)),
                ('ava', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 8, 0, 57, 313297)),
        ),
    ]