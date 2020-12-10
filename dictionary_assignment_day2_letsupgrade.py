Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> diction={'sai':48,'sampath':49,'naveen':47,'shiva':48}
>>> diction
{'sai': 48, 'sampath': 49, 'naveen': 47, 'shiva': 48}
>>> diction.values()
dict_values([48, 49, 47, 48])
>>> diction.keys()
dict_keys(['sai', 'sampath', 'naveen', 'shiva'])
>>> diction.setdefault("sai")
48
>>> d1=diction.copy()
>>> d1
{'sai': 48, 'sampath': 49, 'naveen': 47, 'shiva': 48}
>>> diction.popitem()
('shiva', 48)
>>> diction.pop("sampath")
49
>>> diction.clear()
>>> diction
{}
>>> 