student = {
    "name" : "Tithi",
    "subjects" : {
        "phy" : 95,
        "math" : 96,
        "eng" : 97
    } 
}
"""
#1. use  method.keys()

print(student.keys())
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))"""

#2. use method.values()
"""print(student.values())
print(list(student.values())) #convert to list"""

#3. use method.items()
"""print(student.items()) 
print(list(student.items()))"""


#4. use method.get()
"""print(student.get("name"))
print(student.get(name4))"""

#5. use method.update()
"""student.update({"City" : "Dhaka"})
print(student)
#Another
new_dict = {"City" : "Dhaka", "age" : "5"}
student.update(new_dict)
print(student)"""

