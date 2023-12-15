
try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Файл не найден")

try:
    with open('/folder', 'r') as file:
        content = file.read()
except IsADirectoryError:
    print("Укажите полностью путь к файлу")

try:
    with open('file.txt', 'w') as file:
        file.write('Новая запись')
except PermissionError:
    print("Нет прав на запись в файл")