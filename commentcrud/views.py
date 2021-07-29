from django.shortcuts import render,get_object_or_404, redirect
from .forms import CommentForm
from human.models import Humanlog
from django.contrib.auth.models import User

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