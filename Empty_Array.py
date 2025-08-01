from array import *

arr = array('i', [])
n = int(input('Enter the array size'))
for i in range(n):
    insert = int(input('Enter the number {}'.format(i+1)))
    arr.append(insert)

print(arr)

Search = int(input('Enter the number to be searched'))

k = 0
for e in arr:
    if e == Search:
        print("We found the number ", Search, " in the array")
        print(k)
        break
    k += 1
else:
    print("We did not find the number ", Search, " in the array")

# better way to print K
print(arr.index(Search))