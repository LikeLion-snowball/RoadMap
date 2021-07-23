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
import info.views
import cal.views
import qna.views
import human.views
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name="home"),
    path('info/', info.views.info, name="info"),
    path('<int:user_id>/', include('user.urls')),
    path('cal/', cal.views.calendar_view, name="calendar"),
    path('cal/', include('cal.urls')),
    path('qna/', qna.views.qna, name="qna"),
    path('qna/', include('qna.urls')),
    path('human/', human.views.human, name="human"),
    path('human/dnew/', human.views.dnew, name='dnew'),
    path('human/<int:human_id>', human.views.dpage, name='dpage'),
    path('human/dwrite', human.views.dwrite, name='dwrite'),
    path('human/dpostcreate', human.views.dpostcreate, name='dpostcreate'),
    path('accounts/', include('accounts.urls')),
    path('human/dpostupdate/<int:human_id>',human.views.dpostupdate, name='dpostupdate'),
    path('human/dupdate', human.views.dupdate, name='dupdate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)