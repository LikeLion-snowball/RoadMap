from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('eventcreate/', eventcreate, name="eventcreate"),
    path('eventedit/<int:event_id>/', eventedit, name="eventedit"),
    #path('eventdelete/<int:event_id>', eventdelete, name="eventdelete"),
]