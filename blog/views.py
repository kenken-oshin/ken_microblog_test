from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.
from .models import Blog

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog