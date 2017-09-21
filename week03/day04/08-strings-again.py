# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def x_remover (text):
    if text == "":
        return ""
    elif text[0] == "x":
        return x_remover(text[1:])
    else:
        return text[0] + x_remover(text[1:])


print(x_remover("azexxxdc"))