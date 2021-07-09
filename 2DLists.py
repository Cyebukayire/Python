matrix =[
    [1, 2, 3],
    [4, 5, 6],
    ["A", "B", "C", 3242],
    ["D", "E", "F"]
]

for row in matrix:
    print (row)

for row in matrix:
    for item in row:
        print (item)

print(matrix[2][3])

