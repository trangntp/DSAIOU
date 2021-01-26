input_str =input("Nhap vao so dong va so cot cua mang  2 chieu: ")
row_colum = [int(x) for x in input_str.split(',')]
row = row_colum[0]
colum = row_colum[1]
multi_array = [[0 for c in range(colum)] for r in range(row)]
for r in range(row):
    for c in range(colum):
        multi_array[r][c] = r*c
print("Day la man 2 chieu cua ban: ")
for r in range(row):
    print(multi_array[r])