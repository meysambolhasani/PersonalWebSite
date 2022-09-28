from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.


def last_posts(request):
    last_post=Post.objects.all().order_by('-date')[:3]

    context={
        'last_post': last_post
    }
    return render(request, 'blog/last-posts.html',context)


def all_posts(request):
    posts=Post.objects.all()
 
    context={'posts':posts}
    return render(request, 'blog/all-posts.html', context)


def single_post(request, slug):
    post=Post.objects.get(slug=slug)
    tags = post.tags.all()
    comments = post.comments.all()
    comment_form = CommentForm()
    context={
        'post':post,
        'tags':tags,
        'comments': comments,
        'comment_form': comment_form,
    }
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
           comment= comment_form.save(commit=False)
           comment.post=post
           comment.save()

    return render(request, 'blog/single-post.html',context)
