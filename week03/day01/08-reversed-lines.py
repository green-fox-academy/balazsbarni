# Create a method that decrypts reversed-lines.txt
reversed_file = ("reversed.txt")

def decrypt(file_name):
    with open(file_name , "r") as f:
        decoded = ""
        for letters in f.read()[::-1]:
            decoded += letters
        print(decoded)

decrypt(reversed_file)