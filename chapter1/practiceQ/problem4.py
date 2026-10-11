# write a python program to print the contents of a directory using the os module. search online for the function which does that.

import os 

# Sepecify the directory path you want to list:

directory_path = '/'

#List all files and directories in the specified path:

contents = os.listdir(directory_path)

#print each file and directory name:
for item in contents:
    print(item)




# import os 
# path ='/'
# c = os.listdir(path)
# for i in c:
#     print(i)
 