from django.shortcuts import render
from .models import Post


def show_post(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/show_post.html', context)

def one_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/one_post.html', context)