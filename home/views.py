from info.models import Recruit
from django.shortcuts import render,get_object_or_404
from qna.models import Qna
from human.models import Humanlog

# Create your views here.
def home(request):
    Qnadts = Qna.objects.all()[:3]
    return render(request, 'home.html', {'Qnadts' : Qnadts})

def home2(request):
    Humandts = Humanlog.objects
    return render(request, 'home.html', {'Humandts' : Humandts})

def home3(request):
    Recruitdts = Recruit.objects.all()[:4]
    return render(request, 'home.html', {'Recruitdts' : Recruitdts})