first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")


def check_if_anagram(first_input, second_input):
    word_list_first = sorted(list(first_input))
    word_list_second = sorted(list(second_input))
    if word_list_first == word_list_second:
        return True
    else:
        return False
    

print(check_if_anagram(first_word, second_word))