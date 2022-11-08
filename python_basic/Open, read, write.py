import os
from pprint import pprint

FILE_NAME = "recipes.txt"
BASE_PATH = os.getcwd()
full_path = os.path.join(BASE_PATH, FILE_NAME)


def catalog_dish_reader(file):
    cook_book = {}
    with open(file, encoding='utf-8') as file_obj:
        for line in file_obj:
            name_dish = line.strip()
            cook_book[name_dish] = []
            for i in range(int(file_obj.readline())):
                ingredient = file_obj.readline().strip().split('|')
                cook_book[name_dish].append(
                    {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
            file_obj.readline()
        return cook_book

# вывод 1 задания
# pprint(catalog_dish_reader(full_path), width=200, sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = {}
    cook_book = catalog_dish_reader(full_path)
    for item in dishes:
        if item in cook_book:
            for ingredient in cook_book[item]:
                if ingredient['ingredient_name'] in dishes_dict:
                    dishes_dict[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
                else:
                    dishes_dict[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': (
                            int(ingredient['quantity']) * person_count)}
        else:
            print(f'Блюдо "{item}" нет в меню')
    return dishes_dict


# вывод 2 задания
# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

def file_reading():
    file_dict = {}
    for filename in os.listdir('open, read, write task3'):
        with open(os.path.join('open, read, write task3', filename), encoding='utf-8') as file:
            text = file.readlines()
            total = sum(1 for line in text)
            file_dict[filename] = [total, text]
    return sorted(file_dict.items(), key=lambda item: item[1][0])


def file_writer(text_list):
    for element in text_list:
        with open('result.txt', 'a', encoding='utf-8') as file:
            file.write(element[0] + '\n')
            file.write(str(element[1][0]) + '\n')
            for row in element[1][1]:
                if row == element[1][1][-1]:
                    file.write(row + '\n')
                else:
                    file.write(row)
    return 'Запись файла успешно завершена'

# вывод 3 задания
# print(file_writer(file_reading()))
