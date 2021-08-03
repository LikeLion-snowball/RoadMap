from django.urls import path
from . import views

urlpatterns = [
    path('', views.humanhome, name="humanhome"),
    path('notice/', views.notice, name="notice"),
    path('dpage/<int:post_id>/<int:user_id>', views.dpage, name="dpage"),
    path('dpage/<int:post_id>/', views.dpage_visitor, name="dpage_visitor"),
    path('hpostcreate/<int:user_id>/', views.hpostcreate, name="hpostcreate"),
    path('hpostdelete/<int:post_id>/', views.hpostdelete, name="hpostdelete"),
    path('hpostupdate/<int:post_id>/', views.hpostupdate, name="hpostupdate"),
<<<<<<< HEAD
    path('like/<int:post_id>', views.like, name="like"),
    path('h_result', views.h_result, name="h_result"),
=======
    path('post_search/', views.post_search, name='post_search'),
>>>>>>> dce5aa2f443779743b28fb8247a8fdd0c422a0a0
]