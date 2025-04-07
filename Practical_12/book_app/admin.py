from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'isbn', 'genre')
    list_filter = ('genre', 'publication_date')
    search_fields = ('title', 'author', 'isbn')
    date_hierarchy = 'publication_date'
