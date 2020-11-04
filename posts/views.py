from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post


def index(request):
    latest = Post.objects.all()[:11] 
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    return render(request, "group.html", {"group": group, "posts": posts})


@login_required
def new_post(request):
    if not request.method == 'POST':
        form = PostForm()
        return render(request, 'new.html', {'form': form})
    form = PostForm(request.POST)
    if not form.is_valid():
        return render(request, 'new.html', {'form': form})
    author = Post(author=request.user)
    new_form = PostForm(request.POST, instance=author)
    new_form.save()
    return redirect('index')