row_input = int(input("enter the number of rows :"))
col_input = int(input("enter column input :"))

multi_list = [[0 for col in range(col_input)] for row in range(row_input)]
for row in range(row_input):
    for col in range(col_input):
        multi_list[row][col]= row*col
print(multi_list)