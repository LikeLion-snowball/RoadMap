from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import CustomUser
import datetime
from .models import Event
import calendar
from .calendar import Calendar
from django.utils.safestring import mark_safe
from .forms import EventForm

def calendar_view(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar(today.year, today.month)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'cal.html', context)

def calForAll(request):
    # 로그인 안 한 사람이 보는 view
    return render(request, 'cal.html')

#현재 달력을 보고 있는 시점의 시간을 반환
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()

#현재 달력의 이전 달 URL 반환
def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

#현재 달력의 다음 달 URL 반환
def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

#이벤트 생성
def eventcreate(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    instance = Event()
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('calendar', user_id=user.pk)
    return render(request, 'eventcreate.html', {'form': form})

#이벤트 수정
def eventedit(request, user_id, event_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    instance = get_object_or_404(Event, pk=event_id)
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('calendar', user_id=user.pk)
    return render(request, 'eventedit.html', {'form': form})

#이벤트 삭제
#def eventdelete(request, event_id) :
#    instance = get_object_or_404(Event, pk=event_id)
#    instance.delete()
#    return redirect('calendar')
