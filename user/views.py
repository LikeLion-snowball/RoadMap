from typing import ClassVar
from django.http.response import HttpResponseRedirect
from accounts.models import CustomUser #Humanlog
from django.shortcuts import redirect, render, get_object_or_404
from .models import  Project, Activity
from .forms import ActivityForm, ProjectForm

# Create your views here.
def myPage(request, user_id):
    return render(request, "myPage.html")
    
def portfolio(request, user_id):
    projects = Project.objects.filter(user=request.user)
    projects.order_by('project_start') # 시작날짜 순으로 정렬
    activities = Activity.objects.all().filter(user=request.user)
    activities.order_by('activity_start') # 시작날짜 순으로 정렬
    return render(request, "portfolio.html", {'projects': projects, 'activities': activities, 'username': request.user.username})

def others_portfolio(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    projects = Project.objects.filter(user=user_id)
    projects.order_by('project_start')
    activities = Activity.objects.all().filter(user=user_id)
    activities.order_by('activity_start') # 시작날짜 순으로 정렬
    return render(request, "portfolio.html", {'projects': projects, 'activities': activities, 'username': user.username, 'others': user})

def port_open(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        if user.portfolio_isPrivate == False:
            user.portfolio_isPrivate = True
            user.save()
        else :
            user.portfolio_isPrivate = False
            user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def projectcreate(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = user
            project.save()
            return redirect('portfolio', user_id=user.pk)
    else:
        form = ProjectForm()
        return render(request, 'project_new.html', {'form':form})

def projectupdate(request, user_id, project_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('portfolio', user_id=user.pk)
    else:
        form = ProjectForm(instance=project)
        return render(request, 'project_edit.html', {'form': form, 'project': project})

def projectdelete(request, user_id, project_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return redirect('portfolio', user_id=user.pk)

def activitycreate(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = user
            project.save()
            return redirect('portfolio', user_id=user.pk)
    else:
        form = ActivityForm()
        return render(request, 'activity_new.html', {'form':form})

def activityupdate(request, user_id, activity_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    activity = get_object_or_404(Activity, pk=activity_id)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.save()
            return redirect('portfolio', user_id=user.pk)
    else:
        form = ActivityForm(instance=activity)
        return render(request, 'activity_edit.html', {'form': form, 'activity': activity})

def activitydelete(request, user_id, activity_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    activity = get_object_or_404(Activity, pk=activity_id)
    activity.delete()
    return redirect('portfolio', user_id=user.pk)

#def dpage_visitor(request, post_id):
    #post = get_object_or_404(Humanlog, pk=post_id)
    #return render(request, 'dpage.html', {'post': post})
