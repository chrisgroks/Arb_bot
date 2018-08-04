import gdax


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

# Dummy account for now --> once proof on concept is complete will connect to GDAX account
account = 100

# TODO make these functions nicer!
# determine order size [in USD] with the funds(account) function --> account is just your account size in USD
def funds(coin, account):
    usd_crypto_check = coin.get_ask_price(coin.first_dict) * coin.get_ask_size(coin.first_dict)
    crypto_crypto_check = coin.get_ask_price(coin.second_dict) * coin.get_ask_size(coin.second_dict) * coin.get_ask_price(coin.first_dict)
    crypto_usd_check = coin.get_ask_price(coin.third_dict) * coin.get_ask_size(coin.third_dict)
    if usd_crypto_check and crypto_crypto_check and crypto_usd_check > account:
        return account
    else:
        return min(usd_crypto_check, crypto_crypto_check, crypto_usd_check)

# TODO document this
def arb_calc(coin):
    initial_trade = (funds(coin, account) - (funds(coin, account) * coin.fees(coin.pair1))) * coin.get_ask_price(coin.first_dict)
    middle_trade = (initial_trade - (initial_trade * coin.fees(coin.pair2))) * coin.inv_ask(coin.second_dict)
    final_trade_value = (middle_trade - (middle_trade * coin.fees(coin.pair3))) * coin.inv_ask(coin.third_dict)
    return final_trade_value


def arb_btc_calc(coin):
    initial_trade = (funds(coin, account) - (funds(coin, account) * coin.fees(coin.pair3))) * coin.get_ask_price(coin.third_dict)
    middle_trade = (initial_trade - (initial_trade * coin.fees(coin.pair2))) * coin.get_ask_price(coin.second_dict)
    final_trade_value = (middle_trade - (middle_trade * coin.fees(coin.pair1))) * coin.inv_ask(coin.first_dict)
    return final_trade_value



