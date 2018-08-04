
###############################################################
##                                                           ##
##  This section is for pulling in data from the public API  ##
##                                                           ##
###############################################################

# pull in the GDAX client library and the datetime library
# for more info and to download this GDAX client see the github ReadMe file at https://github.com/danpaquin/gdax-python
# also, https://docs.gdax.com/#get-product-order-book is very useful for reference

import gdax
import datetime
import login
# # create a variable to pull in the public products dictionary
# public_client = gdax.PublicClient()
#
# # List of avialable methods for 'public_client':
# # get_currencies
# # get_product_24hr_stats
# # get_product_historic_rates
# # get_product_order_book
# # get_product_ticker
# # get_product_trades
# # get_products
# # get_time
# # Build a list of trading pairs to use to call from dictionaries
# trading_pairs = list()
# products = public_client.get_products()
#
#
# for product in products:
#     pair = product['id']
#     trading_pairs.append(pair)
# trading_pairs.sort()
#

# order of pairs from above:
# 0 BCH-BTC
# 1 BCH-EUR
# 2 BCH-USD
# 3 BTC-EUR
# 4 BTC-GBP
# 5 BTC-USD
# 6 ETH-BTC
# 7 ETH-EUR
# 8 ETH-USD
# 9 LTC-BTC
# 10 LTC-EUR
# 11 LTC-USD


def get_current_orders(pair):
    dict = login.auth_client.get_product_order_book(pair, level=1)
    return dict


# wsClient = gdax.WebsocketClient(url="wss://ws-feed.gdax.com", products=["BTC-USD", "ETH-USD"])
