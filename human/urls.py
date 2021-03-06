from django.urls import path
from . import views
import human.views
urlpatterns = [
    path('', views.humanhome, name="humanhome"),
    path('notice/', views.notice, name="notice"),
    path('dpage/<int:post_id>/<int:user_id>', views.dpage, name="dpage"),
    path('dpage/<int:post_id>/', views.dpage_visitor, name="dpage_visitor"),
    path('hpostcreate/<int:user_id>/', views.hpostcreate, name="hpostcreate"),
    path('hpostdelete/<int:post_id>/', views.hpostdelete, name="hpostdelete"),
    path('hpostupdate/<int:post_id>/', views.hpostupdate, name="hpostupdate"),
    path('like/<int:post_id>', views.like, name="like"),
    path('h_result', views.h_result, name="h_result"),
    path('commentupdate/<int:post_id>/<int:user_id>/<int:comment_id>',views.commentupdate,name='commentupdate'),
    path('commentdelete/<int:post_id>/<int:user_id>/<int:comment_id>',views.commentdelete,name='commentdelete'),
    path('mycomment/<int:post_id>/<int:comment_id>/<int:user_id>', human.views.mycomment, name='mycomment'),
]