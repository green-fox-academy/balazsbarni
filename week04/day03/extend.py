# Adds a and b, returns as result
def add(a, b):
    return a + b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

# Returns the median value of a list given as param
def median(pool):
    sorted_pool = sorted(pool)
    n = len(sorted_pool)
    if n % 2 == 1:
        return sorted_pool[n // 2]
    else:
        i = n // 2
        return (sorted_pool[i - 1] + sorted_pool[i]) / 2

# Returns true if the param is a vovel
def is_vovel(char):
    vovel_list = list('aeiouéáőúűöüóí')
    return char.lower() in vovel_list

# Create a method that translates hungarian into the teve language
def translate(teve):
    to_translate = []
    for char in teve:
        if is_vovel(char):
            to_translate.append(char+"v"+char)
        else:
            to_translate.append(char)
    return "".join(to_translate)


