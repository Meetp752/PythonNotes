#Position, Keyword, default
def person(name, age = 18): #age = 18 is default value if not passed
    print('Name: ',name,'age: ', age)

person(name='meet') #if you dont know the Position you can set keyword


# *args (one *) collects extra positional arguments as a tuple.
# **kwargs (two **) collects extra keyword arguments as a dictionary
def person2(name2, **data2):
    print(name2)
    for i,j in data2.items():
        print(i,j)

person2('meet', age = 23, city = 'Chicago', mob = 12342)


# variable length (b is a tuple)
def sum(a,*b):
    c = a

    for i in b:
        c = c  + i

    print(c)

sum(1,2,3,4)