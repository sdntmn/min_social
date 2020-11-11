from django.contrib.auth.decorators import login_required
from django.db.models import fields
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post


def index(request):
    latest = Post.objects.all()[:11] 
    return render(request, 'index.html', {'posts': latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.all()[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})


@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
        return render(request, 'new.html', {'form': form})
    form = PostForm(request.POST)
    if not form.is_valid():
        return render(request, 'new.html', {'form': form})
    new_form = form.save(commit=False)
    new_form.author = request.user
    new_form.save()
    return redirect('index')

""" Так получается то же не правильно
author = Post(author=request.user) 
form = PostForm(request.POST, instance=author) 
new_form = form.save() 
"""