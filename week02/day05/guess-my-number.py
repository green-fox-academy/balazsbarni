from random import randint

lifes_nr = int(input("Enter how many tries you want: "))
range_nr = int(input("Enter range: "))
random_number = randint(0,range_nr)
#print(random_number)

def guessing_game(number_of_lifes, random_nr):
    for tries in range(number_of_lifes):
        nr_lifes_in = int(number_of_lifes - tries)
        #print(nr_lifes_in)
        user_guess = int(input("Enter guess: "))
        if nr_lifes_in - 1 == 0: 
            print("Out of lives!")
            break
        elif user_guess == random_nr:
            print("Congrats, you won!")
            break
        elif user_guess < random_nr:
            print("Too low. You have " , nr_lifes_in - 1 , "lives left.")
            nr_lifes_in -= 1
        elif user_guess > random_nr:
            print("Too high. You have " , nr_lifes_in - 1  , "lives left.")
            nr_lifes_in -= 1
        
 
guessing_game(lifes_nr , random_number)