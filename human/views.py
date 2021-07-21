from django.shortcuts import render, get_object_or_404
from .models import Human
# Create your views here.

def human(request):
    humans = Human.objects
    return render(request, 'human.html', {'humans': humans})

def dpage(request, human_id):
    human_dpage = get_object_or_404(Human, pk=human_id)
    return render(request, 'dpage.html', {'human': human_dpage})

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

    return render(request, 'new.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()} )

def dwrite(request):
    return render(request, 'dwrite.html')