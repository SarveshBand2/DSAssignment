'''1. Write a Python program which accepts the user's first and last name and prints them in
reverse order with a space between them.
'''

from ctypes import LittleEndianStructure
from selectors import EpollSelector
import mysqlx

from numpy import arctanh


first = input("Enter Your First Name: ")
last = input("Enter Your Last Name: ")

print(last, first)

'''Output'''
Enter Your First Name: Sarvesh 
Enter Your Last Name: Band
Band Sarvesh
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 
    
    
'''Write a Python program which accepts a sequence of comma-separated numbers from the
user and generates a list and a tuple with those numbers.
'''


nums = input("Input some comma seperated numbers: ")
list = nums.split(",")
tuple = tuple(list)
print(list)
print(tuple)

'''Output'''
Input some comma seperated numbers: 1,3,5,8,10
['1', '3', '5', '8', '10']
('1', '3', '5', '8', '10')
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 
    
    

'''Write a Python program to display the first and last colours from the following list.
color_list = ["Red","Green","White" ,"Black"]
'''
color_list = ["Red","Green","White" ,"Black"]
print("First Color: ", color_list[0])
print("Last Color: " ,color_list[3])

'''Output'''
First Color:  Red
Last Color:  Black
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 

    
    
'''Write a Python program to print the documents (syntax, description etc.) of Python built-in
function(s).'''

print(abs.__doc__, '\n')
print(all.__doc__, '\n')
print(any.__doc__, '\n')
print(ascii.__doc__, '\n')
print(bin.__doc__, '\n')
print(bool.__doc__, '\n')
print(chr.__doc__, '\n')

'''Output'''
Return the absolute value of the argument. 

Return True if bool(x) is True for all values x in the iterable.

If the iterable is empty, return True. 

Return True if bool(x) is True for any x in the iterable.

If the iterable is empty, return False. 

Return an ASCII-only representation of an object.

As repr(), return a string containing a printable representation of an
object, but escape the non-ASCII characters in the string returned by
repr() using \\x, \\u or \\U escapes. This generates a string similar
to that returned by repr() in Python 2. 

Return the binary representation of an integer.

   >>> bin(2796202)
   '0b1010101010101010101010'

bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.

Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

PS C:\Users\sarve\Desktop\Programming\DS Assignments> 
    
    
    
'''Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''
import calendar
year = 2022
month = 8
print(calendar.month(year, month))

'''Output'''
    August 2022
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

PS C:\Users\sarve\Desktop\Programming\DS Assignments> 
    
    
    
'''Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''

from datetime import date
date1 = date(2014,7,2)
date2 = date(2014,7,11)
num_days = date2 - date1
print(num_days.days)

'''Output'''
9
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 

    
    
