from django.urls import path
from . import views

urlpatterns = [
    path('mypage/', views.myPage, name="myPage"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/projectcreate/', views.projectcreate, name='projectcreate'),
    path('portfolio/activitycreate/', views.activitycreate, name='activitycreate'),
]