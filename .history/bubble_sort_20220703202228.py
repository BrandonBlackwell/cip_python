# Bubble Sort Algo
# Start with first item and compare to second item
# If item is larger than second item, switch items
# Repeat process until the end of list is reached.
# Now start process again and compare 
# until 1-end of list is reached

my_list = [6,3,7,5,4,1,2]
#               i
#     j 
for i in range(len(my_list)-1,0,-1):
    for j in range(i):
        if my_list[j] > my_list[j+1]:
            temp_var = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = temp_var