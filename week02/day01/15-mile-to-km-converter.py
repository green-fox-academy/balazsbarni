# Write a program that asks for an integer that is a distance in kilometers,
# then it converts that value to miles and prints it

print("How many kilometers do you want to convert?")
converter = 0.621371192
km = float(input ('Km:'))
km *=converter
print("It is " , km , "miles!")