'''Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''

list1 = [1,5,8,3]
x = int(input("Enter a no to Search in Given List: "))
if x in list1:
    print("True")
else:
    print("False")

'''Output'''
Enter a no to Search in Given List: 3
True
PS C:\Users\sarve\Desktop\Programming\DS Assignments> python -u "c:\Users\sarve\Desktop\Programming\DS Assignments\tempCodeRunnerFile.py"
Enter a no to Search in Given List: 4
False
PS C:\Users\sarve\Desktop\Programming\DS Assignments>

    
    
''' Write a Python program to create a histogram from a given list of integers.'''

'''Write a Python program to concatenate all elements in a list into a string and return it.'''

list = ['7','3','1','A','Z','6']
z=' '
for i in list:
    z =  z + i
print(z)

'''Output'''
PS C:\Users\sarve\Desktop\Programming\DS Assignments> python -u "c:\Users\sarve\Desktop\Programming\DS Assignments\tempCodeRunnerFile.py"
 731AZ6
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 

    
    
''' Write a Python program to print out a set containing all the colors from color_list_1 which are
not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
'''

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

'''Output'''
{'White', 'Black'}
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 
    
    
    
'''Write a Python program to get the current username'''

import os
print(os.getlogin())

'''Output'''
PS C:\Users\sarve\Desktop\Programming\DS Assignments> python -u "c:\Users\sarve\Desktop\Programming\DS Assignments\tempCodeRunnerFile.py"
sarve
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 
    
    

'''Write a program to get execution time for a Python method.'''

import time
start = time.time()
a=0

for i in range (1000):
    a += (i**100)
end = time.time()

print(end-start)

'''Output'''
PS C:\Users\sarve\Desktop\Programming\DS Assignments> python -u "c:\Users\sarve\Desktop\Programming\DS Assignments\tempCodeRunnerFile.py"
0.0010297298431396484
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 
    
    
    
'''Write a Python program to sort three integers without using conditional statements and
loops.
'''

num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))
num3 = int(input("Enter Third Num: "))

a = min(num1,num2,num3)
b = max(num1,num2,num3)
c = (num1+num2+num3)-a-b
print(a,c,b)

'''Output'''
Enter First Num: 7
Enter Second Num: 3
Enter Third Num: 5
3 5 7
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 
    
    
    
'''Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.'''

from array import *
arr = ([1,23,14,34,75])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

'''Output'''
PS C:\Users\sarve\Desktop\Programming\DS Assignments> python -u "c:\Users\sarve\Desktop\Programming\DS Assignments\tempCodeRunnerFile.py"
1
23
14
34
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 

    
    
    
'''Write a Python program to reverse the order of the items in the array.
'''

from array import *
arr = ([1,23,14,34,75])
print(list(reversed(arr)))

'''Output'''
PS C:\Users\sarve\Desktop\Programming\DS Assignments> python -u "c:\Users\sarve\Desktop\Programming\DS Assignments\tempCodeRunnerFile.py"
[75, 34, 14, 23, 1]
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 
    
    
    
'''Write a Python program to get the number of occurrences of a specified element in an
array.'''

from array import *
list = ([50,100,150,100,200,50,100,600,50,200,320,100,400,100,100])
print(list)
num = int(input("Enter num from above list to find its total occurrence: "))
print(list.count(num))

'''Output'''
[50, 100, 150, 100, 200, 50, 100, 600, 50, 200, 320, 100, 400, 100, 100]
Enter num from above list to find its total occurrence: 100
6
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 

    
    
''' Write a Python program to create a set.'''

my_set = (50,100,150,100,200,50,100,600,50,200,320,100,400,100,100)
print(set(my_set))

'''Output'''
PS C:\Users\sarve\Desktop\Programming\DS Assignments> python -u "c:\Users\sarve\Desktop\Programming\DS Assignments\tempCodeRunnerFile.py"
{320, 100, 200, 400, 50, 150, 600}
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 
    
    
'''Write a Python program to iteration over sets.
'''

my_set = set('Hello World!!')
for i in my_set :
    print(i)

'''Output'''
H
e
!
 
d
W
o
r
l
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 


    
'''Write a Python program to add member(s) in a set.
'''

my_set = {50,100,150,100,200,50,100,600,50,200,320,100,400,100,100}
print("Default Set is: ",my_set)
my_set.update([250,700,30,50])
print("Set after update: ",my_set)

'''Output'''
PS C:\Users\sarve\Desktop\Programming\DS Assignments> python -u "c:\Users\sarve\Desktop\Programming\DS Assignments\tempCodeRunnerFile.py"
Default Set is:  {320, 100, 200, 400, 50, 150, 600}
Set after update:  {320, 100, 200, 400, 50, 150, 600, 250, 700, 30}
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 

    
    
''' Write a Python program to remove item(s) from set'''

my_set = {320, 100, 200, 400, 50, 150, 600, 250, 700, 30}
my_set.remove(100)
print(my_set)

my_set.pop()
print(my_set)

print(my_set.pop(),'\n',my_set)

'''Output'''
PS C:\Users\sarve\Desktop\Programming\DS Assignments> python -u "c:\Users\sarve\Desktop\Programming\DS Assignments\tempCodeRunnerFile.py"
{320, 200, 400, 50, 150, 600, 250, 700, 30}
{200, 400, 50, 150, 600, 250, 700, 30}
200 
 {400, 50, 150, 600, 250, 700, 30}
PS C:\Users\sarve\Desktop\Programming\DS Assignments> 
    
    

'''Write a Python program to remove an item from a set if it is present in the set.'''
my_set = {320, 100, 200, 400, 50, 150, 600, 250, 700, 30}
print(my_set)
i = int(input("Enter a num to remove from above set: "))
if i in my_set:
    my_set.remove(i)
    print(my_set)
else:
    print("Please Enter a num from set!")

'''Output'''
PS C:\Users\sarve\Desktop\Programming\DS Assignments> python -u "c:\Users\sarve\Desktop\Programming\DS Assignments\tempCodeRunnerFile.py"
{320, 100, 200, 400, 50, 150, 600, 250, 700, 30}
Enter a num to remove from above set: 400
{320, 100, 200, 50, 150, 600, 250, 700, 30}
PS C:\Users\sarve\Desktop\Programming\DS Assignments> python -u "c:\Users\sarve\Desktop\Programming\DS Assignments\tempCodeRunnerFile.py"
{320, 100, 200, 400, 50, 150, 600, 250, 700, 30}
Enter a num to remove from above set: 120
Please Enter a num from set!
PS C:\Users\sarve\Desktop\Programming\DS Assignments>

