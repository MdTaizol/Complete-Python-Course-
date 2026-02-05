
#Variables do not need to be declared with any particular type, and can even change type after they have been set
# x = 4
# x = "sally"
# print(x)

#Casting
# x = str(908)
# y = int(3)
# z = float(3)
# print(x,y,z)

# Get the type
# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# Legal variable names:
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"
# print(myvar)
# print(my_var)
# print(_my_var)
# print(myVar)
# print(MYVAR)
# print(myvar2)

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Camel Case
# Each word, except the first, starts with a capital letter:
# myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
# MyVariableName = "John"

# Many Values to Multiple Variables
# x,y,z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# One value to MUltiple variables
# x = y = z = "Orange"
# print(x +" "+ y +" " + z)

# unpack of collection
# fruits = ["apple", "banana", "cherry"]
# x,y,z = fruits
# print(x + " " + y + " " + z)

#In the print() function, you output multiple variables, separated by a comma:
# x , y, z = 5, 10.5, "Hello"
# print(x , y, z)

# Global variable

# x = "awesome"
# def my():
#     x = "fantastic" #local variable
#     print("Python is " + x)
  
# my()  
# print("Python is " + x)


# def myfunc():
#     global x
#     x = "fantastic"
# myfunc()
# print("Python is " + x)

#If you change the global variable use global keyword.

# x = "awesome"
# def myfunc():
#     global x
#     x = "fantastic"
# myfunc()
# print("Python is " + x)
