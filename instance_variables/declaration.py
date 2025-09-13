# Where we declare instance variables
# 1. Inside Constructor by using self variable.
# 2. Inside Instance Method by using self variable.
# 3. Outside of the class by using object reference variable.

print("# 1.Inside constructor by using self variable")

class Employee:
    def __init__(self):
        self.eno = 100
        self.ename = 'Srinivasulu'
        self.esal = 1000
    
e = Employee()
print(e.__dict__) # object_reference.__dict__ attribute gives the dictionary of instance variable w.r.t object

print('# 2.Inside Instance by using self variable.')

class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)

print('# 3.Outside of class by using Object Reference variable.')

class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
t.d=40
print(t.__dict__)
