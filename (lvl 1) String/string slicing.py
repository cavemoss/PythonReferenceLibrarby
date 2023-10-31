# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> string slicing

name = 'what this'

name_first = name[0:4]
name_last = name[5:]
funky_name = name[0:9:2]
funky_name2 = name[::2]
name_reversed = name[::-1]

print(name_first, name_last, funky_name, funky_name2, name_reversed, sep='\n')


website = 'http://google.com'
website2 = 'http://wikipedia.com'

slice_index = slice(7, -4,)
print(website[slice_index])
print(website2[slice_index])
