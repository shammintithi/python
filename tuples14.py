marks = (45.9, 45, 89.9, 34.7, 54.5,34.7)
print(marks[0]) #for tuple we can print value by assigning the index number--> print (marks[0])

#single value tuple
tup = (1,) #single comma cz the value will count the number in integers not for tuple
print(tup)
#Note: same for multiple values tuple 

#sub_tuple
print(marks[1 : 4])


#Methods
print(marks.index(34.7)) #it is use for find out the values of index number

print(marks.count(34.7)) 
