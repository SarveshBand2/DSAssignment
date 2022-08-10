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


'''Write a Python program which accepts a sequence of comma-separated numbers from the
user and generates a list and a tuple with those numbers.
'''


nums = input("Input some comma seperated numbers: ")
list = nums.split(",")
tuple = tuple(list)
print(list)
print(tuple)


'''Write a Python program to display the first and last colours from the following list.
color_list = ["Red","Green","White" ,"Black"]
'''
color_list = ["Red","Green","White" ,"Black"]
print("First Color: ", color_list[0])
print("Last Color: " ,color_list[3])

'''Write a Python program to print the documents (syntax, description etc.) of Python built-in
function(s).'''

print(abs.__doc__, '\n')
print(all.__doc__, '\n')
print(any.__doc__, '\n')
print(ascii.__doc__, '\n')
print(bin.__doc__, '\n')
print(bool.__doc__, '\n')
print(chr.__doc__, '\n')


'''Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''
import calendar
year = 2022
month = 8
print(calendar.month(year, month))


'''Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days'''

from datetime import date
date1 = date(2014,7,2)
date2 = date(2014,7,11)
num_days = date2 - date1
print(num_days.days)

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

''' Write a Python program to create a histogram from a given list of integers.'''

'''Write a Python program to concatenate all elements in a list into a string and return it.'''

list = ['7','3','1','A','Z','6']
z=' '
for i in list:
    z =  z + i
print(z)


''' Write a Python program to print out a set containing all the colors from color_list_1 which are
not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
'''

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

'''Write a Python program to get the current username'''

import os
print(os.getlogin())


'''Write a program to get execution time for a Python method.'''

import time
start = time.time()
a=0

for i in range (1000):
    a += (i**100)
end = time.time()

print(end-start)


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


'''Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.'''

from array import *
arr = ([1,23,14,34,75])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])


'''Write a Python program to reverse the order of the items in the array.
'''

from array import *
arr = ([1,23,14,34,75])
print(list(reversed(arr)))


'''Write a Python program to get the number of occurrences of a specified element in an
array.'''
from array import *
list = ([50,100,150,100,200,50,100,600,50,200,320,100,400,100,100])
print(list)
num = int(input("Enter num from above list to find its total occurrence: "))
print(list.count(num))



''' Write a Python program to create a set.'''

my_set = (50,100,150,100,200,50,100,600,50,200,320,100,400,100,100)
print(set(my_set))


'''Write a Python program to iteration over sets.
'''

my_set = set('Hello World!!')
for i in my_set :
    print(i)

'''Write a Python program to add member(s) in a set.
'''

my_set = {50,100,150,100,200,50,100,600,50,200,320,100,400,100,100}
my_set.update([250,700,30,50])
print(my_set)


''' Write a Python program to remove item(s) from set'''

my_set = {320, 100, 200, 400, 50, 150, 600, 250, 700, 30}
my_set.remove(100)
print(my_set)

my_set.pop()
print(my_set)

print(my_set.pop(),'\n',my_set)


'''Write a Python program to remove an item from a set if it is present in the set.'''
my_set = {320, 100, 200, 400, 50, 150, 600, 250, 700, 30}
print(my_set)
i = int(input("Enter a num to remove from above set: "))
if i in my_set:
    my_set.remove(i)
    print(my_set)
else:
    print("Please Enter a num from set!")


