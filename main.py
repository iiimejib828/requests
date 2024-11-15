import requests
import pprint

url = 'https://api.github.com/search/repositories'

params = {
    'q': 'html'
}

response = requests.get(url=url, params=params)

print(f"\n\nУрл - {url}, параметры {params}\n")
print(response.status_code)
pprint.pprint(response.json())


url = 'https://jsonplaceholder.typicode.com/posts'

params = {
    'userId': '1'
}

response = requests.get(url=url, params=params)

print(f"\n\nУрл - {url}, параметры {params}\n")
print(response.status_code)
pprint.pprint(response.json())

url = 'https://jsonplaceholder.typicode.com/posts'

params = {
    'title': 'test',
    'body': 'request',
    'userId': 1
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url=url, json=params, headers=headers)

print(f"\n\nУрл - {url}, параметры {params}\n")
print(response.status_code)
pprint.pprint(response.json())
