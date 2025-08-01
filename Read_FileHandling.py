
f = open("files/MyData", 'r')


#print(f.read())                # this will print the complete File
print(f.readline(), end='')     # only Prints the first line
print(f.readline())             # it will print the second line
print(f.readline(3))            # it will only print the first 3 characters
