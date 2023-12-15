import openpyxl

number_tuple = (1,2,3,4,5,6,7,8,9,0)

counter = 0

for num in number_tuple:
    if num % 2 == 0:
        counter += 1

book = openpyxl.Workbook()

sheet = book.active

sheet['A1'] = 'Количество'
sheet['B1'] = counter

with open("Lab14.xlsx", "wb") as file:
    book.save(file)

with open("Lab14.xlsx", "rb") as file:
    book = openpyxl.load_workbook(file)
    counter_excel = [sheet['A1'].value, sheet['B1'].value]
    print(counter_excel)