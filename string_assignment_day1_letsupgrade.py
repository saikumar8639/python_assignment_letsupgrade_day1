Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1='My name is sai kumar. My age is 19 years'
>>> str1.isprintable()
True
>>> str1.capitalize()
'My name is sai kumar. my age is 19 years'
>>> str1.index
<built-in method index of str object at 0x03084C38>
>>> str1.split(".")
['My name is sai kumar', ' My age is 19 years']
>>> str1
'My name is sai kumar. My age is 19 years'
>>> str1.upper()
'MY NAME IS SAI KUMAR. MY AGE IS 19 YEARS'
>>> str1.count()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    str1.count()
TypeError: count() takes at least 1 argument (0 given)
>>> str1.count("s")
4
>>> str1.islower()
False
>>> str1
'My name is sai kumar. My age is 19 years'
>>> str1.rsplit(,-1)
SyntaxError: invalid syntax
>>> str1.rsplit()
['My', 'name', 'is', 'sai', 'kumar.', 'My', 'age', 'is', '19', 'years']
>>> 