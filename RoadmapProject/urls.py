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
##from . import views

import teamapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', teamapp.views.home, name="home"),
    #path('new/', teamapp.views.new, name='new'),
    #path('detail/<int:team_id>', teamapp.views.detail, name="detail"),
    #path('create', teamapp.views.create, name="create"),
    #path('postcreate/', teamapp.views.postcreate, name='postcreate'),
    path('teamapp/', include('teamapp.urls')),
    ##path('delete/<int:team_id>/', views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

