
# price of the most expensive jeans
print (jeans['price'].max())

# brand for the most expensive jeans
print (jeans['brand'][jeans['price'] == jeans['price'].max()])

# price of the cheapest jeans
print (jeans['price'].min())

# brand for the cheapest jeans
print (jeans['brand'][jeans['price'] == jeans['price'].min()])

# difference in price
print(jeans['price'].max() - jeans['price'].min())
