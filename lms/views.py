from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, logout
from .models import Book, RequestBook, Borrow, History
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, UpdateView
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from . forms import UserForm, BookForm
from django.urls import reverse_lazy
from django.db.models import Count
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def base(request):
    return render(request, 'lms/base.html')
#Shared Views
@csrf_protect

def logoutView(request):
    logout(request)
    return redirect('base')

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('boss')
            else:
                return redirect('user')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('base')

def registerView(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        password = make_password(password)
        a = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        a.save()
        messages.success(request, 'Account was created successfully')
        return redirect('base')
    else:
        messages.error(request, 'Registration fail, try again later')
        return redirect('base')



#Admin Views
def boss(request):
    book = Book.objects.all().count()
    user = User.objects.all().count()
    requestb = RequestBook.objects.all().count()
    labels1 = []
    data1 = []
    labels2 = []
    data2 = []
    labels3 = []
    data3 = []
    topbooks = Borrow.objects.all().values('book').annotate(total=Count('book')).order_by('-total')[:3]
    btitles = Book.objects.order_by('-quantity')[:5]
    for bt in btitles:
        labels2.append(bt.title)
        data2.append(bt.quantity)

    categories = ["Science", "Romance", "Mystery", "Literature", "History", "Cookbook", "Business", "Biography", "Art"]
    for category in categories:
        count = Book.objects.filter(category=category).count()
        labels1.append(category)
        data1.append(count)

    for topbook in topbooks:
        labels3.append(topbook['book'])
        data3.append(topbook['total'])


    newbooks = Book.objects.order_by('-id')[:3]
    newusers = User.objects.order_by('-id')[:7]
    context = {'book': book, 'user': user, 'requestb':requestb, 'labels1':labels1, 'data1':data1, 'labels2':labels2, 'data2':data2, 'newbooks':newbooks, 'newusers':newusers, 'topbooks':topbooks, 'labels3':labels3,'data3':data3}
    return render(request, 'boss/home.html', context)

class BUserListView(generic.ListView):
    model = User
    template_name = 'boss/user_list.html'
    context_object_name = 'users'
    paginate_by = 5

    def get_queryset(self):
        return User.objects.order_by('id')

def bauser_form(request):
    return render(request, 'boss/add_user.html')

def bauser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = make_password(password)

        a = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        a.save()
        return redirect('bulist')
    else:
        return redirect('bauser_form')

class BMUserListView(generic.ListView):
    model = User
    template_name = 'boss/manage_user.html'
    context_object_name = 'users'
    paginate_by = 5

    def get_queryset(self):
        return User.objects.order_by('id')

def buesearch(request):
    if request.method == 'GET':
        searched = request.GET['searched']
        users = User.objects.filter(username__contains=searched)
        return render(request, 'boss/manage_user.html', {'users': users})

def beuser(request,pk):
    euser = get_object_or_404(User, pk=pk)
    return render(request, 'boss/edit_user.html', {'euser':euser})

def uduser(request,pk):
    upduser = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST, instance=upduser)
    if form.is_valid:
        form.save()
        messages.success(request, "Updated Successfully!")
        return redirect('bmuser')

def delete_user(request,pk):
    if request.method == 'POST':
        du = get_object_or_404(User, pk=pk)
        du.delete()
        return redirect('bmuser')
    return render(request, 'boss/manage_user.html')

class BBookListView(generic.ListView):
    model = Book
    template_name = 'boss/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.order_by('id')

@login_required
def babook_form(request):
    return render(request, 'boss/add_book.html')

def babook(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST['year']
        category = request.POST['category']
        quantity = request.POST['quantity']
        review = request.POST['review']
        cover = request.FILES['cover']

        a = Book(title=title, cover=cover, author=author, category=category, review=review, year=year, quantity=quantity)
        a.save()
        return redirect('bblist')
    else:
        return redirect('babook_form')

class BMBookListView(generic.ListView):
    model = Book
    template_name = 'boss/manage_book.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.order_by('id')

def bbesearch(request):
    if request.method == 'GET':
        searched = request.GET['searched']
        books = Book.objects.filter(title__contains=searched)
        return render(request, 'boss/manage_book.html', {'books': books})


def bstatus(request):
    books = Book.objects.all()
    for book in books:
        book.bring = Borrow.objects.filter(book=book.title).count()
        book.order = RequestBook.objects.filter(book=book.title).count()
        book.save()
    return render(request, 'boss/book_status.html', {'books':books})

def bssearch(request):
    if request.method == 'GET':
        title = request.GET['title']
        books = Book.objects.filter(title__contains=title)
        return render(request, 'boss/book_status.html', {'books':books})

def bebook(request,pk):
    ebook = get_object_or_404(Book, pk=pk)
    return render(request, 'boss/edit_book.html', {'ebook':ebook})

def udbook(request,pk):
    updbook = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST, instance=updbook)
    if form.is_valid:
        form.save()
        messages.success(request, "Updated Successfully!")
        return redirect('bmbook')

def delete_book(request, pk):
    if request.method == "POST":
        dbo = get_object_or_404(Book, pk=pk)
        dbo.delete()
        return redirect('bmbook')
    return render(request, 'boss/manage_book.html')

