marks = [45.9, 45, 89.9, 34.7, 54.5]
print(marks)
print(type(marks)) #print the type of data
print(len(marks)) #print the length of the data
print(marks[0])
print(marks[3])

#2.can change STRING value in LIST, BUT can  not change string value in nomally
students = ["Tithi", 21, 79.9, "Dhaka"]
print(students)
students[3] = "Moghbazar"
print(students)

## List Slicing
print(marks[1:4]) #from index 1 to index 3
print(marks[:3]) #from starting to index 2
print(marks[2:]) #from index 2 to end
print(marks[-4:-1]) #from index -4 to index -2
print(marks[-3:]) #from index -3 to end
print(marks[:-2]) #from starting to index -3

##length of LIST
print(len(students))