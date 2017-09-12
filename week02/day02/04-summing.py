# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum (*numbers):
    total = 0
    for i in numbers:
            total += i
    print ("The numbers sum is: " , total)

sum(2,3,4)
