# Generated by Django 3.2.9 on 2021-11-12 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0010_borrow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
