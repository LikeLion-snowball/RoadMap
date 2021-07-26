from django.shortcuts import render
from .models import Recruit
from datetime import date

# Create your views here.
def info(request):
    recruits = Recruit.objects
    Recruit.objects.filter(end_date__lt=date.today()).delete()
    return render(request, "info.html", {'recruits': recruits, 'today': date.today()})