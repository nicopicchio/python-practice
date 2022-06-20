# Index is calculated by :
#   - Get current US Big Mac price
#   - Get current Big Mac price from country we're comparing
#   - Divide US Big Mac price by country's Big Mac price
#     (this is called the implied purchasing power)
#   - Get country's currency rate to USD value
#   - Substract currency rate with the implied purchasing power
#   - Divide the previous result by the implied purchasing power
#   - This will give you the Big Mac Index

# For example, using figures in July 2008:
#   - the price of a Big Mac was $3.57 in the United States 
#   - the price of a Big Mac was £2.29 in the United Kingdom 
#   - the implied purchasing power parity was $1.56 to £1, that is $3.57/£2.29 = 1.56
#   - this compares with an actual exchange rate of $2.00 to £1 at the time
#   - (2.00 – 1.56) / 1.56 = 28%
#   - the pound was thus overvalued against the dollar by 28%


US_Big_Mac_Price = float(3.99)
comparison_country_Big_Mac_price = float(input('Enter Big Mac price in your country: '))
IPP = float(US_Big_Mac_Price / comparison_country_Big_Mac_price)
currency_rate_to_USD = float(input('Enter your country\'s currency rate against USD: '))

def calculate_currency_valuation(currency_rate, IPP):
  result = round(((currency_rate - IPP) / IPP) * 100, 1)
  if result < 0:
    print(f'Your country\'s currency is undervalued by {-result}%')
  elif result > 0:
    print(f'Your country\'s currency is overvalued by {result}%')
  else:
    print('Your country\'s currency is fairly valued')

calculate_currency_valuation(currency_rate_to_USD, IPP)
