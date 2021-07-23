from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('event/new/', event, name="new"),
    path('event/edit/<int:event_id>', event, name="edit"),
]