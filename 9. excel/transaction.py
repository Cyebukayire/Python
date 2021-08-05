import openpyxl as xl
workbook = xl.load_workbook("transactions.xlsx")
sheet1 = workbook['Sheet1']

# cell1 = sheet1['a1']
# cell1 = sheet1.cell(1, 23)
# print(cell1.value)

#  Print all the values
row = 1
col = 1
while sheet1.cell(row, col):
    print(sheet1.cell(row, col))
    row += 1
    col += 1
