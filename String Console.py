Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String "",'',''' '''
>>> x = "sahil"
>>> x = 'jyoti'
>>> x = '''
a
b
c
d
e'''
>>> x
'\na\nb\nc\nd\ne'
>>> print(x)

a
b
c
d
e
>>> x = "welcome to python programming class"
>>> #String - Immutable data type
>>> x.lower()
'welcome to python programming class'
>>> x
'welcome to python programming class'
>>> x.upper()
'WELCOME TO PYTHON PROGRAMMING CLASS'
>>> x
'welcome to python programming class'
>>> x = x.upper()
>>> x
'WELCOME TO PYTHON PROGRAMMING CLASS'
>>> x
'WELCOME TO PYTHON PROGRAMMING CLASS'
>>> x = "hello JyOtI"
>>> x.capitalize()
'Hello jyoti'
>>> x.title()
'Hello Jyoti'
>>> x.swapcase()
'HELLO jYoTi'
>>> x
'hello JyOtI'
>>> x.replace("hello","Hi")
'Hi JyOtI'
>>> x
'hello JyOtI'
>>> x
'hello JyOtI'
>>> x.count('l')
2
>>> x
'hello JyOtI'
>>> #indexing
>>> x[0]
'h'
>>> x[1]
'e'
>>> x[2]
'l'
>>> x[-1]
'I'
>>> x[-3]
'O'
>>> #Slicing
>>> x
'hello JyOtI'
>>> x[0:4]
'hell'
>>> x[0:5]
'hello'
>>> x[:7]
'hello J'
>>> x[4:]
'o JyOtI'
>>> x[:]
'hello JyOtI'
>>> x[::-1]
'ItOyJ olleh'
>>> x
'hello JyOtI'
>>> x[0:9]
'hello JyO'
>>> x[0:9:1]
'hello JyO'
>>> x[0:9:2]
'hloJO'
>>> x
'hello JyOtI'
>>> x.find("e")
1
>>> x.index("e")
1
>>> x.find("X")
-1
>>> x.index("X")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    x.index("X")
ValueError: substring not found
>>> x
'hello JyOtI'
>>> x.split()
['hello', 'JyOtI']
>>> x.split()[0]
'hello'
>>> x.split()[1]
'JyOtI'
>>> x = "JYOTI"
>>> len(x)
5
>>> x.center(6)
'JYOTI '
>>> x.center(10,"+")
'++JYOTI+++'
>>> x = x.center(10,"+")
>>> x
'++JYOTI+++'
>>> x.lstrip()
'++JYOTI+++'
>>> x.lstrip("+")
'JYOTI+++'
>>> x.rstrip("+")
'++JYOTI'
>>> x.strip("+")
'JYOTI'
>>> x.zfill(20)
'+0000000000+JYOTI+++'
>>> x = "hey"
>>> x.isalpha()
True
>>> x = "123Hey"
>>> x.isalnum()
True
>>> x = "helllo word"
>>> x.startswith("helllo")
True
>>> x.endswith("Z")
False
>>> x.endswith("d")
True
>>> 