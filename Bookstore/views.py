from django.shortcuts import render

from .forms import BookForm
from .models import Book


def home_view(request):
    return render(request, 'bookstore/home.html', {
        'user_name': request.user.get_username() or '使用者',
    })


def book_list_view(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookstore/book_list.html', {
        'books': books,
    })


def book_create_view(request):
    form = BookForm(request.POST or None)
    success = False
    if request.method == 'POST' and form.is_valid():
        form.save()
        success = True
        form = BookForm()

    return render(request, 'bookstore/book_form.html', {
        'form': form,
        'success': success,
    })
