# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def bunny_ear_counter(num, ear):
    if num == 1:
        return ear
    else:
        return ear + bunny_ear_counter(num-1,ear)

print(bunny_ear_counter(8, 2))