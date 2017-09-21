# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.


def x_to_y_changer (text):
    if text == "":
        return ""
    elif text[0] == "x":
        return "y" + x_to_y_changer(text[1:])
    else:
        return text[0] + x_to_y_changer(text[1:])


print(x_to_y_changer("azexxxdc"))