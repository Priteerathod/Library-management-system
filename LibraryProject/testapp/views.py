from django.shortcuts import render
from testapp.models import Book
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.
class Booklist(ListView):
    model=Book
class Bookdetails(DetailView):
    model=Book

class createbookview(CreateView):
    model=Book
    fields=['name','author','price','p_date']
class updatebookview(UpdateView):
    model=Book
    fields=['name','author','price','p_date']
class Deletebookview(DeleteView):
    model=Book
    success_url=reverse_lazy('list')
