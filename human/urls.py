from django.urls import path
from . import views

urlpatterns = [
    path('', views.humanhome, name="humanhome"),
    path('notice/', views.notice, name="notice"),
    path('dpage/<int:post_id>', views.dpage, name="dpage"),
    path('hpostcreate/<int:user_id>', views.hpostcreate, name="hpostcreate"),
    path('hpostdelete/<int:post_id>/', views.hpostdelete, name="hpostdelete"),
    path('hpostupdate/<int:post_id>/', views.hpostupdate, name="hpostupdate"),
]