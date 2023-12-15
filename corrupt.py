
try:
    file = open('txt/Lab14.txt', 'r', encoding='UTF-8')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Файл не найден")
finally:
    pass