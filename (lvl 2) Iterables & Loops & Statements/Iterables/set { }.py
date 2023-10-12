# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> set {}

empty_set = set()

utensils = {'fork', 'spoon', 'knife', 'knife', 'knife', 'knife'}
dishes = {'bowl', 'plate', 'cup', 'knife'}

utensils.add('napkin')                  # (more) ((more) an item to a set)
utensils.remove('knife')                # remove (remove an item for a set)

utensils.update(dishes)                 # update ((more) items form one set to another)
dinner_table = utensils.union(dishes)   # union (combine two sets together)

for i in utensils:
    print(i, end=' ')
print()

for i in dinner_table:
    print(i, end=' ')
print()

print(utensils.difference(dishes))      # difference
print(utensils.intersection(dishes))    # intersection
