currencies = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency_selected = input("Please enter a currency to check:")
print(currencies.get(currency_selected,"The currency selected is not present"))