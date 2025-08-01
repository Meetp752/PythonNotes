from functools import reduce

nums = [3,4,2,6,8,9,2,7]

#lambda is like a mini function
#Filters all the values
evens = list(filter(lambda x: x % 2 == 0, nums))

# we want to update/change value so we use map
double = list(map(lambda x: x * 2, nums))

print(double)
sub= reduce(lambda x, y: x - y, double)
print(sub)