# cafe

""" 
Task 
create a list of at least 4 menu items 
detail the stock of each item
detail the cost of each item
calculate the total cost of the stock in the cafe
"""

'''
Process
create a list of the menu items
create a dictionary containing the stock of each item
create a dictionary containing the cost of each item
work out the amount of stock and cost of each item to give the total value of the stock'''

# set ip menu list
menu = ["Coffee", "Tea", "Water", "Orange"]

# stock dictionary 
stock = {}
# for loop to cycle throuhg the list and pick up the items for the dictionary 
for i in range (len(menu)):
    stock[i] = menu[i]
# amend the dictionary items to show current stock
stock = {"Coffee":5, "Tea":6, "Water":10, "Orange":2}

# item price dictionary
price = {}
# for loop to cycle through the list and pick up the items for the dictionary
for j in range (len(menu)):
    price[j] = menu[j]
#amend the dictionary to have the current value of items 
price = {"Coffee":4, "Tea":4, "Water":2, "Orange":3}

# new dictionary to show the value of stock 
stock_value = {}
#setting up a for loop to cycle through each item in each dictionary 
for key1, value1 in stock.items():
    # if statement to multiply the stock and price
    if key1 in price:
        stock_value[key1] = value1 * price[key1]

print (f"Stock value is:\nCoffee: £{stock_value['Coffee']} \nTea: £{stock_value['Tea']} \nWater: £{stock_value['Water']} \nOrange: £{stock_value['Orange']}")

