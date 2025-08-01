class Computer:

    # Example of a Class Variable
    Num_Of_Cpu = 1

    def __init__(self, name, capacity):
        print("Computer created")
        #Example of instance variables
        self.name = name
        self.capacity = capacity


    def config(self):
        print(f"Name: {self.name}, Capacity: {self.capacity}")

    def CompareCapacity(self, b):
        return True if self.capacity == b else False

comp1 = Computer("computer1", 10)
comp1.config()
comp2 = Computer("computer2", 10)
comp2.config()


compareCapacity = comp1.CompareCapacity(comp2.capacity)

if compareCapacity:
    print("SAME")
else:
    print("NOT SAME")
# print('Comp1:', comp1.name, comp1.capacity)
# print('Comp2:', comp2.name, comp2.capacity)

# Optional: using config method

