from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
    # link this model to User 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # attributes
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    # link this model to ToDoList 
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # attributes
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
