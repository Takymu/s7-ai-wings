import csv
import openpyxl


def word(obj):
    return ''.join(i for i in obj if i.isalpha() or i == ' ')

data = []
try:
    with open('dataset', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            row = [word(i) for i in row]
            data.append(row)
        print(data)
except FileNotFoundError:
    print(f"file is not found.")
    exit()

wb = openpyxl.Workbook()
ws = wb.active

for row in data:
    ws.append(row)

wb.save('output1.xlsx')
