#https://api.vk.com/method/METHOD?PARAMS&access_token=TOKEN&v=V
#https://api.vk.com/method/users.get?user_ids=210700286&fields=bdate&access_token=533bacf01e11f55b536a565b57531ac114461ae8736d6506a3&v=5.131

import requests
from pprint import pprint
import json


params = {'user_ids': '210700286',
          'token': '533bacf01e11f55b536a565b57531ac114461ae8736d6506a3',
          'v': '5.131'}

vk = f'https://api.vk.com/method/groups.get'
vk_p = requests.get(vk, params=params).json()
pprint(vk_p)

with open('data_vk.json', 'w') as f:
    json.dump(vk_p, f)