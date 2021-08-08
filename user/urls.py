from django.urls import path
import info.views
from . import views
import human.views

urlpatterns = [
    path('mypage/', views.myPage, name="myPage"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolios/', views.others_portfolio, name="others_portfolio"),
    path('change/', views.port_open, name="port_open"),
    path('portfolio/projectcreate/', views.projectcreate, name='projectcreate'),
    path('portfolio/projectupdate/<int:project_id>', views.projectupdate, name='projectupdate'),
    path('portfolio/projectdelete/<int:project_id>', views.projectdelete, name='projectdelete'),
    path('portfolio/activitycreate/', views.activitycreate, name='activitycreate'),
    path('portfolio/activityupdate/<int:activity_id>', views.activityupdate, name='activityupdate'),
    path('portfolio/activitydelete/<int:activity_id>', views.activitydelete, name='activitydelete'),
    path('myscrap/', info.views.my_scrap, name="myscrap"),
    path('mycomment/', human.views.mycomment, name="mycomment"),
    path('mypost/', human.views.my_post, name="mypost"),
    #path('human/commentupdate/<int:post_id>/<int:comment_id>/<int:user_id>',human.views.commentupdate,name='commentupdate'),
   # path('human/commentdelete/<int:post_id>/<int:comment_id>/<int:user_id>',human.views.commentdelete,name='commentdelete'),
    #path('human/dpage/<int:post_id>/<int:user_id>', human.views.dpage, name="dpage"),
    #path('human/dpage/<int:post_id>/', human.views.dpage_visitor, name="dpage_visitor"),
]