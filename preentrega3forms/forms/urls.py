from .views import *
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", index, name="home"),
    path("createuser", user_create_view, name="create-user"),
    path("group", group_view, name="group")
]
