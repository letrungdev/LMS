from django.contrib import admin
from .models import Book, RequestBook
# Register your models here.

admin.site.register(Book)
admin.site.register(RequestBook)