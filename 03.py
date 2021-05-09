import os
from datetime import datetime

path = 'dir_name'
dir_names = os.listdir(path)
truth_quantity = 100
quantity_total = 0
quantity = 0
quantity_dup = 0
number_cat_list = []
number_list = []
number_dup_list = []

with open('output.txt', 'w', encoding='utf-8') as f:
    for dir_name in dir_names:
        number_cat_list = []
        name_list = dir_name.split('_')
        day = datetime.strptime('20' + name_list[0], '%Y%m%d').strftime('%Y/%m/%d')
        quantity = name_list[1]
        number = name_list[2]
        location = name_list[3]
        product = name_list[4]
        contents = name_list[5]
        number_no = number.split(',')

        for number_dup in number_no:
            if number_dup in number_list and number_dup != 'xxxx':
                quantity_dup += 1
                day_number = str(day) + ':' + str(number_dup)
                number_dup_list.append(day_number)
                number_cat = '(' + str(number_dup) + ')'
                number_cat_list.append(number_cat)
            else:
                quantity += 1
                number_list.append(number_dup)
                number_cat_list.append(number_dup)
            quantity_total += 1

        f.write(day)
        f.write('\t')
        f.write(quantity)
        f.write('\t')
        f.write(','.join(number_cat_list))
        f.write('\t')
        f.write(location)
        f.write('\t')
        f.write(product)
        f.write('\t')
        f.write(contents)
        f.write('\n')

print(truth_quantity)
print(quantity_total)
print(quantity)
print(quantity_dup)
print(truth_quantity - quantity)
print(','.join(number_list))
for num in number_dup_list:
    print(num)
