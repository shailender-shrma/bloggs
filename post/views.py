from django.shortcuts import render, redirect
from .models import Post
from django.views.generic.base import View
from django.views.generic.edit import CreateView 
from django.views.generic import ListView

from django.http import HttpResponse

# Create your views here.


class PostView(CreateView):
    template_name = 'templates/login.html'
    model = Post


    fields = ['title', 'content']
    success_url = 'home'

class ShowView(ListView):
    template_name = 'templates/index.html'
    model = Post
    context_object_name ='post'

# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = ".html"


