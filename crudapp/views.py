from django.shortcuts import render
from .models import Blog
# Create your views here.
def bhome(request):
    posts = Blog.objects
    return render(request, 'bhome.html', {'posts': posts})