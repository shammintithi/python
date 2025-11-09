#1. Dictionary
dict = {
    "Key" : "value",
    "name" : "tithi",
    "age" : 30,
    "info" : ("tithi", 21, "SEU"),
    "fruits" : ["mango", "banana", "orange"],
    "is_valid" : True,
    12.99 : "price"
}

print(dict)
print(dict["age"]) #for diffferent values
print(dict["is_valid"])

#another: will overwrite the previous value of "name"

dict["name"] = "Shammin"
dict["surname"] = "Akter"
print(dict["name"])
#print(dict)

#2. Null dictionary
null_dict = {}

#Also we can add some values in null dictionary

null_dict["name"] = "Shammin"
print(null_dict)
