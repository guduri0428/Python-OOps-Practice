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

# One more Example w.r.t the Student class

class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno  = rollno
        self.marks = marks
    
    def display(self):
        print("Student Name : {}\nRollno : {}\nMarks : {}".format(self.name,self.rollno,self.marks))

s1 = Student("Srinivasulu Guduri",542,82.9)
s1.display()
s2 = Student("Guduri Srinivasulu",542,82.9)
s2.display()