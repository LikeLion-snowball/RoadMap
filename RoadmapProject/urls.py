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
    2. Add a URL to urlpatterns:  path('human/', include('human.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import accounts.views
import info.views
import cal.views
import qna.views
import human.views
import home.views
import commentcrud.views
import crudapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name="home"),
    path('info/', include('info.urls')),
    path('<int:user_id>/', include('user.urls')),
    path('cal/', cal.views.calendar_view, name="calendar"),
    path('cal/', include('cal.urls')),
    path('qna/', qna.views.qna, name="qna"),
    path('qna/', include('qna.urls')),
    path('accounts/', include('accounts.urls')),
   # path('',human.views.humanhome, name='humanhome'),
    path('human/humanhome', human.views.humanhome, name="humanhome"),
    path('human/dnew/', human.views.dnew, name="dnew"),
    path('commentcrud/', include('commentcrud.urls')),
    path('human/dpage/<int:post_id>', human.views.dpage, name="dpage"),
    path('human/newcreate/', human.views.newcreate, name="newcreate"),
    path('human/hpostcreate/', human.views.hpostcreate, name="hpostcreate"),
    path('human/hpostdelete/<int:post_id>/', human.views.hpostdelete, name="hpostdelete"),
    path('human/hpostupdate/<int:post_id>/', human.views.hpostupdate, name="hpostupdate"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)