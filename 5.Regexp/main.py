from pprint import pprint
import re

## Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("5.Regexp\phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


def correct_fio(rows):
    pattern = r"\w+"
    for index, value in enumerate(rows[1:], start=1):
        correct_row = re.findall(pattern, " ".join(value))[0:3] + rows[index][3:]
        rows[index] = correct_row
    return rows


def remove_duplicate(correct_fio):
    res = []
    res.append(correct_fio[0])
    for value_1 in correct_fio:
        for value_2 in res:
            if (
                value_2[0].lower() == value_1[0].lower()
                and value_2[1].lower() == value_1[1].lower()
            ):
                break
        else:
            res.append(value_1)
    return res


def updating_phone_numbers(rows, regular, new):
    phonebook = []
    pattern = re.compile(regular)
    phonebook = [[pattern.sub(new, string) for string in strings] for strings in rows]

    return phonebook


contacts_list = correct_fio(contacts_list)
contacts_list = remove_duplicate(contacts_list)
regular = r"(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})"
contacts_list = updating_phone_numbers(contacts_list, regular, r"+7(\2)\3-\4-\5")
regular_2 = r"(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s]*[(доб.\s]*(\d+)[)]*"
correct_phonebook = updating_phone_numbers(
    contacts_list, regular_2, r"+7(\2)\3-\4-\5 доб.\6"
)


# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("5.Regexp\phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=",")

    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(correct_phonebook)
