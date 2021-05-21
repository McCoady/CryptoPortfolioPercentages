from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# hideAPI's for github???
# BTC conversion Data

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '100',
    'convert': 'BTC'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'config.api_key',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    BTCdata = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

# GBP Conversion Data
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '100',
    'convert': 'GBP'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'config.api_key',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    UKdata = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

# USD conversion data
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '100',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'config.api_key',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    USdata = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

# Coin Class


class Coin():

    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker

    def convertcoinUS(self):
        for i in range(len(USdata['data'])):
            if USdata['data'][i]['name'] == self.name:
                return USdata['data'][i]['quote']['USD']['price']

    def convertcoinUK(self):
        for i in range(len(UKdata['data'])):
            if UKdata['data'][i]['name'] == self.name:
                return UKdata['data'][i]['quote']['GBP']['price']

    def convertcoinBTC(self):
        for i in range(len(BTCdata['data'])):
            if BTCdata['data'][i]['name'] == self.name:
                return BTCdata['data'][i]['quote']['BTC']['price']

    def __str__(self):
        return f"{self.name}({self.ticker}) = ${round(self.convertcoinUS(),2)} £{round(self.convertcoinUK(),2)} {self.convertcoinBTC()}BTC"


# Coin Class inputs
BTC = Coin('Bitcoin', 'BTC')
ETH = Coin('Ethereum', 'ETH')
BNB = Coin('Binance Coin', 'BNB')
XRP = Coin('Ripple', 'XRP')
ADA = Coin('Cardano', 'ADA')
DOGE = Coin('Dogecoin', 'DOGE')
USDT = Coin('Tether', 'USDT')
DOT = Coin('Polkadot', 'DOT')
BCH = Coin('Bitcoin Cash', 'BCH')
LTC = Coin('Litecoin', 'LTC')
LINK = Coin('Chainlink', 'LINK')
UNI = Coin('Uniswap', 'UNI')
USDC = Coin('USD Coin', 'USDC')
SOL = Coin('Solana', 'SOL')
MATIC = Coin('Polygon', 'MATIC')
XLM = Coin('Stellar', 'XLM')
ETC = Coin('Ethereum Classic', 'ETC')
VET = Coin('VeChain', 'VET')
THETA = Coin('Theta Network', 'THETA')
EOS = Coin('EOS', 'EOS')
TRX = Coin('Tron', 'TRX')
AAVE = Coin('AAVE', 'AAVE')
BUSD = Coin('Binance USD', 'BUSD')
SHIB = Coin('Shiba Inu', 'SHIB')
WBTC = Coin('Wrapped Bitcoin', 'BTC')
FIL = Coin('Filecoin', 'FIL')
OKB = Coin('OKB', 'OKB')
NEO = Coin('NEO', 'NEO')
XMR = Coin('Monero', 'XMR')
LUNA = Coin('Luna', 'LUNA')
# Coins 31+ in market cap (except algorand) missing
ALGO = Coin('Alogrand', 'ALGO')
