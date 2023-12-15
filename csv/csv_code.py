import csv

number_tuple = (1,2,3,4,5,6,7,8,9,0)

counter = 0

for num in number_tuple:
    if num % 2 == 0:
        counter += 1

with open("Lab14.csv", "w", encoding="utf-8", newline="") as file:
    write = csv.writer(file)
    write.writerow(['Количество', counter])


with open("Lab14.csv", "r", encoding="utf-8") as file:
    read = csv.reader(file)
    print(next(read))