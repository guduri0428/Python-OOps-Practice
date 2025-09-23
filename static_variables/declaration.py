# If the Value of the variable is not varied from object to object, such type of variables
# we have to declare within the class directly but out side of any methods.
# Such type of variables are called Static variables.

# For total class only one copy of static variables will be created and shared by all objects of the class.

# We we access static variables either by using class name or by using object reference. But recommended 
# to use the class name.

# Note -1
# In case of instance variables for every object a separate copy will be created, But in case of
# static variables for total class only one copy will be created and shaerd by every object of that class.

# Example programme

class Test:
    x = 10
    def __init__(self):
        self.y = 20

t1 = Test()
t2 = Test()

print(t1.x,t1.y)
print(t2.x,t2.y)

Test.x = 888
t1.y = 999

print(t1.x,t1.y)
print(t2.x,t2.y)