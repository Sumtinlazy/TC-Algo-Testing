from urllib2 import Request, urlopen
import requests
from time import time
import base64
import json
import ccxt
from time import sleep

#dc955e1e-12a6-4396-9c1e-bebb21c23b1a is secret

'''
average = []
trend = []
coins = 'ETH'
price = requests.get('https://api.kucoin.com/v1/open/currencies', params = coins)
data = urlopen(price).read()
data = json.loads(data)
USD = data['data']['rates']['BTC']['USD']
print data
parameters = {
    type: BUY,
    amount: 10,
    price: 1.1
}
'''


def signature(order, amount, price):
    type = order
    

    r = Request('https://api.kucoin.com/')
    r.headers = {
        "KC-API-KEY": "5a30780191ed297ad231d9f8",
        "KC-API-NONCE" : time(),
        "KC-API-SIGNATURE" : signature(parameters)
}


'''
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
