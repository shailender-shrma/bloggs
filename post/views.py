from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Post
from django.views.generic.base import View
from django.views.generic.edit import CreateView 
from django.views.generic import ListView , DeleteView , DetailView, UpdateView
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.


class CreatePostView(CreateView):
    template_name = 'templates/login.html'
    model = Post


    fields = ['title', 'content']
    success_url = '/'

class PostShowView(ListView):
    template_name = 'templates/index.html'
    model = Post
    context_object_name ='post'
    success_url = 'home'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.filter(title__contains='hello')
        
                                  

class PostDeleteView(DeleteView):
    template_name = 'templates/delete.html' 
    model = Post
    success_url='/'

class PostDetailView(DetailView):
    template_name = 'templates/detail.html'
    model = Post
    context_object_name = 'post'
    success_Url = '/'


class PostUpdateView(UpdateView):
    template_name = 'templates/update.html'
    model = Post
    context_object_name = 'post'
    fields=['content']
    success_url = '/'




