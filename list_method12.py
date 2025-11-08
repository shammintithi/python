marks = [45.9, 45, 89.9, 34.7, 54.5]

#1. add value in list
marks.append(67)
print(marks)

#2. sort in list or ascending order
marks.sort()
print(marks)

#3. reverse sort in list or descending order
marks.sort(reverse=True)
print(marks)

#4. reverse in list based on previous output
marks.reverse()
print(marks)

#5. insert a new value in index --> marks.insert(index_, new value)
marks.insert(0, 100)
print(marks)

#6. remove a value
marks.remove(45) #marks.remove(element which i want to remove in data, not index number)
print(marks)

#7. pop a value
marks.pop(3) #marks.pop(index number)
print(marks)

#Note: Python documentation for more method and work 