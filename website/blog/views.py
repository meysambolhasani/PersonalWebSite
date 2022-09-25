from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from .forms import PostForm,CommentForm

# Create your views here.

def last_posts(request):
    return render(request, 'blog/last-posts.html')

def all_posts(request):
    return render(request, 'blog/all-posts.html')

def single_post(request,slug):
  return render(request, 'blog/single-post.html')
