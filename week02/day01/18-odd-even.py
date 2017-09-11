# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.

x = float(input("Number: "))
if x % 2 == 0:
    print("It is even!")
else:
    print("It is odd!")