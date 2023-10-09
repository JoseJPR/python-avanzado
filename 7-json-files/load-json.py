import json

with open('example.json', 'r') as json_file:
    content = json.load(json_file)

print(type(content))
print(content)
print(content['firstName'])