from django.shortcuts import render
from .models import ToDoList


def index(response):
    return render(response, "app1/base.html")

def home(response):
    return render(response, "app1/home.html")

def view_list(response, name):

    todo_list = ToDoList.objects.get(name=name)
    
    variables: dict = {
        "ls" : todo_list
    }
    return render(response, "app1/data.html", variables)
