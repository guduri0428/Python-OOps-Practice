# Within a class we can delete instance as follows
# del self.variableName

# From outside of class we can delete instance variables as follows
# def objectreference.variableName

class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40

    def m1(self):
        del self.d

t = Test()
print(t.__dict__)

t.m1()
print(t.__dict__)

del t.c
print(t.__dict__)


# The instance variables which are deleted from one object, will not be deleted from other objects.

class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40

t1 = Test()
t2 = Test()

print(t1.__dict__)
print(t2.__dict__)

del t1.d

print(t1.__dict__)
print(t2.__dict__)

print("""If change the values of instance variables of one object then
      then those chages won't be reflected to the remaining objects because for every
      object a separate copy of instance variables are available""")

