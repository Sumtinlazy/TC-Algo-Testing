from urllib2 import Request, urlopen
import requests
from time import time
import base64
import json
import ccxt
from time import sleep
import numpy as np
'dc955e1e-12a6-4396-9c1e-bebb21c23b1a is secret'


# returns the current price of RPX
def priceRPX():
    request = Request('https://api.kucoin.com/v1/open/tick?symbol=RPX-ETH')
    data = urlopen(request).read()
    data = json.loads(data)
    data = data['data']['lastDealPrice']
    return data


def movingaverage(values, window):
    weights = np.repeat(1.0, window) / window
    sma = np.convolve(values, weights, 'valid')
    return sma

def authenticate(type, amount, price):


dataRPX = list()
maverage = list()
changeRPX = list()

# this is the main loop
while True:
    # add latest price to price list
    dataRPX.append(priceRPX())
    print('current price:',priceRPX()),len(dataRPX)

    if len(dataRPX) > 60:
        # find average price from last minute
        trend = movingaverage(dataRPX, 60)
        print('trend last minute:',(dataRPX[len(dataRPX)]-dataRPX[len(dataRPX)-60])/dataRPX[len(dataRPX)-60]*100) + '%'



    sleep(1)

# noinspection PyUnreachableCode

class Client():
    BASE_URL = 'api.kucoin.com'
    def __init__(self, key = None, secret = None):
        if key is None:
            key = DEFAULT_KEY
        #also for secret
        self.key = key


def params_to_str():
    pass

def _get(endpoint, **parmas):
    prams_str = ''
    url = BASE_URL + '?' + params_str
    #send GET request to that url
    date = parse('')
    pass

def parse(data):
    pass

def _sign(endpoint, nonce, str_params_for_sign):
    #use SHA_256 to encrypto
    str_to_sign = endpoint + '/' + nonce + '/' + str_params_for_sign
    str_to_sign = base64.b64encode(str_to_sign.encode('utf-8'))
    signed_str = hmac.new(secret.encode(), str_to_sign, hashlib.sha256).hexdigest()
    return signed_str

def _nonce():
    return

def _post(endpoint, payload):
    #organize header
    header = {}
    payload = {}
    url = BASE_URL + '/' + endpoint
    signed_str = _sign(endpoint, nonce, str_params_for_sign)
    #post your request to url
    header['KC-API-SIGNATURE'] = signed_str
    #add key and nonce

    data = ''
    #parse
    return


def create_limit_order(symbol, side, price, amount):
    pass

'''
average = []
trend = []
coins = 'ETH'
price = requests.get('https://api.kucoin.com/v1/open/currencies')
data = urlopen(price).read()
data = json.loads(data)
USD = data['data']['rates']['BTC']['USD']
print data
parameters = {
    type: BUY,
    amount: 10,
    price: 1.1
}

def signature(order, amount, price):
    type = order


    r = Request('https://api.kucoin.com/')
    r.headers = {
        "KC-API-KEY": "5a30780191ed297ad231d9f8",
        "KC-API-NONCE" : time(),
        "KC-API-SIGNATURE" : signature(parameters)
}

while True:
    if len(average) < 10 :
        average.append(USD)
    else:
        del average[0]
        average.append(USD)
    data = urlopen(price).read()
    data = json.loads(data)
    USD = data['data']['rates']['BTC']['USD']
    print(average)
    if len(average) == 10:
        maverage = (float(average[0]))/int(average[9])-1
        print maverage, "% <-- growth in last 10 ticks"
        trend.append(maverage)
        print average[0] - average[9]
    price = Request('https://api.kucoin.com/v1/open/currencies')
    sleep(10)
'''