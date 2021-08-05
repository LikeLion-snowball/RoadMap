from django.http.response import HttpResponseRedirect
from accounts.models import CustomUser
from django.shortcuts import render, get_object_or_404, redirect
from .models import Qna, Q_Comment, Q_Like
from .forms import PostForm, CommentForm
from django.db.models import Q

# Create your views here.
def qna(request) :
    qnas = Qna.objects
    return render(request, 'qna.html', {'qnas':qnas})

def detail(request, qna_id, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    qna_detail = get_object_or_404(Qna, pk=qna_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.qna = qna_detail
            comment.save()
            return redirect('detail', qna_id=qna_detail.pk, user_id=user.pk)
    else:
        form = CommentForm()
        like = Q_Like.objects.filter(user=request.user, qna=qna_detail)
        return render(request, 'detail.html', {'form': form, 'qna': qna_detail, 'like': like})
    
def detail_visitor(request, qna_id):
    qna = get_object_or_404(Qna, pk=qna_id)
    return render(request, 'detail.html', {'qna': qna})

def create(request) :
    return render(request, 'create.html')

def postcreate(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.save()
            return redirect('qna')
    else:
        form = PostForm()
        return render(request, 'create.html', {'form':form})

def postupdate(request, qna_id):
    post = get_object_or_404(Qna, pk=qna_id)
    if request.method =='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('detail', qna_id=post.pk)
    else :
        form=PostForm(instance=post)
        return render(request,'edit.html',{'form':form})

def postdelete(request, qna_id) :
    post = get_object_or_404(Qna, pk=qna_id)
    post.delete()
    return redirect('qna')

def qcommentupdate(request, qna_id, comment_id, user_id):
    comment = get_object_or_404(Q_Comment, pk=comment_id)
    qna = get_object_or_404(Qna, pk=qna_id)
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method=='POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', qna_id=comment.qna.pk, user_id=user.pk)
    else:
        form = CommentForm(instance=comment)
        return render(request, 'detail.html', {'form_comment': form, 'qna': comment.qna, 'commentId': comment_id})

def qcommentdelete(request, qna_id, comment_id, user_id):
    comment = get_object_or_404(Q_Comment, pk=comment_id)
    qna = get_object_or_404(Qna, pk=qna_id)
    user = get_object_or_404(CustomUser, pk=user_id)
    comment.delete()
    return redirect('detail', qna_id=qna.pk, user_id=user.pk)

def q_result(request):
    q_result = Qna.objects.all()
    order = request.GET.get('order', '')
    query = request.GET.get('query', '')
    if order == "최신순":
        q_result = Qna.objects
    if order == "인기순":
        q_result = Qna.objects.order_by('-like_count')
    if query:
        q_result = q_result.filter(Q(body__icontains=query) | Q(title__icontains=query))

    return render(request, 'qna.html', {'q_results' : q_result, 'order': order } )

def like(request, qna_id):
    qna = get_object_or_404(Qna, pk=qna_id)
    liked = Q_Like.objects.filter(user=request.user, qna=qna)
    if not liked:
        Q_Like.objects.create(user=request.user, qna=qna)
        qna.like_count += 1
        qna.save()
    else:
        liked.delete()
        qna.like_count -= 1
        qna.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
