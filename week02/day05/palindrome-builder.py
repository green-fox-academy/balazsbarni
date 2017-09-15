to_palindrome_word = input("Enter the word: ")


def build_palindrome(entered_word):
    print(entered_word, entered_word[::-1] , sep='')

build_palindrome(to_palindrome_word)