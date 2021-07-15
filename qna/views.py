from django.shortcuts import render, get_object_or_404, redirect
from .models import Qna
from .forms import PostForm

# Create your views here.
def qna(request) :
    qnas = Qna.objects
    return render(request, 'qna.html',{'qnas':qnas})

def detail(request, qna_id):
    qna_detail = get_object_or_404(Qna, pk=qna_id)
    return render(request, 'detail.html',{'qna':qna_detail})

def create(request) :
    return render(request, 'create.html')

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('qna')
        
    else:
        form = PostForm()
        return render(request, 'create.html', {'form':form})

def edit(request):
    return render(request,'edit.html')

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