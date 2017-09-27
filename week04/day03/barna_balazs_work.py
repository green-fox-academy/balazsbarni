class My_Class(object):
    
    def get_apple(self):
        return "apple"


    def get_sum(self, list_to_sum):
        sum_of_list = 0
        for items in list_to_sum:
            sum_of_list += items
        return sum_of_list

    
    def is_anagram(self, first_sting, second_sring):
        letters_first = sorted(list(first_sting))
        letters_second = sorted(list(second_sring))
        return letters_first == letters_second


    def letter_counter(self, word):
        letters = {}
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        return letters


    def fibonacci (self, nth):
        if nth == 0  or nth == 1:
            return nth
        else:
            return self.fibonacci(nth-1) + self.fibonacci(nth-2)
        

