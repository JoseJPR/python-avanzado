import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(r.json())
