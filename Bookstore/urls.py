from django.urls import path

from .views import book_create_view, book_list_view

urlpatterns = [
    path('', book_list_view, name='book-list'),
    path('new/', book_create_view, name='book-create'),
]
