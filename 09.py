import openpyxl as xl
import pathlib
import os

path = pathlib.Path('dir_name')

wb = xl.load_workbook('read_excel.xlsx')
ws = wb.active

'''
# Another way
for row in ws.iter_rows():
    for cell in row:
        print(cell.value)
'''

for row, file in zip(list(ws.columns)[0], path.iterdir()):
    os.rename(file, os.path.join(path, row.value) + '.jpg')
    print(file)
