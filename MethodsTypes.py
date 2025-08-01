
class Student:

    school = "naci"

    #constructor
    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    # Instance method
    def average(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    # Instance method (Accessor Methods)
    def get_m1(self):
        return self.mark1

    # Instance method (Mutator Methods)
    def set_m1(self, value):
        self.mark1 = value

    @classmethod
    def Info(cls):
        return cls.school

    @staticmethod
    def Info2():
        print("This is a static method")



s1 = Student(1,2,3)
s2 = Student(2,2,2)
print(s1.average())

print(Student.Info())
print(Student.Info2())