# Programme to Demonstrate the constructor will execute only once per Object.

class TestConstructor:
    def __init__(self):
        print("Constructor Execution...!")
    
    def m1(self):
        print("Method Execution...!")

t1 = TestConstructor()
t2 = TestConstructor()
t3 = TestConstructor()
t1.m1()