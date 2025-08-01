
class a:

    def feature1(self):
        print("Feature1")

    def feature2(self):
        print("Feature2")

class b():

    def feature3(self):
        print("Feature3")

    def feature4(self):
        print("Feature4")

class c(a,b):
    def feature5(self):
        print("Feature5")
a1 = a()
b1 = b()

a1.feature1()
a1.feature2()

#i can call f1 using class b
c1 = c()
c1.feature1()