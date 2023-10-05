import csv

columns = ['First Name', 'Last Name']
persons = [
    {
        'First Name': 'John',
        'Last Name': 'Doe'
    },
    {
        'First Name': 'Other',
        'Last Name': 'Example'
    },
]

path = 'example.csv'
with open(path, 'w') as open_file:
    writer = csv.DictWriter(open_file, fieldnames=columns, delimiter=',')
    writer.writeheader()
    writer.writerows(persons)
