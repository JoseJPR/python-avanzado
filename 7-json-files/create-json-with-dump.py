import json

person = {
    'firstName': 'John',
    'lastName': 'Doe',
    'age': 41,
    'active': False
}

with open('example.json', 'w') as json_file:
    json.dump(person, json_file)
