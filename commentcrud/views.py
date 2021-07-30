from django.shortcuts import render,get_object_or_404, redirect
from .forms import CommentForm
from human.models import Humanlog
from .models import Comment
from accounts.models import CustomUser

def commentupdate(request, post_id, comment_id, user_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Humanlog, pk=post_id)
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method=='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('dpage', post_id=comment.post.pk, user_id=user.pk)
    else:
        form = CommentForm(instance=comment)
        return render(request, 'dpage.html', {'form_comment': form, 'post': comment.post, 'commentId': comment_id})

def commentdelete(request, post_id, comment_id, user_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Humanlog, pk=post_id)
    user = get_object_or_404(CustomUser, pk=user_id)
    comment.delete()
    return redirect('dpage', post_id=post.pk, user_id=user.pk)     