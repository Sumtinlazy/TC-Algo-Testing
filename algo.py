import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
import numpy
import requests
from time import time
import base64
import json
from time import sleep
import numpy as np
import hashlib
import hmac
import pandas as pd
from matplotlib.finance import candlestick_ochl as ochl


request = requests.get('https://api.kucoin.com/v1/user/info ')
secret = 'dc955e1e-12a6-4396-9c1e-bebb21c23b1a'
key = '5a30780191ed297ad231d9f8'

'''
# returns the current price of RPX
def priceRPX():
    request = Request('https://api.kucoin.com/v1/open/tick?symbol=RPX-ETH')
    data = urlopen(request).read()
    data = json.loads(data)
    data = data['data']['lastDealPrice']
    return data


dataRPX = list()
maverage = list()
changeRPX = list()

# this is the main loop
while True:
    # add latest price to price list
    dataRPX.append(priceRPX())
    print('current price:',priceRPX(),'index:', len(dataRPX), 'change:',  round(100*(dataRPX[len(dataRPX)-1]/dataRPX[len(dataRPX)-2]), 2))


    sleep(1)
'''
# noinspection PyUnreachableCode


class Client():
    BASE_URL = 'api.kucoin.com'

    def __init__(self, key, secret):
        if key is None:
            key = key
        # also for secret
        self.key = key


# Alphabetizes dictionary and converts to string
def params_to_str(params):
    sign = ''
    keys = list()
    for i in range(0, len(params)):
        keys.append(list(params.keys())[i])
        keys = sorted(keys)
    for i in range(0,len(params)):
        sign = sign+keys[i]+'='+params[keys[i]]+'&'
    sign = sign[:-1]
    return sign


def _get(endpoint, payload):
    header = {
        'Accept-Language': 'en_US',
        'Content-type': 'application/json'
    }
    url = 'http://api.kucoin.com' + endpoint
    # send GET request to that url
    header['KC-API-NONCE'] = str(int(time()*1000))
    header['KC-API-SIGNATURE'] = _sign(endpoint, params_to_str(payload),header['KC-API-NONCE'])
    header['KC-API-KEY'] = key
    request = requests.get(url + "?" + params_to_str(payload), params=payload, headers=header)
    response_body = request.json()
    return response_body


def parse(data):
    return ''
    pass


def _sign(endpoint, str_params_for_sign,nonce):
    # use SHA_256 to encrypto
    str_to_sign = endpoint + '/' + nonce + '/' + str_params_for_sign
    str_to_sign = base64.b64encode(str_to_sign.encode('utf-8'))
    signed_str = hmac.new(secret.encode(), str_to_sign, hashlib.sha256).hexdigest()
    return signed_str


def _post(endpoint, payload):
    # organize header
    header = {
        'Accept-Language':'en_US',
        'Content-type':'application/json'
    }
    url = 'https://api.kucoin.com' + endpoint
    header['KC-API-NONCE'] = str(int(time()*1000))
    signed_str = _sign(endpoint,params_to_str(payload), header['KC-API-NONCE'])
    # post your request to url
    header['KC-API-SIGNATURE'] = signed_str
    # add key and nonce
    header['KC-API-KEY'] = key
    data = ''
    print('arguments are', url+'?'+params_to_str(payload), header)
    request = requests.post(url+'?'+params_to_str(payload),data=json.dumps({}),headers=header)
    response_body = request.json()
    print('Latency (ms):',int(header['KC-API-NONCE'])-int(time()*1000))
    print(payload)
    return response_body


def create_limit_order(symbol, side, price, amount):
    pass


requests.post('https://api.kucoin.com/v1/order',params={'amount': '10',
    'price': '.00023',
    'type': 'BUY'})

# historic data


def historic(symbol,first, last):
    payload = {
        'symbol': symbol,
        'from': first,
        'to': last
    }
    request = requests.get('https://api.kucoin.com/v1/open/chart/history', params=payload)
    jdata = request.json()
    return jdata


data = historic('RPX-ETH', 1250000000,int(time()))

df = pd.DataFrame({
    'open':data['c'],
    'tstamp':data['t'],
    'volume':data['v'],
    'high':data['h'],
    'close':data['o'],
    'low':data['l']
})


def movingaverage(values,window):
    maverage = []
    for i in range(0,len(values)):
        maverage.append(sum(values[i:window+i])/window)

    return maverage

# bollinger bands

test = range(0,200)
print(movingaverage(test,10))
print(sum(test[190:200]))