from info.models import Recruit
from django.shortcuts import render,get_object_or_404
from qna.models import Qna
from human.models import Humanlog

# Create your views here.
def home(request):
    Qnadts = Qna.objects.all()[:3]
    Humandts = Humanlog.objects.all()[:3]
    Recruitdts = Recruit.objects.all()[:4]
    return render(request, 'home.html', {'Qnadts' : Qnadts, 'Humandts' : Humandts, 'Recruitdts' : Recruitdts})
