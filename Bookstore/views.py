from django.shortcuts import render

from .forms import BookForm
from .models import Book


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
