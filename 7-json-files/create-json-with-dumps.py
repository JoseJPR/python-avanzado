import json

person = {
    'firstName': 'John',
    'lastName': 'Doe',
    'age': 41,
    'active': False
}

serialized = json.dumps(person, indent=2)
with open('example.json', 'w') as json_file:
    json_file.write(serialized)
