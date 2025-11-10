#recursion
#1.
def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)

show(5)

#factorial recursion
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    
    return factorial(n-1) * n

print(factorial(8))

#print the value of the sum and calculate the sum

def calc_sum(n):
    if(n == 0):
        return 0 
    print(n)
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)