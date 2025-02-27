from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_create.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_update.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(View):
    def post(self, request, pk):
        author = get_object_or_404(Book, pk=pk)
        author.delete()
        return redirect('book_list')
