# Creates an instance of the Portfolio class  based on user input
user = Portfolio(str(input('Portfolio Name:')), str(
    input('Preferred Currency: $/£/BTC')), int(input('Fiat invested:')))
# Allows user to add coins (would like to create a GUI for this, with 'add coins' & 'show overview' buttonss)
add = user.addcoins(input('Coin Name:'), int(input('Quantity')))
showoverview = user.overview(str(input('Select Currency: USD/GBP/BTC')))
