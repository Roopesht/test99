def get_names():
    l1 = ['Sameera', 'Nidhi', 'Vishnavi']
    return l1

f=open("names.txt", "w")
names = get_names()
names = [name + '.\n' for name in names]

f.writelines(names)
f.close()

f= open("names.txt", "r")
s = f.read()
print ("The contents are:\n",s)
f.close()



