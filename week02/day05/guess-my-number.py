from random import randint
random_number = randint(0,100)
print(random_number)
nr_lifes = 5

for tries in range(nr_lifes):
    nr_lifes_in = int(nr_lifes)
    print(nr_lifes_in)
    user_guess = int(input("Enter guess: "))
    if nr_lifes - tries - 1 == 0: 
        print("Out of lives!")
    if user_guess == random_number:
        print("Congrats, you won!")
    elif user_guess < random_number:
        print("Too low. You have " , nr_lifes - tries - 1  , "lives left.")
    elif user_guess > random_number:
        print("Too high. You have " , nr_lifes - tries - 1  , "lives left.")  
 