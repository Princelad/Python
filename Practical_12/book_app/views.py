from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm

# List all books
class BookListView(ListView):
    model = Book
    template_name = 'book_app/book_list.html'
    context_object_name = 'books'

# Show book details
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_app/book_detail.html'
    context_object_name = 'book'

# Create a new book
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_app/book_form.html'
    success_url = reverse_lazy('book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

# Update an existing book
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_app/book_form.html'
    success_url = reverse_lazy('book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update'
        return context

# Delete a book
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_app/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
