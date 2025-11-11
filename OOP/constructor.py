class Student:
#default Constructor
    """def __init__(self):
        print("default constructor")"""
    
    Name_of_University = "University"
#parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        #print("Information")

s1 = Student("tithi", 80) 
print(s1.name)
print(s1.marks)
print(s1.Name_of_University )
s2 = Student("shammin", 90)
print(s2.name, s2.marks, s2.Name_of_University)
 