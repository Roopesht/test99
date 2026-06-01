
howmany=0
apples = 20

import age
print (age.calculate_age ("2004-01-14"))

from age import calculate_age, func1
print (calculate_age ("2004-01-14"))

func1()

from large_functions import Func1
Func1()

import age as age_functions
print (age_functions.calculate_age ("2004-01-14"))

if howmany == 0:
    print ("You cannot have 0 as number of people")
    
try:
    print (f"each person gets {apples/howmany} apples")
except TypeError as e:
    print ("Make sure all are numbers")
except Exception as e:
    print ("Something worng, cannot calculate")


