from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *

urlpatterns = [
    path('detail/<int:qna_id>/<int:user_id>', detail, name="detail"),
    path('detail/<int:qna_id>/', detail_visitor, name="detail_visitor"),
    path('q_result', q_result, name="q_result"),
    path('like/<int:qna_id>', like, name="qlike"),
    path('create',create, name="create"),
    path('postcreate/<int:user_id>', postcreate, name='postcreate'),
    path('postupdate/<int:qna_id>', postupdate, name='postupdate'),
    path('postdelete/<int:qna_id>',postdelete, name='postdelete'),
    path('commentupdate/<int:qna_id>/<int:comment_id>/<int:user_id>', qcommentupdate,name='qcommentupdate'),
    path('commentdelete/<int:qna_id>/<int:comment_id>/<int:user_id>', qcommentdelete,name='qcommentdelete'),
]
