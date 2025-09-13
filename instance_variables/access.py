# we can access the instance variables Within the class by using self variable
# And outside of the class by using object reference variables

class Test:
    def __init__(self):
        self.a=10
        self.b=20

        print(self.a,self.b)
    def display(self):
        print(self.a,self.b)

t = Test()
t.display()
print(t.a,t.b)