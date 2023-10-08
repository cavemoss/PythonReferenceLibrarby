# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> string slicing

name = 'what this'

name_first = name[0:4]
name_last = name[5:9]
funky_name = name[0:9:2]
funky_name2 = name[::2]
name_reversed = name[::-1]

print(name_first)
print(name_last)
print(funky_name)
print(funky_name2)
print(name_reversed)


website = 'http://google.com'
website2 = 'http://wikipedia.com'

slice_index = slice(7, -4,)
print(website[slice_index])
print(website2[slice_index])
