class Parent:
    def show(self):
        print("This is Python")

class Child(Parent):
    def display(self):
        print("This is Java")

obj = Child()
obj.show()   
obj.display()
