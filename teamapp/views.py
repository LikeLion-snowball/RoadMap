from django.shortcuts import render, get_object_or_404, redirect
from .models import Team
from django.utils import timezone

# Create your views here.
def team_home(request):
    teams = Team.objects.order_by('pub_date')
    return render(request, 'team_home.html', {'teams' : teams})

def team_detail(request, team_id):
    team_detail = get_object_or_404(Team, pk = team_id)
    return render(request, 'team_detail.html', {'team' : team_detail})

def team_new(request):
    #return render(request, 'team_new.html')
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

    return render(request, 'team_new.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()} )
def team_create(request): #글쓰기
    return render(request, 'team_create.html')
   #postcreate 함수 추가
#team란 이름은 team()에 담기고
#team.title과 body는 GET 방식으로 오는 title과 body의 이름들의 값 ( create.html에서 )
#pub_date는 서버 시간 저장
#save
#해당 글로 바로 페이지 생성 url은 '/crudapp/detail/'에 해당 team.id로 이동

#detail페이지의 url 주소는 url을 묶어주어 http://127.0.0.1:8000/crudapp/detail/x/
# 그러므로 해당 주소로 바로 이동하기 위해 /crudapp/detail/ + str(team.id)
def team_postcreate(request): #글 등록
    team = Team()
    team.title = request.POST['title']
    team.body = request.POST['body']
    team.images = request.FILES['images']
    team.pub_date = timezone.datetime.now()
    team.save()
    return redirect('/teamapp/team_detail/' + str(team.id))

