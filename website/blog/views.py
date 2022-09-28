
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.


def last_posts(request):
    last_post = Post.objects.all().order_by('-date')[:3]

    context = {
        'last_post': last_post
    }
    return render(request, 'blog/last-posts.html', context)


def all_posts(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'blog/all-posts.html', context)


def single_post(request, slug):

    # post=Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    tags = post.tags.all()
    comments = post.comments.all()
    comment_form = CommentForm()
    context = {
        'post': post,
        'tags': tags,
        'comments': comments,
        'comment_form': comment_form,
    }
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

    return render(request, 'blog/single-post.html', context)


def create_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()

    else:
        post_form = PostForm()

    context = {
        'post_form': post_form
    }
    return render(request, 'blog/create-post.html', context)


def delete_post(request, slug):
    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect('all-post')
    return render(request, 'blog/delete-post.html')


def update_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_form = PostForm(instance=post)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('all-post')

    return render(request, 'blog/update-post.html',
                  {'post_form': post_form}
                  )
