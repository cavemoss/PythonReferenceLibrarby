from app1.models import ToDoList

# add a todo list 
my_list = ToDoList(name="My List")
my_list.save()

# query todo lists
ToDoList.objects.all() # <QuerySet [<ToDoList: My List>]>
ToDoList.objects.get(id=1)  # <ToDoList: My List>
ToDoList.objects.get(name="My List")  # <ToDoList: My List>

# add todo list items
my_list.item_set.create(text="Drink coffee", complete=True)  # <Item: Drink coffee>
my_list.item_set.create(text="Eat cheetos", complete=False)  # <Item: Eat cheetos>
my_list.item_set.create(text="Eat chicken", complete=True)  # <Item: Eat chicken>

# query todo list items
my_list.item_set.all()  # <QuerySet [<Item: Drink coffee>, <Item: Eat cheetos>, <Item: Eat chicken>]>
my_list.item_set.get(id=1)  # <Item: Drink coffee>
my_list.item_set.get(text="Drink coffee")  # <Item: Drink coffee>


tdl = ToDoList.objects

# query objects with filter
tdl.filter(id = 1)  # <QuerySet [<ToDoList: My List>]>
tdl.filter(id = 2)  # <QuerySet []>
tdl.filter(name__startswith = 'My')  # <QuerySet [<ToDoList: My List>]>
tdl.filter(name__startswith = 'my')  # <QuerySet []>

# deleting objects from database
del_object = tdl.get(name="My List")
del_object.delete()  # (1, {'app1.Item': 3, 'app1.ToDoList': 1})
