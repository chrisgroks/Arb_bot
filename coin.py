# This object is built based on two input trading pairs(IE: 'ETH-USD', 'BTC-USD'). When instantiated, it will
# automatically create two dictionaries with the best current bid/ask info. The methods here return the needed values.
# While looping the main program, only 6(?) of these should be created. Once built, the dictionaries can be updated
# each time the arb opportunity search loops through.
import fetch


class Coin:

    def __init__(self, pair1, pair2, pair3):
        self.pair1 = pair1
        self.pair2 = pair2
        self.pair3 = pair3
        self.first_dict = fetch.get_current_orders(pair1)
        self.second_dict = fetch.get_current_orders(pair2)
        self.third_dict = fetch.get_current_orders(pair3)

    # TODO test this update method
    # This updates the dictionaries
    def dict_update(self):
        self.first_dict = fetch.get_current_orders(self.pair1)
        self.second_dict = fetch.get_current_orders(self.pair2)
        self.third_dict = fetch.get_current_orders(self.pair3)
    # Get current asking price for trading pairs --> output from GDAX = [price, order size, number of asks]
    # example --> if there are (2) orders each of 100 BTC at $100, the output would look like this: {100, 200, 2]

    # this function returns best bid and ask on order book for pair.
    # return from gdax:
    #  {
    #     "sequence": "3",
    #     "bids": [
    #         [ price, size, num-orders ],
    #     ],
    #     "asks": [
    #         [ price, size, num-orders ],
    #     ]
    # }
    def get_ask_price(self, dictionary):
            return float(dictionary['asks'][0][0])

    # Pull the inverse of the current ask for arbitrage purposes
    def inv_ask(self, dictionary):
        return 1.0 / float(self.get_ask_price(dictionary))

    # get current ask size
    def get_ask_size(self, dictionary):
        return float(dictionary['asks'][0][1])

    # Pull the current bid prices
    def get_bid_price(self, dictionary):
        return float(dictionary['bids'][0][0])

    # Pull the inverse of the current bid for arbitrage purposes
    def inv_bid(self, dictionary):
        return 1.0 / float(self.get_bid_price(dictionary))

    # get current bid size
    def get_bid_size(self, dictionary):
        return float(dictionary['bids'][0][1])

    # Pull in GDAX fees:
    # BTC transactions = 0.25%
    # All others = 0.3%

    def fees(self, pair):
        if pair[0] == 'E':
            return 0.0030
        if pair[0] == 'L':
            return 0.0030
        else:
            return 0.0025

