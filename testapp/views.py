from django.shortcuts import render
from .models import Book
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

class list_view(ListView):
    model = Book
    template_name = 'testapp/books.html' # default template file book_list.html
    context_object_name = 'books' # default book_list {% for book in book_list%}, now:{% for book in books%}

class BookDetailView(DetailView): #it talks about only one book 
    model = Book
    # default template file : book_detial.html 
    # default context object : object or book

class BookCreateView(CreateView):
    model = Book
    fields = ('title','author','pages','price')

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'

from django.urls import reverse_lazy
class BookDeleteView(DeleteView):
    model = Book 
    success_url = reverse_lazy('list') # path('list/',views.list_view.as_view(),name= 'list'),here name is called reverse url we dont use url