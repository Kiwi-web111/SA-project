from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'category', 'quantity')
    search_fields = ('isbn', 'title', 'category')
    list_filter = ('category',)
