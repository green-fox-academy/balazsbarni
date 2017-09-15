given_number = int(input("Give the number, you want to check: "))

def is_armstrong(number_to_check):
    if number_to_check == armstrong_sum(number_to_check):
        print("It is an Armstrong number!")
    else:
        print("It is not an Armstrong number!")

def length_of(lenght_of_a_number):
    return len(str(lenght_of_a_number))

#print(length_of(given_number))
    

def armstrong_sum(number_to_check):
    armstrong_sum = 0
    for digit in map(int, str(number_to_check)):
        armstrong_sum += digit ** length_of(number_to_check)
    return armstrong_sum
    

is_armstrong(given_number) 

