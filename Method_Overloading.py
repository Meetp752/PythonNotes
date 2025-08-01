
class student:

    def __init__(self, mark1, mark2):
        self.mark1 = mark1
        self.mark2 = mark2

    #python dose not support functions wih same names Use the below strat
    def sum(self, a = None, b = None, c = None):

        s = 0

        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a

        return s

s1 = student(60, 90)

print(s1.sum(5))

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2))         # Output: 2
print(calc.add(2, 3))      # Output: 5
print(calc.add(2, 3, 4))   # Output: 9
