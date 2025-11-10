#1. iteration
"""count = 1

while count <= 5 :
    print("Hello world!")
    count += 1

    print(count)

i = 2
while i < count :
    print("Iteration",i)
    i+=1
    print(i)"""

#2. Print index
"""nums = [1,3,4,56,34,7,24,67]
fruits = ["apple", "orange", "grape", "avocado", "strawberry"]

idx = 0
while idx < len(nums):
    print("Index:", idx)
    print(nums[idx])
    idx += 1

index = 0
while index < len(fruits):
    print(fruits[index])
    index += 2"""

#3. find the index of the value
"""nums = [1, 3, 4, 56, 34, 7, 24, 67]

x = 56

i = 0
while i < len(nums) :
    if(nums[i] == x):
        print("Found the index of x: ",i)
        break
    else :
        print("Not found it")
    i += 1"""

#4. break
"""i = 0
while i <= 8:
    print(i)
    if(i == 4):
        break
    i += 1
print("End of loop")"""

#5. continue
"""i = 0
while i <= 8:
    if(i == 4):
        i +=1
        continue
    print("will continue",i)
    i += 1"""

#For odd number
"""i = 0
while i <= 8:
    if(i % 2 == 0):
        i +=1
        continue
    print(i)
    i += 1"""

#For even number
i = 0
while i <= 8:
    if(i % 2 != 0):
        i +=1
        continue
    print(i)
    i += 1