# Write a program that asks for two numbers
# Thw first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people

x = float(input("Girls: "))
y = float(input("Boys: "))

if x + y > 20 and x / y == 1:
    print("The party is exellent!")
elif x + y > 20 and x < y:
    print("Quite cool party!")
elif x + y < 20 and x > 0:
    print("Average party...")
elif x == 0:
    print("Sausage party") 