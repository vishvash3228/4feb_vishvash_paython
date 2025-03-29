class Grandparent:
    def func1(self):
        print("This is Python.")

class Parent(Grandparent):
    def func2(self):
        print("This is Java")

class Child(Parent):
    def func3(self):
        print("This is HTML")

obj = Child()
obj.func1()  
obj.func2()  
obj.func3()
