# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def power_to_n(n,num):
    if n == 1:
        return num
    else:
        return num * power_to_n(n-1, num)

print(power_to_n(3,3))