from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="home"),
    path('home', views.home, name="home view"),
    path('home/edit', views.profile_edit, name="user_edit"),
    path('home/userlist', views.user_list, name="user_list"),
    path('register',views.register,name="detail view"),
    path('details',views.details,name="detail view")
    ]