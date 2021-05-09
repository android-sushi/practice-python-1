import os

dir_name = 'foo'
path = dir_name + '/'
file_names = os.listdir(path)
file_name_head = dir_name + '-'

cnt = 0
target_range = 1
file_name_cnt = 1

for file_name in file_names:
    new_file_name = file_name_head + str(target_range) + ' (' + str(file_name_cnt) + ').jpg'
    print(new_file_name)
    os.rename(path + file_name, path + new_file_name)
    cnt += 1
    file_name_cnt += 1
    if cnt % 10 == 0:
        target_range += 1
        file_name_cnt = 1
