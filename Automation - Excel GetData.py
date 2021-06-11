import openpyxl
from openpyxl import cell

excel_values = ['C:/Users/Justin/Documents/GitHub/python-public/Data/SampleData.xlsx', 'C:/Users/Justin/Documents/GitHub/python-public/Data/SampleData2.xlsx']
values = []

for file in excel_values:
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['SalesOrders']
    cell_value = worksheet['G11'].value
    values.append(cell_value)

print(values)