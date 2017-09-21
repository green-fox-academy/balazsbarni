# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def star_add (text):
    if text == "":
        return ""
    else:
        return text[0]+ "*" + star_add(text[1:])


print(star_add("azexxxdc"))