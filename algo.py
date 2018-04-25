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
import math


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


class kucoin():
    BASE_URL = 'api.kucoin.com'
    secret = 'dc955e1e-12a6-4396-9c1e-bebb21c23b1a'
    key = '5a30780191ed297ad231d9f8'

    def __init__(self, key, secret):
        if key is None:
            key = key
        # also for secret
        self.key = key

    def params_to_str(self, params):
        sign = ''
        keys = list()
        for i in range(0, len(params)):
            keys.append(list(params.keys())[i])
            keys = sorted(keys)
        for i in range(0, len(params)):
            sign = sign + keys[i] + '=' + params[keys[i]] + '&'
        sign = sign[:-1]
        return sign

    def _get(self, endpoint, payload):
        header = {
            'Accept-Language': 'en_US',
            'Content-type': 'application/json'
        }
        url = 'http://api.kucoin.com' + endpoint
        # send GET request to that url
        header['KC-API-NONCE'] = str(int(time() * 1000))
        header['KC-API-SIGNATURE'] = self._sign(self, endpoint, self.params_to_str(self, payload), header['KC-API-NONCE'])
        header['KC-API-KEY'] = self.key
        request = requests.get(url + "?" + self.params_to_str(payload), params=payload, headers=header)
        response_body = request.json()
        return response_body

    def _sign(self, endpoint, str_params_for_sign, nonce):
        # use SHA_256 to encrypto
        str_to_sign = endpoint + '/' + nonce + '/' + str_params_for_sign
        str_to_sign = base64.b64encode(str_to_sign.encode('utf-8'))
        signed_str = hmac.new(self.secret.encode(), str_to_sign, hashlib.sha256).hexdigest()
        return signed_str

    def _post(self, endpoint, payload):
        # organize header
        header = {
            'Accept-Language': 'en_US',
            'Content-type': 'application/json'
        }
        url = 'https://api.kucoin.com' + endpoint
        header['KC-API-NONCE'] = str(int(time() * 1000))
        signed_str = self._sign(self, endpoint, self.params_to_str(self, payload), header['KC-API-NONCE'])
        # post your request to url
        header['KC-API-SIGNATURE'] = signed_str
        # add key and nonce
        header['KC-API-KEY'] = self.key
        data = ''
        print('arguments are', url + '?' + self.params_to_str(self, payload), header)
        request = requests.post(url + '?' + self.params_to_str(self, payload), data=json.dumps({}), headers=header)
        response_body = request.json()
        print('Latency (ms):', int(header['KC-API-NONCE']) - int(time() * 1000))
        print(payload)
        return response_body

    # get kline data
    def historic(self, symbol, first, last):
        payload = {
            'symbol': symbol,
            'from': first,
            'to': last
        }
        r = requests.get('https://api.kucoin.com/v1/open/chart/history', params=payload)
        jdata = r.json()
        return jdata


class TestClient():
    def __init__(self, exchange, currency, quote_currency):
        #initialize the exchange client for kucoin
        client = Client(None, None)
        #initialize market
        pass
    def test_ticker(self):
        #get ticker
        ticker = self.client.get_ticker()
        assert ticker is not None
        assert isinstance(ticker['last'], [float, int])
        assert 'bid' in ticker.keys()
        #verify ticker

        pass

    def test_order(self):
        #get active orders
        active_orders = client.get_active_orders(self.market)
        for order_id, value in active_orders.items():
            #cancel it
            pass
            #check the order info
            order_info = self.client.get_order_info(order_id, self.market, 'buy')
            #check the balance
            #re-create the order at the same price with same volume

    def test_rate_limit(self):
        try_times = 0
        while(try_times <= 500):
            #get balacne'
            try_times += 1

        #test public endpoints

    def run(self):
        pass

'''
print(kucoin._post(kucoin, '/v1/order', {
    'symbol':'RPX-ETH',
    'type':'BUY',
    'amount': '10',
    'price': '0.000001'
}))
print(kucoin._get(kucoin, '/v1/order/active', {
    'symbol':'RPX-ETH',
    'type':'BUY'
}))
'''


class data_process():
    def moving_average(self, values,window):
        sum = 0
        for i in range(0,window):
            sum += values[len(values)-window+i]
        movingaverage = sum/window
        return movingaverage

    def standard_dev(self, values, window):
        frame = values
        frame = list(map(lambda x: x - 13, frame))
        frame = list(map(lambda x: x ** 2, frame))
        var = sum(frame) / (window - 1)
        var = math.sqrt(var)
        return var

    def average(self, values):
        total = sum(values)
        return total/len(values)

 # basic trading logic


"""
 #calculating bollinger bands
   top_band = []
   mid_band = []
   bot_band = []

   while True: 
       mid_band.append(data_process.movingaverage(data, 20))
       top_band.append(data_process.movinigaverage(data, 20) + 2 * data_process.standard_dev(


   if current_bid =< upper_band :
       sell x amount
   if current_bid => lower_band :
       buy x amount


"""



