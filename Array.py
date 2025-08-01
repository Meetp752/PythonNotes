from array import *

vals = array('i', [5,9,8,4])
char = array('u',['a','b','c','d','e','f'])

#copying arry and type into new array
newArr = array(vals.typecode, (a*a for a in vals))

vals.reverse()
print(vals)
print('Array Info: ',vals.buffer_info())

for j in vals:
    print(j)

for j in newArr:
    print(j)

for j in char:
    print(j)






