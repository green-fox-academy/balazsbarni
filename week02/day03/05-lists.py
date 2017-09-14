# Check if the list contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

numbers = [1, 2, 3, 4, 5, 6, 8]

for i in numbers:
    cont = 0
    if i == 7:
        cont += 1
        break
    else:
        cont += 0     
if cont == 1:
    print("Hooorray")
else:
    print("Noooooo")


    
