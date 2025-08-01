class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.Laptop = None  # Placeholder to store Laptop instance

    def show(self):
        print(self.name, self.rollno)
        if self.Laptop:
            self.Laptop.show()
        else:
            print("No laptop assigned.")

    class Laptop:

        def __init__(self, brand, CPU):
            self.brand = brand
            self.CPU = CPU

        def show(self):
            print(self.brand, self.CPU)


# Create student objects with only name and roll number
s1 = Student("Meet", 1)
s2 = Student("Jeet", 2)

# Assign Laptop instances manually using Student.Laptop
s1.Laptop = Student.Laptop('hp', 3)


# Show student and laptop details
s1.show()
s2.show()
