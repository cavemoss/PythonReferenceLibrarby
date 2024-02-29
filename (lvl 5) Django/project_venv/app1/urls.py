from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="base"),
    path("home/", views.home, name="home"),
    path("<str:name>", views.view_list, name="list"),
    path("create/", views.create, name="create"),
    path("view/", views.view_all, name="view"),
]
