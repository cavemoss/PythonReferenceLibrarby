from django.db import models

class ToDoList(models.Model):
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
