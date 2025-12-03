Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x = -12.56
print(abs(x))
12.56
print(round(10.345,2))
10.35
print(pow(2,3,5))
3
print(int(12.99))
12
print(float(12))
12.0
z= complex(2,3)
print(z)
(2+3j)
result=divmod(17,5)
print(result)
(3, 2)
print(bin(25))
0b11001
print(oct(10))
0o12
print(hex(10))
0xa
s = "hello world"
print(s.upper())
HELLO WORLD
s = "HeLLo"
print(s.lower())
hello
s = "welcome to python"
print(s.title())
Welcome To Python
s = "python programming"
print(s.capitalize())
Python programming
s = "Hello WORLD"
print(s.swapcase())
hELLO world
s = "   hello   "
print(s.strip())
hello
s = "   hello"
print(s.lstrip())
hello
>>> print(s.rstrip())
   hello
>>> s = "this is Python"
>>> print(s.replace("Python", "Java"))
this is Java
>>> s = "apple,banana,grapes"
>>> print(s.split(","))
['apple', 'banana', 'grapes']
>>> s = "Hello\nWorld\nPython"
>>> print(s.splitlines())
['Hello', 'World', 'Python']
>>> s= "Jothiesh"
>>> s.isupper
<built-in method isupper of str object at 0x0000020A686B33B0>
>>> print(s.isupper())
False
>>> s= jothiesh
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s= jothiesh
NameError: name 'jothiesh' is not defined
>>> s= "jothiesh"
>>> print(s.islower())
True
>>> print(s.istitle())
False
>>> print(s.isalnum())
True
>>> print(s.isdigit())
False
>>> print(s.isalpha())
True
>>> print(s.count(h))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(s.count(h))
NameError: name 'h' is not defined
>>> print(s.count("h"))
2
>>> name = "Jothiesh"
>>> age = 19
>>> print("My name is {} and I am {} years old".format(name, age))
My name is Jothiesh and I am 19 years old
>>> data = {"name": "Jothiesh", "age": 19}
>>> print("My name is {name} and I am {age}".format_map(data))
My name is Jothiesh and I am 19
