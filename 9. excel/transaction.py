import openpyxl as xl
from openpyxl.chart import BarChart, Reference


def process(filename):
    workbook = xl.load_workbook(filename)
    sheet1 = workbook['Sheet1']

    for row in range(2, sheet1.max_row + 1):
        cell = sheet1.cell(row, 3)
        correct_price = cell.value * 0.9
        correct_price_cell = sheet1.cell(row, 4)
        correct_price_cell.value = correct_price
    sheet1.cell(1, 4).value = "Correct Price"

    values = Reference(sheet1,
                       min_row=2,
                       max_row=sheet1.max_row,
                       min_col=4,
                       max_col=4)

    chart = BarChart()
    chart.add_data(values)
    sheet1.add_chart(chart, 'e2')

    workbook.save(filename)


