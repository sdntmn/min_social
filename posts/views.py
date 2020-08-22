from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, request

from .models import Post, Group
from .forms import PostForm

def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    
    return render(request, "group.html", {"group": group, "posts": posts})

def new_post(reguest):
    if request.method == "POST":
        form = PostForm(reguest.POST)
        if form.is_valid():
            post_get = form.save(commit=False)
            post_get.author = request.user
            post_get.save()
            return redirect("index")
        else:
            return render(request, 'new.html')
    return render(request, "new.html", {"form": form})
