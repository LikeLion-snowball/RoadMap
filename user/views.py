from django.shortcuts import redirect, render, get_object_or_404
from .models import  Project, Activity
from .forms import ActivityForm, ProjectForm

# Create your views here.
def myPage(request):
    return render(request, "myPage.html")
    
def portfolio(request):
    projects = Project.objects.all().order_by('project_start') # 시작날짜 순으로 정렬
    activities = Activity.objects.all().order_by('activity_start') # 시작날짜 순으로 정렬
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

def projectupdate(request, project_id):
    # 유저모델연결
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('portfolio')
    else:
        form = ProjectForm(instance=project)
        return render(request, 'project_edit.html', {'form': form, 'project': project})

def projectdelete(request, project_id):
    # 유저모델연결
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect('portfolio')

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

def activityupdate(request, activity_id):
    # 유저모델연결
    activity = get_object_or_404(Activity, pk=activity_id)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.save()
            return redirect('portfolio')
    else:
        form = ActivityForm(instance=activity)
        return render(request, 'activity_edit.html', {'form': form, 'activity': activity})

def activitydelete(request, activity_id):
    # 유저모델연결
    activity = get_object_or_404(Activity, pk=activity_id)
    activity.delete()
    return redirect('portfolio')
