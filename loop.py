Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(1,8):
	print(i)

	
1
2
3
4
5
6
7
>>> 
>>> for i in range(2,11,2):
	print(i)

	
2
4
6
8
10
>>> for i in range(1,18,3)
SyntaxError: invalid syntax
>>>  for i in range(1,18,3):
	
SyntaxError: unexpected indent
>>> for i in range(1,5,3):
	print(i)

	
1
4
>>> for i in reversed(range(1,18)):
	print(i)

	
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
>>> for i in sum(range(1,11)):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    for i in sum(range(1,11)):
TypeError: 'int' object is not iterable
>>> for i in range(1,11,10)
SyntaxError: invalid syntax
>>> for i in range(1,11,10):
	print(i)

	
1
>>> for i in range(1,50,10):
	print(i)

	
1
11
21
31
41
>>> 
>>> for i in range(1,11,5):
	print(i)

	
1
6
>>> for i in range(1,10,10):
	print(i)

	
1
>>> res = 0
>>> for i in range(1,11):
	res=res+i

>>> res
55
>>> 1+2+3+4+5+6+7+8+9+10
55
>>> #find the sum of the no.
>>> x = 0
>>> for i in range(157,157)
SyntaxError: invalid syntax
>>> x = 0
>>> for i in range(157,157):
	
SyntaxError: multiple statements found while compiling a single statement
>>> x = 0
>>> for i in range(15,15):
	x=i(x+x)

	
>>> 485
485
>>> 4+8+5
17
>>> x = 0
>>> for i in range(1,15):
	print(i)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
>>> for i in range(15,17):
	print(i)

	
15
16
>>> res = 0
>>> for i in range(3)
SyntaxError: invalid syntax
>>> res = 0
>>> for i in range(3):
	
SyntaxError: multiple statements found while compiling a single statement
>>> res = 0
>>> x = 127
>>> for i in range(3):
	rem = x%10
	x = X//10
	res = res+rem

	
Traceback (most recent call last):
  File "<pyshell#72>", line 3, in <module>
    x = X//10
NameError: name 'X' is not defined
>>> res = 0
>>> x = 127
>>> for i in range(3):
	rem = x%10
	x = x//10
	res = res+rem
	
SyntaxError: multiple statements found while compiling a single statement
>>>  res = 0
>>> x = 127
>>> for i in range(3):
	rem = x%10
	x = x//10
	res = res+rem
	
SyntaxError: unexpected indent
>>>  res = 0
>>> x = 127
>>> for i in range(3):
	rem = x%10
	x = x//10
	res = res+rem





	
	res = res+rem
KeyboardInterrupt
>>> for i in range(3):
	rem = x%10
	x = x//10
	res = res+rem

>>> res
10
>>> 
