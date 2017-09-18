# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0
number_to = input("Give me a number: ")

def divider_by_ten(number_to_divide):
    try:
       print(10 / int(number_to_divide))
    except ZeroDivisionError:
       print("Fail")

divider_by_ten(number_to)