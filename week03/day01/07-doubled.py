# Create a method that decrypts the duplicated-chars.txt
double_file = ("doubled.txt")

def decrypt(file_name):
    with open(file_name , "r") as f:
        decoded = ""
        for letters in f.read()[::2]:
            decoded += letters
        print(decoded)

decrypt(double_file)


