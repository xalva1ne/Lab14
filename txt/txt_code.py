number_tuple = (1,2,3,4,5,6,7,8,9,0)

counter = 0

for num in number_tuple:
    if num % 2 == 0:
        counter += 1

with open("Lab14.txt", "w", encoding="utf-8") as file:
    file.write(f'Количество: {counter}')

with open("Lab14.txt", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)