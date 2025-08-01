
class PyCharm:
    def execute(self):
        print("Compilling")
        print("Running")

class Myeditor:

    def execute(self):

        print("Spelling checking")
        print("Executing")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()

ide = Myeditor()
#ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)