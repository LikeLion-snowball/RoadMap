from commentcrud.forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Humanlog
from .forms import PostForm
from accounts.models import CustomUser

# Create your views here.

def humanhome(request):
    posts = Humanlog.objects
    return render(request, 'humanhome.html', {'posts':posts})

def notice(request):
    return render(request, 'notice.html')

def dpage(request, post_id, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    post = get_object_or_404(Humanlog, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.post = post
            comment.save()
            return redirect('dpage', post_id=post.pk, user_id=user.pk)
    else:
        form = CommentForm()
        return render(request, 'dpage.html', {'form': form, 'post': post})

def hpostcreate(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.save()
            return redirect('humanhome')
    else:
        form = PostForm()
        return render(request, 'newpost.html', {'form': form})

def hpostupdate(request, post_id):
    post = get_object_or_404(Humanlog, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('dpage', post_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'updatepost.html', {'form': form})

def hpostdelete(request, post_id):
    post = get_object_or_404(Humanlog, pk=post_id)
    post.delete()
    return redirect('humanhome')