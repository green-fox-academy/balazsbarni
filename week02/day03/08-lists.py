# Create a simple calculator application which does read the parameters from the prompt 
# and prints the result to the prompt. 

# It should support the following operations: 
# +, -, *, /, % and it should support two operands. 

# The format of the expressions must be: {operation} {operand} {operand}. 
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

operation, num1, num2 = input("Adatok: ").split(" ")
number1 = int(num1)
number2 = int(num2)

def calculator(number1, number2, operation):
    if operation == '+':
        print(number1, operation, number2, '=', number1 + number2)
    elif operation == '-':
        print(number1, operation, number2, '=', number1 - number2)
    elif operation == '*':
        print(number1, operation, number2, '=', number1 * number2)
    elif operation == '/':
        print(number1, operation, number2, '=', number1 / number2)
   

print(calculator(number1, number2, operation))