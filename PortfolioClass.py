import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Portfolio():

    def __init__(self, name, currencytype, currencyin):
        # Account name
        self.name = name
        # What currency do you want your portfolio displayed in (GBP,USD,EUR etc)
        self.currencytype = currencytype
        # What is initial portfolio total
        self.currencyin = currencyin
        self.coins = {}

    def __str__(self):
        return f"{self.name}'s investment total: {self.currencytype}{self.currencyin}\n Coins in portfolio:"

    '''def currencyconverter(self, currencyin, currencyout):
        # Use API to get a conversion rate from currencyin > currencyout
        # return currencyout
        '''

    def fiatdeposit(self, depcurrency, deposit):
        if depcurrency == self.currencytype:
            self.currencyin += deposit
        else:
            pass
        print(
            f'Updated total fiat deposited. Total fiat invested = {self.currencytype}{self.currencyin}')

    def addcoins(self, coin, amount):
        if coin in self.coins:
            self.coins[coin] += amount
        else:
            self.coins[coin] = amount
        print(
            f'{amount}{coin} added to your portfolio, total {coin}: {self.coins[coin]}')

    def overview(self, currency):
        coinvalues = []
        coinquantity = []
        coins = []
        if currency == 'GBP':
            for coin in self.coins:
                value = coin.convertcoinUK()*self.coins[coin]
                coinquantity.append(self.coins[coin])
                coinvalues.append(value)
                coins.append(coin.ticker)
                # add to total portfolio amount
                total = 0
                for i in coinvalues:
                    total += i
                print(f'{coin}: {value}')
            print(f'Total portfolio value: {total}')

            # coin list data frame
            df = pd.DataFrame(
                {'Coin': coins, 'Amount': coinquantity, 'Value GBP': coinvalues})
            df['Portfolio %'] = round((df['Value GBP']/sum(coinvalues)*100), 2)

            # Pie Chart (donut chart?)
            my_circle = plt.Circle((0, 0), 0.75, color='white')
            fig = plt.figure()
            ax = fig.add_axes([0, 0, 1, 1])
            ax.axis('equal')
            ax.pie(coinvalues, labels=coins, autopct='%1.1f%%',
                   labeldistance=1.05, startangle=90)
            plt.gca().add_artist(my_circle)
            plt.show()

            return df

        elif currency == 'USD':
            for coin in self.coins:
                value = coin.convertcoinUS()*self.coins[coin]
                coinquantity.append(self.coins[coin])
                coinvalues.append(value)
                coins.append(coin.ticker)
                # add to total portfolio amount
                total = 0
                for i in coinvalues:
                    total += i
                print(f'{coin}: {value}')
            print(f'Total portfolio value: {total}')

            # coin list data frame
            df = pd.DataFrame(
                {'Coin': coins, 'Amount': coinquantity, 'Value USD': coinvalues})
            df['Portfolio %'] = round((df['Value USD']/sum(coinvalues)*100), 2)

            # Pie Chart (donut chart?)
            my_circle = plt.Circle((0, 0), 0.75, color='white')
            fig = plt.figure()
            ax = fig.add_axes([0, 0, 1, 1])
            ax.axis('equal')
            ax.pie(coinvalues, labels=coins, autopct='%1.1f%%',
                   labeldistance=1.05, startangle=90)
            plt.gca().add_artist(my_circle)
            plt.show()

            return df

        elif currency == 'BTC':
            for coin in self.coins:
                value = coin.convertcoinBTC()*self.coins[coin]
                coinquantity.append(self.coins[coin])
                coinvalues.append(value)
                coins.append(coin.ticker)
                # add to total portfolio amount
                total = 0
                for i in coinvalues:
                    total += i
                print(f'{coin}: {value}')
            print(f'Total portfolio value: {total}')

            # coin list data frame
            df = pd.DataFrame(
                {'Coin': coins, 'Amount': coinquantity, 'Value BTC': coinvalues})
            df['Portfolio %'] = round((df['Value BTC']/sum(coinvalues)*100), 2)

            # Pie Chart (donut chart?)
            my_circle = plt.Circle((0, 0), 0.75, color='white')
            fig = plt.figure()
            ax = fig.add_axes([0, 0, 1, 1])
            ax.axis('equal')
            ax.pie(coinvalues, labels=coins, autopct='%1.1f%%',
                   labeldistance=1.05, startangle=90)
            plt.gca().add_artist(my_circle)
            plt.show()

            return df

        else:
            print('Sorry this currency is not currently supported.')
