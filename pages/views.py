from django.shortcuts import render
from django.views.generic import ListView, DetailView #ListView returns an object object_list
from .models import Post, Blog

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_list'

class  BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'