class BRequestListView(generic.ListView):
    model = RequestBook
    template_name = 'boss/manage_request.html'
    context_object_name = 'requests'
    paginate_by = 10

    def get_queryset(self):
        return RequestBook.objects.order_by('id')

def baborrow(request, pk):
    if request.method == "POST":
        b = get_object_or_404(RequestBook, pk=pk)
        a = Borrow(book=b.book, user=b.user)
        a.save()
        b.delete()
        return redirect('brlist')

def delete_request(request, pk):
    if request.method == "POST":
        dr = get_object_or_404(RequestBook, pk=pk)
        dr.delete()
        return redirect('brlist')


class BSListView(generic.ListView):
    model = Borrow
    template_name = 'boss/manage_borrow.html'
    context_object_name = 'borrows'
    paginate_by = 5

    def get_queryset(self):
        return Borrow.objects.order_by('id')

def bahistory(request, pk):
    if request.method == "POST":
        b = get_object_or_404(Borrow, pk=pk)
        a = History(book=b.book, user=b.user, start_date=b.start_date, end_date=b.end_date)
        a.save()
        b.delete()
        return redirect('bslist')

class BHListView(generic.ListView):
    model = History
    template_name = 'boss/history.html'
    context_object_name = 'histories'
    paginate_by = 5

    def get_queryset(self):
        return History.objects.order_by('id')


def delete_borrow(request,pk):
    if request.method == 'POST':
        db = get_object_or_404(Borrow, pk=pk)
        db.delete()
        return redirect('bslist')
    return render(request, 'boss/manage_borrow.html')

def bsearch(request):
    if request.method == 'GET':
        searched = request.GET['searched']
        books = Book.objects.filter(title__contains=searched)
        return render(request, 'user/result.html', {'searched':searched, 'books':books})

def bbsearch(request):
    if request.method == 'GET':
        searched = request.GET['searched']
        borrows = Borrow.objects.filter(Q(user__contains=searched) | Q(book__contains=searched))
        count = borrows.count()
        return render(request, 'boss/manage_borrow.html', {'borrows':borrows, 'searched':searched, 'count':count})

def brsearch(request):
    if request.method == 'GET':
        searched = request.GET['searched']
        requests = RequestBook.objects.filter(Q(user__contains=searched) | Q(book__contains=searched))
        count = requests.count()
        return render(request, 'boss/manage_request.html', {'requests':requests, 'searched':searched, 'count':count})

def bhsearch(request):
    if request.method == 'GET':
        searched = request.GET['searched']
        histories = History.objects.filter(Q(user__contains=searched) | Q(book__contains=searched))
        count = histories.count()
        return render(request, 'boss/history.html', {'histories':histories, 'searched':searched, 'count':count})

#User Views
@login_required
def user(request):
    return render(request, 'user/base.html')

def ustatus(request, username):
    borrows = Borrow.objects.filter(user=username)
    count = borrows.count()
    histories = History.objects.filter(user=username)
    return render(request, 'user/status.html', {'borrows':borrows, 'histories':histories, 'count':count})

def urequest(request, pk):
    book = get_object_or_404(Book, pk=pk)
    c = book.bring + book.order
    if c < book.quantity:
        return render(request, 'user/bookdetail.html', {'book':book})
    else:
        return render(request, 'user/bookdetail2.html', {'book':book})
@login_required
def urequestb(request, pk):
   if request.method == 'POST':
       rbook = get_object_or_404(Book, pk=pk).title
       ruser = request.user.username
       b = RequestBook.objects.values_list('user', flat=True)
       c = RequestBook.objects.values_list('book', flat=True)
       if ruser in b and rbook in c:
           return redirect('user')
       else:
           a = RequestBook(user=ruser, book=rbook)
           a.save()
           return redirect('user')


class UBookListView(LoginRequiredMixin,ListView):
    model = Book
    template_name = 'user/book_list.html'
    context_object_name = 'books'
    paginate_by = 9

    def get_queryset(self):
        return Book.objects.order_by('id')

@login_required
def uchoose(request):
    if request.method == 'GET':
        if request.GET['category']:
            category = request.GET['category']
            if request.GET['year']:
                year = request.GET['year']
                books = Book.objects.filter(category=category, year=year)
                count = books.count()
                return render(request, 'user/find.html', {'searched':category,'year':year, 'books':books, 'count':count})
            else:
                books = Book.objects.filter(category=category)
                count = books.count()
                return render(request, 'user/find.html',{'searched': category, 'books': books, 'count': count})

        if request.GET['year']:
            year = request.GET['year']
            if request.GET['category']:
                category = request.GET['category']
                books = Book.objects.filter(category=category, year=year)
                count = books.count()
                return render(request, 'user/find.html', {'searched':category,'year':year, 'books':books, 'count':count})
            else:
                books = Book.objects.filter(year=year)
                count = books.count()
                return render(request, 'user/find.html',{'searched':'all category', 'books': books, 'count': count})


def usearch(request):
    if request.method == 'GET':
        searched = request.GET['searched']
        books = Book.objects.filter(title__contains=searched)
        count = books.count()
        return render(request, 'user/result.html', {'searched':searched, 'books':books, 'count':count})

