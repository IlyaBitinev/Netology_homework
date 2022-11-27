import csv
import re


def reader(csv_file):
    with open(csv_file, encoding='utf8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)
        return contacts_list


def change_names(row_list):
    for item in row_list:
        for j in item[:3]:
            a = j.split()
            if len(a) == 1:
                continue
            elif len(a) == 2:
                item[0] = a[0]
                item[1] = a[1]
            elif len(a) == 3:
                item[0] = a[0]
                item[1] = a[1]
                item[2] = a[2]
    return row_list


def duplicate_deleting(row_list):
    table = [row_list[0]]
    for i in row_list[1:]:
        if i[0] not in [j[0] for j in table]:
            table.append(i)
        else:
            for j in table:
                if j[0] == i[0]:
                    j.extend([k for k in i if k not in j])
    return table


def change_phone(row_list):
    pattern = r'(\+7|8)\s*?\(?(\d{3})\)?\s*?-?\s*(\d{3})-?(\d{2})-?(\d{2})\s*\(?(доб.\s*\d*)?\)?'
    substitution = r'+7(\2)-\3-\4-\5 \6'
    some_list = []
    for item in row_list:
        text = ' '.join(i for i in item)
        new = re.sub(pattern, substitution, text)
        some_list.append([new])
    return some_list


def writer(result):
    with open(r'phonebook.csv', 'w', encoding='utf8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(result)
