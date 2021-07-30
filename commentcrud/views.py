from django.shortcuts import render,get_object_or_404, redirect
from .forms import CommentForm
from human.models import Humanlog
from django.contrib.auth.models import User
from .models import Comment

# Create your views here.
def commentcreate(request, user_id, post_id):
    user = get_object_or_404(User, pk=user_id)
    post = get_object_or_404(Humanlog, pk=post_id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.post = post
            comment.save()
            return redirect('dpage', post_id=post.pk)
        else:
            redirect('list')
    else:
        form = CommentForm()
        return render(request, 'dpage.html', {'form': form, 'post': post})

def commentupdate(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Humanlog, pk=post_id)
    if request.method=='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('dpage', post_id=comment.post.pk)

    else:
        form = CommentForm(instance=comment)
        return render(request, 'dpage.html', {'form_comment': form, 'post': comment.post})

def commentdelete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Humanlog, pk=post_id)
    comment.delete()
    return redirect('dpage', post_id=post.pk)     