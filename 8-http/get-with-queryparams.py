import requests

r = requests.get('https://jsonplaceholder.typicode.com/comments', params={
    'postId': 1
})
print(r.json())
