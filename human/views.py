from django.shortcuts import render, get_object_or_404, redirect
from .models import Humanlog
from .forms import PostForm
from django.contrib.auth.models import User

# Create your views here.

def humanhome(request):
    posts = Humanlog.objects
    return render(request, 'humanhome.html', {'posts':posts})

def dnew(request):
    return render(request, 'dnew.html')

def dpage(request, post_id):
    post_dpage = get_object_or_404(Humanlog, pk=post_id)
    return render(request, 'dpage.html', {'post': post_dpage})

def newcreate(request):
    return render(request, 'newcreate.html')

def hpostcreate(request):
    post = Humanlog()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.save()
    return redirect('/human/dpage/' + str(post.id))

def hpostdelete(request, post_id):
    post = Humanlog.objects.get(id=post_id)
    post.delete()
    return redirect('/human/humanhome')

def hpostupdate(request, post_id):
    post = Humanlog.objects.get(id=post_id)

    if request.method == "POST":
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
        return redirect('/human/dpage/' + str(post.id))

    else:
        return render(request, 'hpostupdate.html')