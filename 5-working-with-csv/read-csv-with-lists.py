import csv

path = 'example.csv'
with open(path, 'r', encoding='utf-8') as open_file:
    reader = csv.reader(open_file, delimiter=',')
    print(reader)
    print(list(reader))

print('--------------')

with open(path, 'r', encoding='utf-8') as open_file:
    reader = csv.reader(open_file, delimiter=',')
    colums = next(reader)
    print(reader)
    print(list(reader))
