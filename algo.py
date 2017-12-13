from urllib2 import Request, urlopen
import requests
from time import time
import base64
import json


def signature(): #dc955e1e-12a6-4396-9c1e-bebb21c23b1a is secret
    host = 'https://api.kucoin.com'
    endpoint = '/v1/KCS-BTC/order'
    secret = 'dc955e1e-12a6-4396-9c1e-bebb21c23b1a'
    string = endpoint+'/'+secret
    string = base64.b64encode(string)
    return string


Authorize = {
    "KC-API-KEY": "59c5ecfe18497f5394ded813",
    "KC-API-NONCE": time(),
    "KC-API-SIGNATURE": signature()
}
KEY = requests.get('https://api.kucoin.com/v1/api/list',params=Authorize)


request = Request('https://api.kucoin.com/v1/open/currencies')

response_body = urlopen(request).read()
print response_body
