import requests

r = requests.post('https://jsonplaceholder.typicode.com/posts', data={
    'userId': 1,
    'title': 'title example',
    'body': 'body example'
})
print(r.json())
