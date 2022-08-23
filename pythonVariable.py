'''# comments are green and used to explain code they start with #
# python has no command for declaring variables, a variable is created the moment you first
#assign a value to it
x=5
y="john"
print(y)
print(x)

 #variables have types
x= 4 #x is of type int
x= "sally" #x is now type str
#casting
#casting is to specify the data type of variable
x= str (3)
#x will be string or word 3
y= int (3)
#y will be number 3
z= float (3)
# z will be decimal 3

#how to print the type 
x = 5 
y = "john"
print (type(x))
print (type(y))
# Note: "" is the same as '' so "x" is same as 'x'
a = 4
A = "sally"
#A will NOT overide a
#NAMING VARIABLES:
#1 a variable must start with a letter or underscore 
#2 a variable name cannot start with a number
#3 A variable name is case sensitive 
myvar = "john"
my_var = "john"
_my_var = "john"
myVar = "john"
MYVAR = "john"
myvar2 = "john"
#illeagal naming
2myvar = "john"
my-var = "john"
my var = "john"

#assign Multiple values
x,y,z= "orange","bannana","cherry"
print(x)
print(y)
print(z)
#assign 1 value to multiple variables
x=y=z= "orange"
print(x)
print(y)
print(z)
'''
# Random Number
import random

print(random.randrange(1,10))

#concatenation
a = "Hello"
b = "patricia"
c = a+" "+b
print(c)
# String Format
Age = str(36)
txt = "My name is Patricia, I am "+Age
print(txt)

#Escape Charecters
#To insert charecters that are illeagal in a string , use an escape charecter in this case /
#text = "we're fabulous" Unicorns "from amazingland"
text = "We're fabulous\"unicorns\" from amazingland"
print(text)
