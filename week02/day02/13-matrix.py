# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

def list_matrix (widht, height):
    height_list = []
    for i in range(widht):
        widht_list = []
        for j in range(height):
            if j == i:
                widht_list.append ("1")
            else:
                widht_list.append ("0")    
        height_list.append (widht_list)
    return height_list

def row_matrix (list_matrix):
    for row in list_matrix:
        print (row)

row_matrix(list_matrix(4,4))
