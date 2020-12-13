>>> family=['Father','Mother','son',"there ages :",50,45,10,'percentage of son:',98.89]
>>> family
['Father', 'Mother', 'son', 'there ages :', 50, 45, 10, 'percentage of son:', 98.89]
>>> family.reverse()
>>> family
[98.89, 'percentage of son:', 10, 45, 50, 'there ages :', 'son', 'Mother', 'Father']
>>> family.reverse()
>>> family
['Father', 'Mother', 'son', 'there ages :', 50, 45, 10, 'percentage of son:', 98.89]
>>> print('there are '+family[0]+family[1]+family[2]+' in the family')
there are FatherMotherson in the family
>>> family.pop()
98.89
>>> family
['Father', 'Mother', 'son', 'there ages :', 50, 45, 10, 'percentage of son:']
>>> family.append(99.8)
>>> print('family after editing marks of the son ')
family after editing marks of the son 
>>> family
['Father', 'Mother', 'son', 'there ages :', 50, 45, 10, 'percentage of son:', 99.8]
>>> family.count("son")
1
>>> family.index(45)
5
>>> family.copy()
['Father', 'Mother', 'son', 'there ages :', 50, 45, 10, 'percentage of son:', 99.8]
>>> fam=family.copy()
>>> fam
['Father', 'Mother', 'son', 'there ages :', 50, 45, 10, 'percentage of son:', 99.8]
>>> family.remove(10)
>>> family
['Father', 'Mother', 'son', 'there ages :', 50, 45, 'percentage of son:', 99.8]
>>> family.clear()
>>> family
[]
>>> type(family)
<class 'list'>
>>> 
