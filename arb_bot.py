
###############################################################
##                                                           ##
##  This section is for pulling in data from the public API  ##
##                                                           ##
###############################################################

# pull in the GDAX client library and the datetime library
# for more info on and to download this GDAX client please see the github ReadMe file at https://github.com/danpaquin/gdax-python
# also, https://docs.gdax.com/#get-product-order-book is very useful for reference

import gdax
import datetime

# create a variable to pull in the public products dictionary
public_client = gdax.PublicClient()

# List of avialable methods for 'public_client':
# get_currencies
# get_product_24hr_stats
# get_product_historic_rates
# get_product_order_book
# get_product_ticker
# get_product_trades
# get_products
# get_time
# Build a list of trading pairs to use to call from dictionaries
trading_pairs = list()
products = public_client.get_products()

for product in products:
    pair = product['id']
    trading_pairs.append(pair)
trading_pairs.sort()


# order of pairs from above:
# BCH-BTC
# BCH-EUR
# BCH-USD
# BTC-EUR
# BTC-GBP
# BTC-USD
# ETH-BTC
# ETH-EUR
# ETH-USD
# LTC-BTC
# LTC-EUR
# LTC-USD

# Get current asking price for trading pairs --> output from GDAX = [price, order size, number of asks]
# example --> if there are (2) orders each of 100 BTC at $100, the output would look like this: {100, 200, 2]
def get_ask(pair):
    asks = public_client.get_product_order_book(pair, level=1)
    for ask in asks['asks']:
        return float(ask[0])


# Pull the inverse of the current ask for arbitrage purposes
def inv_ask(pair):
    return 1 / float(get_ask(pair))


# Pull the current bid prices
def get_bid(pair):
    bids = public_client.get_product_order_book(pair, level=1)
    for bid in bids['bids']:
        return float(bid[0])


# Pull the invers of the current bid for arbitrage purposes
def inv_bid(pair):
    return 1 / float(get_bid(pair))


# Pull in GDAX fees:
# BTC transactions = 0.25%
# All others = 0.3%

def fees(pair):
    if pair[0] == 'E':
        return 0.0030
    if pair[0] == 'L':
        return 0.0030
    else:
        return 0.0025

def BCH_BTC_arb():
    USD_BCH_trade = (funds(account,'BCH-USD','BCH-BTC','BTC-USD') - (funds(account,'BCH-USD','BCH-BTC','BTC-USD') * fees('BCH-USD'))) * get_ask('BCH-USD')
    BCH_BTC_trade = (USD_BCH_trade - (USD_BCH_trade * fees('BCH-BTC'))) * inv_ask('BCH-BTC')
    BTC_USD_trade = (BCH_BTC_trade - (BCH_BTC_trade * fees('BTC-USD'))) * inv_ask('BTC-USD')
    return BTC_USD_trade

###########################################################
##                                                       ##
##  This section is for connecting to your GDAX account  ##
##                                                       ##
###########################################################

# 3 inputs needed that is generated under the GDAX API webpage
# key = API key
# b64secret = API secret key
# passphrase = passphrase from GDAX

key = 'user key here'
b64secret = 'user secret key here'
passphrase = 'user passphrase here'

auth_client = gdax.AuthenticatedClient(key, b64secret, passphrase)

##################################################
##                                              ##
##  This section is for checking for Arbitrage  ##
##                                              ##
##################################################

# For arbitrage we always want to start and end in USD

# Looking at ETH arbitrage opportunities
# possible ETH arbritrage combinations are as follows:
# (ETH/USD)/(BTC/USD) < ETH/BTC:
# USD --> ETH
# ETH --> BTC
# BTC --> USD
# or
# (ETH/USD)/(BTC/USD) > ETH/BTC:
# USD --> BTC
# BTC --> ETH
# ETH --> USD


