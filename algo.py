from urllib2 import Request, urlopen
import requests
from time import time
import base64
import json
import ccxt
from time import sleep
import numpy as np
import plotly.plotly as py
from datetime import datetime
from plotly.tools import FigureFactory as FF
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.offline as offline
import plotly.graph_objs as go
import json
'''
request = Request('https://api.kucoin.com/v1/user/info ')
secret = 'dc955e1e-12a6-4396-9c1e-bebb21c23b1a'
key = '5a30780191ed297ad231d9f8'

print int(time()*1000)
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


dataRPX = list()
maverage = list()
changeRPX = list()

# this is the main loop
while True:
    # add latest price to price list
    dataRPX.append(priceRPX())
    print('current price:',priceRPX(),'index:', len(dataRPX), 'change:',  round(100*(dataRPX[len(dataRPX)-1]/dataRPX[len(dataRPX)-2]), 2))


    sleep(1)

# noinspection PyUnreachableCode


class Client():
    BASE_URL = 'api.kucoin.com'

    def __init__(self, key, secret):
        if key is None:
            key = key
        #also for secret
        self.key = key


def params_to_str():
    pass


def _get(endpoint, **parmas):
    prams_str = ''
    url = BASE_URL + '?' + params_str
    # send GET request to that url
    date = parse('')
    pass


def parse(data):
    return ''
    pass




def _sign(endpoint, str_params_for_sign):
    # use SHA_256 to encrypto
    str_to_sign = endpoint + '/' + i    nt(time()*1000) + '/' + str_params_for_sign
    str_to_sign = base64.b64encode(str_to_sign.encode('utf-8'))
    signed_str = hmac.new(secret.encode(), str_to_sign, hashlib.sha256).hexdigest()
    return signed_str


def _nonce():
    return


def _post(endpoint, payload):
    # organize header
    header = {}
    payload = {

    }
    url = BASE_URL + '/' + endpoint
    signed_str = _sign(endpoint, str_params_for_sign)
    # post your request to url
    header['KC-API-SIGNATURE'] = signed_str
    header['KC-API-NONCE'] = time()
    # add key and nonce

    data = ''
    # parse
    return


def create_limit_order(symbol, side, price, amount):
    pass

'''


# historic data
def historic(symbol,first, last):
    payload = {
        'symbol':symbol,
        'from':first,
        'to':last
    }
    request = requests.get('https://api.kucoin.com/v1/open/chart/history', params=payload)
    jdata = request.json()
    return jdata['c']


print historic('RPX-ETH', '1006609507', '1516033560')

# graphing
offline.init_notebook_mode()
plotdata = historic('RPX-ETH', '1006609507', '1516033560')
plotx = []
plotx = range(0,len(plotdata))
offline.iplot({'data': [{'y': plotdata}], 'layout': {'title': 'Test Plot', 'font': dict(size=16)}}, image='png')
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
