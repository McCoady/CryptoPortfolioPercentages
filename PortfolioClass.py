class Portfolio():

    def __init__(self, name, currencytype, currencyin):
        # Account name
        self.name = name
        # What currency do you want your portfolio displayed in (GBP,USD,EUR etc)
        self.currencytype = currencytype
        # What is initial portfolio total
        self.currencyin = currencyin

    def __str__(self):
        return f"{self.name}'s investment total: {self.currencyin}"

    def currencyconverter(self, currencyin, currencyout):
        # Use API to get a conversion rate from currencyin > currencyout
        # return currencyout
        pass

    def fiatdeposit(self, depcurrency, deposit):
        if depcurrency == self.currencytype:
            self.currencyin += deposit
        else:
            pass
        print(
            f'Updated total fiat deposited. Total fiat invested = {self.currencytype}{self.currencyin}')
