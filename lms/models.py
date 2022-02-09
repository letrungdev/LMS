from datetime import datetime, timedelta
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100)
    review = models.TextField(null=True)
    year = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True)
    bring = models.IntegerField(null=True)
    order = models.IntegerField(null=True)
    cover = models.ImageField(upload_to='Media/BookCover', null=True, blank=True)


class RequestBook(models.Model):
    user = models.CharField(max_length=100)
    book = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add = True)


class Borrow(models.Model):
    user = models.CharField(max_length=100)
    book = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add = True, null=True)
    end_date = models.DateTimeField(default=datetime.now()+timedelta(days=60))
    is_returned = models.CharField(max_length=100, default='No')

class History(models.Model):
    user = models.CharField(max_length=100)
    book = models.CharField(max_length=100)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    return_date = models.DateTimeField(auto_now_add = True)

