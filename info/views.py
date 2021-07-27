from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Recruit, Scrap
from datetime import date
from django.db.models import Q

# Create your views here.
def info(request):
    recruits = Recruit.objects
    Recruit.objects.filter(end_date__lt=date.today()).delete()
    return render(request, "info.html", {'recruits': recruits, 'today': date.today()})

def result(request):
    result = Recruit.objects
    query = request.GET.get('query', '')
    type = request.GET.get('type', '')
    area = request.GET.get('area', '')
    order = request.GET.get('order', '')
    if order == "날짜순":
        result = result.order_by('end_date')
    if order == "인기순":
        result = Recruit.objects
    if query:
        result = result.filter(Q(title__icontains=query) | Q(corp__icontains=query) 
                                | Q(career__icontains=query) | Q(academic__icontains=query))
    if type:
        result = result.filter(type__icontains=type)
    if area:
        result = result.filter(area__icontains=area)
    return render(request, 'info.html', {'results': result, 'result_count':result.count(), 'area': area, 'type': type, 'order': order, 'today': date.today()})

def scrap(request, recruit_id):
    recruit = get_object_or_404(Recruit, pk=recruit_id)
    scrapped = Scrap.objects.filter(user=request.user, recruit=recruit)
    if not scrapped:
        Scrap.objects.create(user=request.user, recruit=recruit)
        recruit.scrap_count += 1
        recruit.save()
    else:
        scrapped.delete()
        recruit.scrap_count -= 1
        recruit.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def my_scrap(request, user_id):
    scrapped = Scrap.objects.filter(user=request.user)
    return render(request, 'myScrap.html', {'scraps': scrapped, 'today': date.today()})