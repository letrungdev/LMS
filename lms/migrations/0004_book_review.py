# Generated by Django 3.2.9 on 2021-11-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_alter_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
