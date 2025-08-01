# in python we dont have pass by reference or by value
def update(y):

    print(id(y))

    y = 8
    print('y in function: ', id(y))
    print(y)

# in python we dont have pass by reference or by value
def update2(lst):

    print(id(lst))

    lst[1] = 8
    print(id(lst))
    print(lst)


y = 10
print('y: ', id(y))
update(y)
print('y: ', id(y))



lst = [10, 23, 32, 32]
print(id(lst))
update2(lst)