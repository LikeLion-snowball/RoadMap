from django.shortcuts import redirect, render, get_object_or_404
from .models import  Project, Activity
from .forms import ActivityForm, ProjectForm

# Create your views here.
def myPage(request):
    return render(request, "myPage.html")
    
def portfolio(request):
    projects = Project.objects
    activities = Activity.objects
    return render(request, "portfolio.html", {'projects': projects, 'activities': activities})

def projectcreate(request):
    # 유저모델연결
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('portfolio')
    else:
        form = ProjectForm()
        return render(request, 'project_new.html', {'form':form})

def activitycreate(request):
    # 유저모델연결
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('portfolio')
    else:
        form = ActivityForm()
        return render(request, 'activity_new.html', {'form':form})
