import datetime
import coin
import arbitrage
import time
import login

login.auth_client
a = True
sleepTime = .3


eth_usd = coin.Coin('ETH-USD', 'ETH-BTC', 'BTC-USD')
time.sleep(sleepTime)
ltc_usd = coin.Coin('LTC-USD', 'LTC-BTC', 'BTC-USD')
time.sleep(sleepTime)
bch_usd = coin.Coin('BCH-USD', 'BCH-BTC', 'BTC-USD')
time.sleep(sleepTime)
percentage = .99
print("Objects created. Now scanning...")
while a:
# ETH
    eth_usd.dict_update()
    x = arbitrage.arb_calc(eth_usd)

    if x > arbitrage.account * percentage:
        #a = False
        print("Arb opportunity! ", datetime.datetime.now().time())
        print("ETH-BTC: ", x)
    y = arbitrage.arb_btc_calc(eth_usd)

    if y > arbitrage.account * percentage:
        #a = False
        print("Arb opportunity! ", datetime.datetime.now().time())
        print("BTC-ETH: ", y)
    time.sleep(sleepTime)

# # LTC
#     ltc_usd.dict_update()
#     x = arbitrage.arb_calc(ltc_usd)
#
#     if x > arbitrage.account * percentage:
#         # a = False
#         print("Arb opportunity! ", datetime.datetime.now().time())
#         print("LTC-BTC: ", x)
#     y = arbitrage.arb_btc_calc(ltc_usd)
#
#     if y > arbitrage.account * percentage:
#         # a = False
#         print("Arb opportunity! ", datetime.datetime.now().time())
#         print("BTC-LTC: ", y)
#     time.sleep(sleepTime)
#
# # BCH
#     bch_usd.dict_update()
#     x = arbitrage.arb_calc(bch_usd)
#
#     if x > arbitrage.account * percentage:
#         # a = False
#         print("Arb opportunity! ", datetime.datetime.now().time())
#         print("BCH-BTC: ", x)
#     y = arbitrage.arb_btc_calc(bch_usd)
#
#     if y > arbitrage.account * percentage:
#         # a = False
#         print("Arb opportunity! ", datetime.datetime.now().time())
#         print("BTC-BCH: ", y)
#     time.sleep(sleepTime)