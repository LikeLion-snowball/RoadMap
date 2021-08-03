from django.http.response import HttpResponseRedirect
from commentcrud.forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Humanlog, Like
from .forms import PostForm
from accounts.models import CustomUser
from django.db.models import Q

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
        like = Like.objects.filter(user=request.user, post=post)
        return render(request, 'dpage.html', {'form': form, 'post': post, 'like': like})

def dpage_visitor(request, post_id):
    post = get_object_or_404(Humanlog, pk=post_id)
    return render(request, 'dpage.html', {'post': post})

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

def like(request, post_id):
    post = get_object_or_404(Humanlog, pk=post_id)
    liked = Like.objects.filter(user=request.user, post=post)
    if not liked:
        Like.objects.create(user=request.user, post=post)
        post.like_count += 1
        post.save()
    else:
        liked.delete()
        post.like_count -= 1
        post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def mylike(request, user_id):
    liked = Like.objects.filter(user=request.user)
    return render(request, 'like.html', {'likes': liked})

def h_result(request):
    h_result = Humanlog.objects.all()
    order = request.GET.get('order', '')
    query = request.GET.get('query', '')
    if order == "최신순":
        h_result = Humanlog.objects
    if order == "인기순":
        h_result = Humanlog.objects.order_by('-like_count')
    if query:
        h_result = h_result.filter(Q(body__icontains=query) | Q(title__icontains=query))

    return render(request,'humanhome.html', {'h_results' : h_result, 'order': order } )