# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy_file():
    try:
        first = open("first.txt" , "a")
        second = open("second.txt" , "r")
        first.writelines(second.readlines())
        return True
    except Exception:
        return False

print(str(copy_file()))