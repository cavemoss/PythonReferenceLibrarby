from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import ToDoList
from .forms import CreateNewList


def index(response):
    return redirect('/login/')

def home(response):
    return render(response, "app1/home.html", {"name" : response.user})

def view_list(response, name):
    ls = response.user.todolist_set.get(name=name)
    
    if response.method == 'POST':
        print(response.POST)  # returns a dictionary

        # if button with the value 'save' has been pressed
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        # if button with the value 'newItem' has been pressed
        elif response.POST.get("newItem"):
            text = response.POST.get("new")
            if len(text) > 2:
                ls.item_set.create(text=text, complete=False)
            else:
                print('invalid input')
            
    return render(response, "app1/data.html", {"ls" : ls})

def create(response):
    
    if response.method == 'POST':
        form = CreateNewList(response.POST)
        if form.is_valid():
            user_input: dict = form.cleaned_data  # returns dictionary of values input by user

            if ToDoList.objects.filter(name=user_input["name"]).__len__() == 0:
                response.user.todolist_set.create(name=user_input["name"])
                ls = response.user.todolist_set.get(name=user_input['name'])
                return HttpResponseRedirect(f"/{ls}")
            else:
                return HttpResponseRedirect("/create/")
    else:
        form = CreateNewList()

    return render(response, "app1/create.html", {"form" : form})

def view_all(response):
    return render(response, 'app1/view.html', {"ls" : response.user.todolist_set.all()})
