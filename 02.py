from pathlib import Path
import csv

path = Path('analyzing_list')
file_names = list(path.glob('*'))
analyzing_list = []
large_sum = 0
small_sum = 0

for file_name in file_names:
    large = 0
    small = 0
    with open(file_name, encoding='utf-8') as f:
        row = csv.reader(f)
        for col in row:
            if col[1] == 'l':
                large += int(col[2])
            elif col[1] == 's':
                small += int(col[2])
        analyzing_list.append([file_name.stem, large, small])

for row in analyzing_list:
    large_sum = large_sum + row[1]
    small_sum = small_sum + row[2]

print(len(analyzing_list))

for row in analyzing_list:
    print(row[0], row[1], row[2], sep='\t')

print()
print(large_sum)
print(small_sum)
