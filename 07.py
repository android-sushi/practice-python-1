import os

path = 'dir_name'
dir_names = os.listdir(path)

for dir_name in dir_names:
    cd_path = dir_name
    print(dir_name)

    sub_path = path + '/' + dir_name
    sub_dir_names = os.listdir(sub_path)
    print(sub_dir_names)

    if sub_dir_names:
        dir_name = sub_dir_names[0]
        new_sub_dir_path = path + '/' + dir_name
        os.rename(sub_path, new_sub_dir_path)
    else:
        continue
