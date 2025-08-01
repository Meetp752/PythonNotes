
#print the number of fib passed to function
def fib(n):
    a, b = 0, 1

    if n <= 0:
        print("Negative number or Zero")
        return 0

    if n == 1:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2,n):

            temp = a + b
            a = b
            b = temp
            print(temp)

#fib(0)

def fib2(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return

    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


fib2(100)
