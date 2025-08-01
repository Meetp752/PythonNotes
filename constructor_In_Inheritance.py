
class a:

    def __init__(self):
        print("constructor A")

    def feature1(self):
        print("Feature 1 A")

    def feature2(self):
        print("Feature2")

class b:

    def __init__(self):

        #this calles the super class of b which is a
        super().__init__()
        print("constructor B")

    def feature1(self):
        print("Feature 1 B")

    def feature4(self):
        print("Feature4")

class c(a,b):

    def __init__(self):
        super().__init__()
        print("constructor C")

c1 = c()
c1.feature1()

