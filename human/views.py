from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Humanlog
from .forms import PostForm
from django.contrib.auth.models import User

# Create your views here.

def humanhome(request):
    humanlogs = Humanlog.objects
    return render(request, 'humanhome.html', {'humanlogs': humanlogs})

def dpage(request, humanlog_id):
    humanlog_dpage = get_object_or_404(Humanlog, pk=humanlog_id)
    return render(request, 'dpage.html', {'humanlog': humanlog_dpage})

def dnew(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    return render(request, 'dnew.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()} )