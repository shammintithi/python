#. Nested dictionary

student = {
    "name" : "Tithi",
    "subjects" : {
        "phy" : 95,
        "math" : 96,
        "eng" : 97
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["math"])