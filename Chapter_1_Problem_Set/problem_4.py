#wrtie a python  program to print the contents of a directory using os module.

import os
# specify the directory path 
di ='.'
content = os.listdir(di)
# print each file and directory name
for i in content:
    print(i)
    

