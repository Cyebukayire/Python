import openpyxl as xl

workbook = xl.load_workbook("transactions.xlsx")
sheet1 = workbook['Sheet1']

# cell1 = sheet1['a1']
# cell1 = sheet1.cell(1, 23)
# print(cell1.value)

# print(sheet1.max_column)
# print(sheet1.max-row)

#  Print all the values
for row in range(2, sheet1.max_row + 1):
    col3 = sheet1.cell(row, 3).value
    correct_price = col3 * 0.9
    correct_price_cell = sheet1.cell(row, 4)
    correct_price_cell.value = correct_price

sheet1.cell(1, 4).value = "Correct Price"
workbook.save("transactions2.xlsx")

