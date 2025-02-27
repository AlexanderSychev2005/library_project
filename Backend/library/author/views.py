from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author
from .forms import AuthorForm


# Create your views here.
class AuthorListView(ListView):
    model = Author
    template_name = 'author/author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/author_detail.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/author_create.html'
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/author_update.html'
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(View):
    def post(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return redirect('author_list')
