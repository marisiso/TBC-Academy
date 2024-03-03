from datetime import datetime
import requests
import forex_python
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
purchase_date = input('Please type purchase date (dd/mm/yyyy): ')
purchase_price = int(input('How much did you pay in USD?: '))

b = BtcConverter() # force_decimal=True to get Decimal rates
current_price = b.get_latest_price('USD')
date_object = datetime.strptime(purchase_date, "%d/%m/%Y")
old_price = b.get_previous_price('USD', date_object)

amount_owned = purchase_price / old_price

current_value = amount_owned * current_price

net_income = current_value - purchase_price
print('You have won $ ', net_income)

