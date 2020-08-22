from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, request

from .models import Post, Group
from django.forms import ModelForm

def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:12]
    
    return render(request, "group.html", {"group": group, "posts": posts})

def new_post(reguest):
    if request.method == "POST":
        form = ModelForm(reguest.POST)
        if form.is_valid():
            form.save()
            return redirect("")
        return render(request, "new_post.html", {"form": form})
    form = ModelForm(reguest.POST)   
    return render(request, "new_post.html", {"form": form})
