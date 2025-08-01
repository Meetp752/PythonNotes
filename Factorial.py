
def factorial(n):

    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


x = 4
result = factorial(x)
print(result)

def factREC(n):

    if(n==0):
        return 1

    return n * factREC(n - 1)


result2 = factREC(5)
print(result2)