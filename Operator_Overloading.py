
class Student:
    def __init__(self, mark1, mark2):
        self.mark1 = mark1
        self.mark2 = mark2

    def __add__(self, other):
        m1 = self.mark1 + other.mark1
        m2 = self.mark2 + other.mark2
        s3 = Student(m1, m2)
        return s3

    #greater then
    def __gt__(self, other):
        r1 = self.mark1 + self.mark2
        r2 = other.mark2 + other.mark2
        if r1 > r2:
            return True
        elif r1 < r2:
            return False

    def __str__(self):
        return '{} {}'.format(self.mark1, self.mark2)
        # f'{self.mark1} {self.mark2}'

s1 = Student(60, 90)
s2 = Student(90, 94)

s3 = s1 + s2

print(s3.mark1)
print(s3.mark2)

if s1 > s2:
    print("s1 Wins")
else:
    print("s2 Wins")

print(s1)
print(s2)