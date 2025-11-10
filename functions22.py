#use "def" for define function
#1. 
def calc_sum(a,b): #parameters
    sum = a + b
    print(sum)

#call the function by using "function name(value/arguments)
calc_sum(5,10)
calc_sum(5,15)
calc_sum(10,24)

#2.

def calc_sum (a,b): 
    return a + b

sum = calc_sum(10,24) #function call
sum = calc_sum(10,456)
print(sum)

#3. 
def print_hello(): #without parameters
    print("Tithi")

print_hello()
print_hello()
print_hello()

#Q. average of 3 numbers

def calc_avg(a, b, c):
    sum = (a + b + c) 
    avg = sum / 3
    print(avg)

calc_avg (2,3,4)
calc_avg (1,1,1)
calc_avg (5,23,52)

#Q. print factorial number using function

def calc_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)

calc_fact(7)

#even or add
def calc_even(x):
    if (x % 2 == 0):
        print("even")

    else:
        print("odd")

calc_even(2)
calc_even(79)