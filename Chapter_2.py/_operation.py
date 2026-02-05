# operator module 
# print ( 10 +5)
# print( 10 -5)

# sum = 100 + 50 
# sum2 = sum + 250
# sum3 = sum2 + 500
# print(sum3)

# Arithmatic operators:
# ________________________
# x = 5
# y = 3
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y) #given float value
# print(x % y)
# print(x ** y)
# print(x // y) #given int value

# Assignment operators:
# ________________________

# x += 5
# x -= 2
# x *= 5
# x /= 2
# x %= 3
# x //=2
# x **=2
# x &=3
# x |=2
# x ^=2
# x >>=2
# x <<=2
#.032
# + print(x :=3) # walrus operator
# print(x)
# print(x)
# print(x)
# print(x)
# print(x)
# print(x)
# print(x)
# print(x)
# print(x)
# print(x)
# print(x)
# print(x)
# print(x)
#
#Walrus operator expample
# n = [1,2,3,4,5,6]
# c = len(n)
# if c > 4:
#     print(f"List has {c} elements")
# if (c := len(n)) > 7:
#     print(f"list has {c}elements")    

#comparison operators:
# ________________________
# x = 5
# y = 3

# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)
# print(x is y)
# print(x is not y)
# print(x in [1,2,3,4,5])
# print(1<x<10)
# print(1< x and x <10)
 
#logical operators:
# ________________________
# x = 5
# print(x >3 and x<10)
# print(x >3 or x < 10)
# print(not(x > 3 and x <10))

#iddentity operators:
# ________________________
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x  # x all value assign to z

print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x == y) # returns True because x is equal to y

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#Membership operators:
# ________________________
x = ["apple", "banana", "cherry"]
print("banana" in x)
print("pinapple" not in x)

text = "Hello, welcome to the world of pyhton programming."
print("welcome" in text)
print("to" not in text)

furits = ["apple ","bnana", "cherry"]
if "cherry" in furits:
    print("Yes, apple is a fruites")
else:
    print("No, apple is not a fruites")  

 #Bitwise operators:
 # ________________________

print(6 & 3) 
print(6|3)
print(6 ^ 3)
print(~6)
print(6 << 2)
print(float(6 >> 2))

# operator precedance:
# ________________________
print(10 +3 * 2)
print((10+3) * 2)
print( 100 - 2 ** 3)
print(6^3 +1)
print(6&3 +1)
print( 6|3 *2)
print( not 5 == 5)
print( 1 or 2 and 3) # or firstly find true ,always return left side value.
print( 2 or 5 + 10 and 8) # and fistly find false, always return right side vlaue first
 
L = 5
print(isinstance(L,int))