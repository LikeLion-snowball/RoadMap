#from django.contrib import admin
from django.urls import path

import teamapp.views

urlpatterns = [
    path('new/', teamapp.views.new, name='new'),
    path('detail/<int:team_id>', teamapp.views.detail, name="detail"),
    path('create/', teamapp.views.create, name="create"),
    path('postcreate/', teamapp.views.postcreate, name='postcreate'),
]
