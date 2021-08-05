import openpyxl as xl
workbook = xl.load_workbook("transactions.xlsx")
sheet1 = workbook['Sheet1']
cell1 = sheet1['a1']
sheet1.cell(1, 1)

print(sheet1.cell(1, 1))
print(cell1)
