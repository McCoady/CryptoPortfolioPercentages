class Coin():

    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker

    def __str__(self):
        # ADD CONVERT COIN DETAILS TO THIS... = USD/GBP/BTC
        return f" 1 {self.name}({self.ticker}) = ..."

    def convertcoin(self):
        # get API of live coin conversion
        # return price of 1 coin in chosen currency
        pass
