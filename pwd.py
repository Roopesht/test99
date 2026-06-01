import os
current_dir = os.getcwd()
print("Current directory:", current_dir)

file = open ("abc/test1.txt", "r")
print (file.read())
file.close()

os.makedirs('abc/ram')

