import shutil
import pathlib
import re
import cv2
import os

path_list = {1: '1', 11: '11', 2: '1', 22: '22', 3: '3', 33: '33', 4: '4', 44: '44',
             5: '5', 55: '55', 6: '6', 66: '66', 7: '7', 77: '77', 8: '8', 88: '88', 9: '9'
             }


def mkdir():
    print('do you want to create folders? y/n: ')
    while True:
        yn = input()
        if yn == 'y':
            for value in path_list.values():
                os.mkdir(value)
            break
        elif yn == 'n':
            break
        else:
            print('enter y or n')


def sort_photos():
    print('begin')
    path = pathlib.Path('./')
    file_list = [p for p in path.iterdir() if re.search('.jpg|.JPG', str(p))]

    try:
        for file_name in file_list:
            os.system('cls')
            print(file_name)
            img = cv2.imread(file_name.name)
            img_resize = cv2.resize(img, dsize=(500, 400))
            cv2.imshow(file_name.name, img_resize)
            cv2.moveWindow(file_name.name, 100, 200)
            cv2.waitKey(400)
            cv2.destroyAllWindows()
            while True:
                switch_num = int(input())
                if switch_num not in path_list.keys():
                    print('enter the correct number')
                else:
                    dir_path = pathlib.Path(path_list[switch_num]) / file_name
                    shutil.move(file_name, dir_path)
                    break
    except KeyboardInterrupt:
        print('finished')


def main():
    mkdir()
    sort_photos()


if __name__ == '__main__':
    main()
