from django.shortcuts import render
from .models import Post


def show_post(request):
    """Take all posts from db and show on show_post.html"""
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/show_post.html', context)


def one_post(request, post_id):
    """Take one post from db and show on one_post.html"""
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/one_post.html', context)

