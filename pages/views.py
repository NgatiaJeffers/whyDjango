from django.shortcuts import render
from django.views.generic import TemplateView, ListView #ListView returns an object object_list
from .models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_list'

class AboutPageView(TemplateView):
    template_name = 'about.html'