# Write a recursive function that takes one parameter: n and counts down from n.

def count_down (num):
    print(num)
    if num == 1:
        return num
    else:
        return count_down(num-1)

print(count_down(10))