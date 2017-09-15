given_number = input("Give the number, you want to check: ")



def length_of(lenght_of_a_number):
    return len(str(lenght_of_a_number))

#print(length_of(given_number))
    

def is_armstrong(number_to_check):
    armstrong_sum = 0
    for digit in map(int, str(number_to_check)):
        armstrong_sum += digit ** length_of(number_to_check)
    print(armstrong_sum)


is_armstrong(given_number) 

