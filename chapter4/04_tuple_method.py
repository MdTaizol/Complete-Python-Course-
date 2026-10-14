a = (1,"Taizol",345.5,23,False,'s')
# Tuple is a inmutedable data type.
no = a.count('s') # it's called your how many time value exists.
print(no)
i = a.index(1) #its called your index number.
print(i)
print(len(a))

#concate the tuple:
tuple1 = (1,2,"hello")
tuple2 = (3,4,"world")
print(tuple1 + tuple2)

#repetad the value:

my_tuple = (1,23,4,5)
repeated = my_tuple * 3
print(repeated)

# check the value is exists in this tuple using:

my = (12,11,13)
print(11 in my)
print(12 in my)
print(my[0:1])

# respectally divided the tuple:

a,b,c = my
print(a,b,c)








