import json

number_tuple = (1,2,3,4,5,6,7,8,9,0)

counter = 0

for num in number_tuple:
    if num % 2 == 0:
        counter += 1

data = {'Total numbers': counter}

with open("Lab14.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

with open("Lab14.json", "r", encoding="utf-8") as file:
    result = json.load(file)
    print(result)