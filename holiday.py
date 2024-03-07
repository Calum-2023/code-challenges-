#holiday

""" task - calculate total holiday cost. including plane cost, hotel cost, car rental cost"""

'''set up functions at top of code to be called on later
hotel_cost - take num_nights as an argument and return a total cost for the hotel stay
plane_cost - take city_flight as an argument and return a cost for the flight
car_rental - take rental_days as an argument and return total cost of the car rental
holiday_cost - take hotel_cost, plane_cost and car_rental to return total cost of holiday

request input from users for information
We select the cost of hotel per night and car rental
'''

# set up functions at top of page so the can be called on in code
def calculate_hotel_cost(num_nights):
    total = nightly_cost * num_nights
    return total

# using if, elif to select the correct cost against city
def calculate_plane_cost(city_flight):
    if city_flight == "Paris":
        total = 400
    elif city_flight == "Rome":
        total = 450
    elif city_flight == "London":
        total = 200
    return total

def calculate_car_rental(rental_days):
    total = rental_cost * rental_days
    return total

# function to add the first 3 functions and get the desired output
def calculate_total_holiday_cost(x, y, z):
    total = x + y + z
    return total

# while loop to ensure the user is asked to re-enter input if a list item is not choosen 
while True:
    city_flight = input("Hello, please select a city to travel to. Paris, Rome, London: ")
    if city_flight in ["Paris", "London", "Rome"]:
        break  
    else:
        print("Sorry, your choice is not on our list. Please enter one of the cities listed.")

nightly_cost = 0  

if city_flight == "Paris":
    nightly_cost = 200
elif city_flight == "Rome":
    nightly_cost = 210
elif city_flight == "London":
    nightly_cost = 180

num_nights = (int(input("Please enter the number of nights you will be staying. for example: 5? ")))

rental_days = (int(input("Please enter the number of nights you will be hiring a car for. for example: 5? ")))
rental_cost = (int(80))

# functions are set to variables to enable them to be added together below
hotel_cost = calculate_hotel_cost(num_nights)
plane_cost = calculate_plane_cost(city_flight)
car_rental = calculate_car_rental(rental_days)

print(f"Your total holiday cost is: £{calculate_total_holiday_cost(hotel_cost, plane_cost, car_rental)}")
