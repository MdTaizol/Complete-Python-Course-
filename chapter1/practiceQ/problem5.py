import os

#Select the directory whose content you want to list :

directory_path ='/'

#use the os module to list the directory content:
content = os.listdir(directory_path)
# Print the content of the directory:
print(content)