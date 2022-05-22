#https://api.github.com/users/defunkt

import requests
from pprint import pprint
import json

url = 'https://api.github.com'
user = 'AntonGun'
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47"}

# Profile info
req = f'{url}/users/{user}'
info = requests.get(req, headers=headers).json()
pprint(info)

# Profile repos
rep = f'{url}/users/{user}/repos'
repo = requests.get(rep, headers=headers).json()
pprint(repo)

with open('data_git.json', 'w') as f:
    json.dump(repo, f)
