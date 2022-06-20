# Calculate train ticket price knowing that:
# Tickets cost $0.21/km
# Customers up to 18yo get 20% discount
# Customers over 65yo get 40% discount

try: 
  customer_age = int(input('Enter age: '))
except ValueError:
  print('Enter age in a valid format')

try:
  travel_distance = float(input('Enter travel distance: '))
except ValueError:
  print('Enter travel distance in a valid format, i.e. 10.4')

price_per_km = float(0.21)
junior_age = int(18)
senior_age = int(65)
junior_discount = float(0.8)
senior_discount = float(0.6)

ticket_cost = round(travel_distance * price_per_km, 2)

if customer_age < junior_age:
  print(f'Ticket price is ${round(ticket_cost * junior_discount, 2)}')
elif customer_age > senior_age:
  print(f'Ticket price is ${round(ticket_cost * senior_discount, 2)}')
else:
  print(f'Ticket price is ${ticket_cost}')
  