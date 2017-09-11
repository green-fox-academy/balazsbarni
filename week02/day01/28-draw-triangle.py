# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

triangle_size = int(input("Give a number: "))
for i in range( 1, triangle_size + 1 ):
    print(( triangle_size - ( triangle_size - i )) * "*")