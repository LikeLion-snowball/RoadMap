from django.shortcuts import render, get_object_or_404, redirect
from .models import Human
from .forms import PostForm
from django.utils import timezone
from .forms import CommentForm

# Create your views here.

def human(request):
    humans = Human.objects
    return render(request, 'human.html', {'humans': humans})

def dpage(request, human_id):
    human_dpage = get_object_or_404(Human, pk=human_id)
    return render(request, 'dpage.html', {'human': human_dpage})


def dwrite(request):
    return render(request, 'dwrite.html')

def dpostcreate(request):
    human = Human()
    human.title = request.GET['title']
    human.body = request.GET['body']
    human.pub_date = timezone.datetime.now()
    human.save()
    return redirect('human')


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

def dupdate(request):
    return render(request, 'dupdate.html')


def dpostupdate(request, human_id):
    post = get_object_or_404(Human, pk=human_id)
    if request.method =='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('dpage', human_id=post.pk)
    else :
        form=PostForm(instance=post)
        return render(request,'dupdate.html',{'form':form})

def add_comment_to_post(request, human_id):
    human=get_object_or_404(Human, pk=human_id)
    if request.method == "POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=human
            comment.save()
            return redirect('dpage', human_id=human.pk)
        else:
            redirect('human')

    else:
        form=CommentForm()
        return render(request, 'add_comment_to_post.html', {'form':form})