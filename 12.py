import os
import pathlib
import re


def rename_photos():
    path = pathlib.Path('./')
    file_list = [p for p in path.iterdir() if re.search('.jpg|.JPG', str(p))]

    pattern_list = {
        '１': 'Pattern_A',
        '２': 'Pattern_B',
        '３': 'Pattern_C',
        '４': 'Pattern_D'
    }

    try:
        os.system('cls')
        print('enter a group')
        group = input()

        for file_name in file_list:
            os.system('cls')
            print('group：' + str(group))
            print('target file：' + str(file_name))
            print('\n' + 'enter the layers')
            layer = input()

            while True:
                print('\n' + 'enter a number (double-byte character)' + '\n',
                      'Pattern_A：１　Pattern_B：２　Pattern_C：３　Pattern_D：４')
                pattern = input()
                if pattern in ['１', '２', '３', '４']:
                    break
                else:
                    print('enter the correct information')

            new_file_name_list = [group, layer, pattern_list[pattern]]
            new_file_name = '　'.join(new_file_name_list) + '.jpg'

            i = 0
            while True:
                if os.path.exists(new_file_name):
                    i += 1
                    new_file_name = '　'.join(new_file_name_list) + str(i) + '.jpg'
                else:
                    break

            os.rename(file_name, new_file_name)

    except KeyboardInterrupt:
        print('finished')


def main():
    rename_photos()


if __name__ == '__main__':
    main()
