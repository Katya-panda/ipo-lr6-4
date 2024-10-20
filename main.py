# функция для поиска строк в файле, содержащих искомую подстроку
def search_in_file(file_name, search_string):
    found_lines = []  # список для хранения найденных строк
    with open(file_name, 'r', encoding='utf-8') as file:  # открываем файл для чтения
        for line in file:  # проходим по каждой строке в файле
            if search_string in line:  # проверяем, содержится ли искомая подстрока в строке
                found_lines.append(line.strip())  # если да, добавляем строку в список (удаляем пробелы в начале и конце)
    return found_lines  # возвращаем список найденных строк
# запрашиваем у пользователя строку для поиска
search_string = input("Введите строку для поиска: ")
# указываем имя файла, в котором будем искать
file_name = 'text.txt'
# вызываем функцию для поиска строк, передавая имя файла и искомую строку
found_lines = search_in_file(file_name, search_string)
# определяем количество найденных строк
count_found = len(found_lines)  # считаем количество найденных строк
# выводим количество найденных строк
print(f"Найдено строк: {count_found}")
# проверяем, существуют ли найденные строки
if count_found > 0:
    # сортируем найденные строки по длине
    sorted_lines = sorted(found_lines, key=len)  # сортировка по длине строк
    # выводим отсортированные строки
    print("Найденные строки (от самой короткой к самой длинной):")
    for line in sorted_lines:  # проходим по отсортированным строкам
        print(line)  # печатаем каждую строку
else:
    print("Совпадений не найдено.")  # если строки не найдены, сообщаем об этом
