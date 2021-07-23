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
import accounts.views
import info.views
import user.views
import cal.views
import qna.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
#     path('',accounts.views.home,name="home"),
    path('info/', info.views.info, name="info"),
    path('user/', user.views.myPage, name="myPage"),
    path('user/portfolio', user.views.portfolio, name="portfolio"),
    path('cal/', cal.views.calendar_view, name="calendar"),
     path('cal/', include('cal.urls')),
    path('qna/', qna.views.qna, name="qna"),
    path('qna/', include('qna.urls')),
]
