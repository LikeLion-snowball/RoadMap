"""RoadmapProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import info.views
import cal.views
import qna.views
import teamapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
#     path('',accounts.views.home,name="home"),
    path('info/', info.views.info, name="info"),
    path('<int:user_id>/', include('user.urls')),
    path('', cal.views.cal, name="cal"),
    path('qna/', qna.views.qna, name="qna"),
    path('qna/<int:qna_id>', qna.views.detail, name="detail"),
    path('qna/create',qna.views.create, name="create"),
    path('qna/postcreate', qna.views.postcreate, name='postcreate'),
    path('qna/edit', qna.views.edit, name='edit'),
    path('qna/postupdate/<int:qna_id>', qna.views.postupdate, name='postupdate'),
    path('qna/postdelete/<int:qna_id>',qna.views.postdelete, name='postdelete'),
    path('', teamapp.views.team_home, name="team_home"),
    path('team_new/', teamapp.views.team_new, name='team_new'),
    path('team_detail/<int:team_id>', teamapp.views.team_detail, name="team_detail"),
    path('team_create', teamapp.views.team_create, name="team_create"),
    path('team_postcreate/', teamapp.views.team_postcreate, name='team_postcreate'),
    path('teamapp/', include('teamapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
