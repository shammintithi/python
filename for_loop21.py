#1. for list values
"""list = [1, 2, 3, 4, 5]

#for name in(keyword) list
for element in list :
    print(element)"""

#2. for touple values
"""tup = (1, 2, 3, 4, 5, 6)
for value in tup :
    print(value)"""

#3. for string
"""str = "Print characters"
for char in str :
    print(char)
else :
    print("End")"""

#Practice
"""tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 25

i = 0
for value in tup :
    if(value == x) :
        print("Found x: " , i)
    i+=1"""
    
#4.range
"""seq = range(5)

for i in seq :
    print(i)

#another
for i in range(2, 7) :
    print(i)

for i in range(2, 15, 3) : #start, stop, step
    print(i)"""

#practice - times table
"""n = int(input("Enter the number: "))

for i in range(1,11) :
    print (n * i)"""

#Pass statement
for i in range(5) :
    pass
print("Hudai")

#factorial
"""n = 5
fact = 1

for i in range(1, n + 1) :
    fact *= i
    
print("Factorial: ", fact)"""

n = 5
sum = 0

for i in range(1, n + 1) :
    sum += i
print("Sum: ", sum)
