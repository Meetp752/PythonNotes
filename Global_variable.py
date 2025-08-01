a = 10
print('*** Id Of global Variable: ' ,id(a))
print('Value of variable: ', a)

def dosomthing():
    print('*** changed in function: ', id(a))
    x = globals()['a']
    print('X global ID in function: ', id(x))
    print('X global valuse in fucntion: ', x)
    globals()['a'] = 1
    print('*** changed in function: ', id(a))
    print('changed in function: ',a)




dosomthing()
print('outside function final: ', id(a))
print('outside function final: ', a)