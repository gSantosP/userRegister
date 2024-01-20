from django.urls import path
from app_user_register import views

urlpatterns = [
    #Route, View, Name.
    #users.com
    path("", views.home, name="home"),
    
    #users.com/users
    path("users", views.users, name="users_list")
]