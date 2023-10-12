# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> zip(*iterables)

username = ['dude', 'bro', 'mister']
password = ('p@ssword', 'abc123', 'guest')

users = zip(username, password)
print(type(users))

users = list(zip(username, password))
print(type(users))
for i in users:
    print(i)

users = dict(zip(username, password))
print(type(users))
for key, value in users.items():
    print(key+':'+value)

login_date = ['1/1/2021', '1/2/22021', '1/3/2021']

users_login = zip(username, password, login_date)
for i in users_login:
    print(i)
