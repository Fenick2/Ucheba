import json
import requests
from requests.exceptions import HTTPError


res1 = requests.get('https://api.github.com',
    params={'q':'requests+language:python'})
# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         res = requests.get(url)
#         res.raise_for_status()
#     except HTTPError as e:
#         print(f'HTTP error occured: {e}')
#     except Exception as err:
#         print(f'Other error occured: {err}')
#     else:
#         print('Success!')
print(res1.text)