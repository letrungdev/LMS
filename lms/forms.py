from django.contrib.auth.models import User
from . models import Book
from django import forms



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'review', 'category', 'year', 'quantity')