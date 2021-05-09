import openpyxl as xl

wb = xl.Workbook()
sheet = wb.active

row = 1
list_rows = ('A', 'B', 'C', 'D')
list_columns = [range(1, 5), range(1, 6), range(1, 6), range(1, 8)]
list_range = range(1, 21)

for rows, columns in zip(list_rows, list_columns):
    for num in columns:
        for range_num in list_range:
            sheet['A' + str(row)].value = rows
            sheet['B' + str(row)].value = str(num)
            sheet['C' + str(row)].value = range_num
            sheet['D' + str(row)].value = "".join(['=A', str(row), '&B', str(row), '&C', str(row)])
            write_str = '-'.join([rows, (str(num)), str(range_num)])
            print(write_str)
            row += 1

wb.save('output.xlsx')
