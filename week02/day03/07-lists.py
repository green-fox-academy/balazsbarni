# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.
# "What I cannot create, I do not understand"
#correct = ["What" , "I" , "cannot" , "create" , "I" , "do" , "not" , "understand"]

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]



i1 = words.index("do")
i2 = words.index("cannot")
words[i1] , words[i2] = words[i2] , words[i1]
words_correct = ' '.join(words)
print(words_correct)