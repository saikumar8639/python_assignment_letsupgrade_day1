Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> family=['Father','Mother','son',"there ages :",50,45,10,'percentage of son:',98.89]
>>> family
['Father', 'Mother', 'son', 'there ages :', 50, 45, 10, 'percentage of son:', 98.89]
>>> family.reverse()
>>> family
[98.89, 'percentage of son:', 10, 45, 50, 'there ages :', 'son', 'Mother', 'Father']
>>> family.reverse()
>>> family
['Father', 'Mother', 'son', 'there ages :', 50, 45, 10, 'percentage of son:', 98.89]
>>> print('there are '+famiy[0]+family[1]+family[2]+" in the family")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('there are '+famiy[0]+family[1]+family[2]+" in the family")
NameError: name 'famiy' is not defined
>>> print('there are '+famiy[0]+family[1]+family[2]+' in the family')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print('there are '+famiy[0]+family[1]+family[2]+' in the family')
NameError: name 'famiy' is not defined
>>> print('there are '+family[0]+family[1]+family[2]+' in the family')
there are FatherMotherson in the family
>>> family.pop(98.89)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    family.pop(98.89)
TypeError: integer argument expected, got float
>>> family.pop()
98.89
>>> family
['Father', 'Mother', 'son', 'there ages :', 50, 45, 10, 'percentage of son:']
>>> family.append(99.8)
>>> print('family after editing marks of the son '+family)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print('family after editing marks of the son '+family)
TypeError: can only concatenate str (not "list") to str
>>> print('family after editing marks of the son ')
family after editing marks of the son 
>>> family
['Father', 'Mother', 'son', 'there ages :', 50, 45, 10, 'percentage of son:', 99.8]
>>> family.count()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    family.count()
TypeError: count() takes exactly one argument (0 given)
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