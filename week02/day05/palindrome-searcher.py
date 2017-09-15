to_palindrome_search = input("Enter the sentence: ")
to_palindrome_search_back = to_palindrome_search[::-1]

print(to_palindrome_search)
print(to_palindrome_search_back)

list_palindrome = list(to_palindrome_search)
list_palindrome_back = list(to_palindrome_search_back)

print(list_palindrome)
print(list_palindrome_back)

def search_palindrome(list_palindrome):
    for pos in (1,int(len(list_palindrome))):
        palindromes = ""
        for next_to in list_palindrome:
            if next_to[pos-1] == next_to[pos+1]:
                palindromes = (nex_to[pos-1] + nex_to[pos] + nex_to[pos+1])
        print(palindromes)

#search_palindrome(list_palindrome)