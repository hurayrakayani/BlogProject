from datetime import timezone
from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostForm
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'
class PostListview(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class= PostForm
    model= Post
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class= PostForm
    model= Post
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list') 
class PostDraftView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name  = 'blog/post_detail.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
#####################################
#####################################

def add_comment_to_post(request,pk):
    return 0
