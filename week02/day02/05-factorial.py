# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(number):
    if number == 0:
        return 1
    else:
        return number * factorio(number - 1)
    

print(factorio(5))
