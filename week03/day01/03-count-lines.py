# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.
my_file = ("file-name.txt")


def line_counter(name_of_the_file):
    try:
        num_lines = 0
        lc = open(my_file, "r")
        for lines in lc:
            num_lines += 1
        print(num_lines)
    except IOError:
        print(0)

line_counter(my_file)

 