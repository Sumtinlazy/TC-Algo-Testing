import requests
from time import time

r = requests.get('https://api.kucoin.com/', {
    'KC-API-KEY': '5a300ab009e5a11c90c5a220',
    'KC-API-NONCE': time(),
    'KC-API-SIGNATURE': 'fd83147802c361575bbe72fef32ba90dcb364d388d05cb909c1a6e832f6ca3ac'
})

print(r.status_code)