import csv

path = 'example.csv'
with open(path, 'r', encoding='utf-8') as open_file:
    reader = csv.DictReader(open_file, delimiter=',')
    print(reader)
    print(list(reader))
