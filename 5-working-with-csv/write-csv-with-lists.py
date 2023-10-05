import csv

columns = ['First Name', 'Last Name']
persons = [
    ['John', 'Doe'],
    ['Other', 'Example']
]

path = 'example.csv'
with open(path, 'w') as open_file:
    writer = csv.writer(open_file, delimiter=',')
    writer.writerow(columns)
    writer.writerows(persons)
