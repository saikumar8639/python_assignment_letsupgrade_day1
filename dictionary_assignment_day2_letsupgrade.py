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
