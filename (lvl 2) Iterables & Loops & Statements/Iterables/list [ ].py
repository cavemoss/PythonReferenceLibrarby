# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list []

empty_list = list()

the_list = ['item1', 'item2', 'wath?', 'item4']
the_list[2] = 'item3'

print(the_list)
for i in the_list:          
    print(i)                    
for x in the_list:              
    print(x, end=' ')

print(the_list[2])
print(the_list[0]+' '+the_list[3])

the_list.append('item5')        # append ((more) an item at the end)
the_list.remove('item3')        # remove (remove an item form the list)
the_list.pop()                  # pop (remove the last item)
the_list.insert(1, 'item1.5')   # insert (insert a new item at an index)
the_list.clear()                # clear (clear the list of any items)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list of lists [][]

drinks = ['coffee', 'soda', 'tea']
dinner = ['bread', 'fresh bread', 'more bread']
dessert = ['cake', 'ice cream']

food = [drinks, dinner, dessert]
print(food)
print(food[1])
print(food[1][2])
