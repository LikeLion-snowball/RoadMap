from django.shortcuts import render
from .models import Portfolio, Project, Activity

# Create your views here.
def myPage(request):
    return render(request, "myPage.html")
    
def portfolio(request):
    portfolio = Portfolio.objects
    projects = Project.objects
    activities = Activity.objects
    return render(request, "portfolio.html", {'portfolio': portfolio, 'projects': projects, 'activities': activities})