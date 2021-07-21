from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [
    path('<int:qna_id>', detail, name="detail"),
    path('create',create, name="create"),
    path('postcreate', postcreate, name='postcreate'),
    path('edit', edit, name='edit'),
    path('postupdate/<int:qna_id>', postupdate, name='postupdate'),
    path('postdelete/<int:qna_id>',postdelete, name='postdelete'),
]
