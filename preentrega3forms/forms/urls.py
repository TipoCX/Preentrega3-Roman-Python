from .views import *
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", index, name="home"),
    path("createuser", user_create_view, name="create-user"),
    path("group/<userid>", group_view, name="group"),
    path("login", login_view, name="login"),
    path("creategroup", group_create_view, name="create-group"),

]
