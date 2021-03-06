from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name="info"),
    path('result/', views.result, name="result"),
    path('scrap/<int:recruit_id>', views.scrap, name="scrap"),
]