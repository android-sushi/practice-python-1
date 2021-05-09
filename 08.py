import csv
import os

with open('data_set.txt', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for rows in reader:
        dir_name = rows[0]
        os.mkdir(dir_name)
        print(dir_name)
