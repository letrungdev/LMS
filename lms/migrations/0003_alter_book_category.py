# Generated by Django 3.2.7 on 2021-11-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
