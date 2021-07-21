#from django.contrib import admin
from django.urls import path

import teamapp.views

urlpatterns = [
    path('team_new/', teamapp.views.team_new, name='team_new'),
    path('team_detail/<int:team_id>', teamapp.views.team_detail, name="team_detail"),
    path('team_create/', teamapp.views.team_create, name="team_create"),
    path('team_postcreate/', teamapp.views.team_postcreate, name='team_postcreate'),
]

