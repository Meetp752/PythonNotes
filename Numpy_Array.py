from numpy import *

arr = array([1,2,3,4])
print(arr.dtype)
print(arr)

#linespace By Default the steps are 50
arr2 = linspace(0,15, 16)
print(arr2.dtype)
print(arr2, ' Linspace' )

#arange
arr3 = arange(0,10,2)
print(arr3,' arange')

#coyping array same Location
arr4 = arr
print(arr4, 'copying array same Location')
print(id(arr4))
print(id(arr))

#Shallow Copy changing arr value will change arr5
#copying array different ID/Locations
arr5 = arr.view()
print(arr5, 'copying array different ID/Locations')
print(id(arr5))
print(id(arr))

#Deepcopy
#copying array different ID/Locations
arr6 = arr.copy()
print(arr6, 'copying array different ID/Locations and deepcopy')
print(id(arr6))
print(id(arr))

#2D array
arr2d = array([[1,2,3,4,5,6],[15,24,34,44,55,66]])
print(arr2d, ' Number of dimensions: ', arr2d.ndim)
print('Number of rows and columns ', arr2d.shape)
print(arr2d, ' Size: ', arr2d.size)

#converting from 2d to single dimension array
arrf = arr2d.flatten()
print('Flattened array: ', arrf)

#converting 2d to 3d array
arr3d = arrf.reshape(3,4)
print('Reshaped array: ', arr3d)
arr3d = arrf.reshape(2,2,3)
print('Reshaped array 3 values in 2 array in 2 array: ')
print(arr3d)

#converting 2d arr to matrix so we can perform calcuations
m = matrix(arr2d)
print('matrix: ')
print(m)

#matrix
mtest = matrix('1 2 3 ; 6 4 5 ; 6 7 6')
print('mtest: ')
print(mtest)
print('mtest diagonal: ')
print(diagonal(mtest))
print(mtest.max())






