import openpyxl as xl
import csv


def read_text():
    text_list_5 = []
    text_list_4 = []
    text_list_x = []

    with open('output.txt', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for rows in reader:
            row = rows[2].rstrip().split(',')
            for txt_num in row:
                if txt_num == 'xxxx':
                    text_list_x.append(str(txt_num))
                elif len(txt_num) == 5:
                    text_list_5.append(str(txt_num))
                else:
                    text_list_4.append(str(txt_num))

    text_list = text_list_5 + text_list_4 + text_list_x

    return text_list


def read_xlsx():
    xlsx_list = []
    data_wb = xl.load_workbook('read_excel.xlsx')
    data_ws = data_wb.active

    for row in list(data_ws.columns)[0]:
        xlsx_num = str(row.value)
        xlsx_list.append(xlsx_num)

    return xlsx_list


def match_num(xlsx_num, text_num):
    if text_num == xlsx_num[-5:]:
        return 1
    elif text_num == xlsx_num[-4:]:
        return 1
    elif text_num == 'xxxx':
        return 2
    else:
        return 0


def main():
    data_list = []
    matching_cnt = 0
    unknown_cnt = 0

    text_list = read_text()
    text_list_len = len(text_list)

    xlsx_list = read_xlsx()
    xlsx_len = len(xlsx_list)

    for xlsx_num in xlsx_list:
        return_num = 0
        for text_num in text_list:
            return_num = match_num(xlsx_num, text_num)
            if return_num == 1:
                text_list.remove(text_num)
                matching_cnt += 1
                break
            elif return_num == 2:
                text_list.remove(text_num)
                matching_cnt += 1
                unknown_cnt += 1
                break

        data_list.append([xlsx_num, return_num])

    text_miss_len = len(text_list)

    print('result')
    print('not matching')
    not_matching = 0
    for row in data_list:
        if row[1] == 0:
            not_matching += 1
            print(row[0])
    print('test list')
    for row in text_list:
        print(row)
    print('xlsx len', xlsx_len, '　', 'not matching', not_matching)
    print('test list len', text_list_len, '　', 'matching cnt', matching_cnt, '　', 'unknown cnt', unknown_cnt, '　',
          'text miss len', text_miss_len)
    print('difference', xlsx_len - text_list_len)


if __name__ == '__main__':
    main()
