# sample code to fetch a list of restaurants using zomatopy

import pprint, json
import zomatopy
from Person import Restaurant


p1 = Restaurant("John", 36,'w','r','t')
print(p1.name)

# specify location and cuisine
loc = 'Gandhinagar'
cuisine = 'American'

print ('*'*80)

# provide API key and initialise a 'zomato app' object
config={ "user_key": "a62d4116984f1c5caae3ad4ccdc06f5b"}
zomato = zomatopy.initialize_app(config)

# get_location gets the lat-long coordinates of 'loc'
location_detail=zomato.get_location(loc, 1)

# store retrieved data as a dict
d1 = json.loads(location_detail)

# separate lat-long coordinates
lat=d1["location_suggestions"][0]["latitude"]
lon=d1["location_suggestions"][0]["longitude"]

# cuisines code (used by zomatopy)
cuisines_dict={'chinese':25, 'mexican':73, 'italian':55, 'american':1, 'south indian':85, 'north indian':50}

# fetch and print restaurant details
#restaurantJSON = {}
restaurants = []
for index in range(0,7):
	print("Index : ",index)
	if index == 0:
		starting_index =0
	else:
		starting_index =str(index *20)
	print(starting_index)
	restaurant=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),starting_index, 10)
	restaurantJSON = json.loads(restaurant)
	print("Length : ",len(restaurantJSON['restaurants']))
	i=0
	while i<len(restaurantJSON['restaurants']):
		print("i = ", i)
		#print(restaurantJSON['restaurants'][i])
		print ('-'*80)
		print("Name             : ", restaurantJSON['restaurants'][i]['restaurant']['name'])
		name = restaurantJSON['restaurants'][i]['restaurant']['name']
		print("Address          : ", restaurantJSON['restaurants'][i]['restaurant']['location']['address'])
		address = restaurantJSON['restaurants'][i]['restaurant']['location']['address']
		print("City             : ", restaurantJSON['restaurants'][i]['restaurant']['location']['city'])
		city = restaurantJSON['restaurants'][i]['restaurant']['location']['city']
		print("Locality         : ", restaurantJSON['restaurants'][i]['restaurant']['location']['locality_verbose'])

		print('\n')
		print("Cuisines         : ", restaurantJSON['restaurants'][i]['restaurant']['cuisines'])
		cuisines = restaurantJSON['restaurants'][i]['restaurant']['cuisines']
		establishments = ','.join(string for string in restaurantJSON['restaurants'][i]['restaurant']['establishment'])
		print("Establishment    : ", establishments)
		
		# table_booking = restaurantJSON['restaurants'][i]['restaurant']['has_table_booking']
		# if (table_booking == 0):
		# 	print("Has Table Booking:  No")
		# else:
		# 	print("Has Table Booking:  Yes")

		# try:
		# 	print("URL to Book      : ", restaurantJSON['restaurants'][i]['restaurant']['book_url'])
		# except:
		# 	print("URL to Book      :  None")

		# print("Price Range      : ", restaurantJSON['restaurants'][i]['restaurant']['price_range'])

		#avg_cost = restaurantJSON['restaurants'][i]['restaurant']['currency'] + " " + str(restaurantJSON['restaurants'][i]['restaurant']['average_cost_for_two'])
		avg_cost = restaurantJSON['restaurants'][i]['restaurant']['average_cost_for_two']

		# print("Avg Cost for two : ", avg_cost)
		# print('\n')
		# print("Aggregare Rating : ", restaurantJSON['restaurants'][i]['restaurant']['user_rating']['aggregate_rating'])
		# print("Rating Text      : ", restaurantJSON['restaurants'][i]['restaurant']['user_rating']['rating_text'])
		avg_ratng = restaurantJSON['restaurants'][i]['restaurant']['user_rating']['aggregate_rating']
		restaurant = Restaurant(name, address, cuisines, avg_cost, avg_ratng)
		restaurants.append(restaurant)
		#print("Votes            : ", restaurantJSON['restaurants'][i]['restaurant']['user_rating']['votes'])
		print ('-'*80)
		print('\n\n')
		i += 1

print ('*'*80)
print(len(restaurants))
for rest in restaurants:
	print(rest.avg_cost)
	print(rest.name)
print ('*'*80)

	# print(restaurantJSON.keys())
	# print("results_found : "+ str(restaurantJSON['results_found']))


# table_booking = 0
# avg_cost = ""
# i=0
# print(restaurantJSON)
# while i<5:
# 	print("i = ", i)
# 	print ('-'*80)
# 	print("Name             : ", restaurantJSON['restaurants'][i]['restaurant']['name'])
# 	print("Address          : ", restaurantJSON['restaurants'][i]['restaurant']['location']['address'])
# 	print("City             : ", restaurantJSON['restaurants'][i]['restaurant']['location']['city'])
# 	print("Locality         : ", restaurantJSON['restaurants'][i]['restaurant']['location']['locality_verbose'])
# 	print('\n')
# 	print("Cuisines         : ", restaurantJSON['restaurants'][i]['restaurant']['cuisines'])
	
# 	establishments = ','.join(string for string in restaurantJSON['restaurants'][i]['restaurant']['establishment'])
# 	print("Establishment    : ", establishments)
	
# 	table_booking = restaurantJSON['restaurants'][i]['restaurant']['has_table_booking']
# 	if (table_booking == 0):
# 		print("Has Table Booking:  No")
# 	else:
# 		print("Has Table Booking:  Yes")

# 	try:
# 		print("URL to Book      : ", restaurantJSON['restaurants'][i]['restaurant']['book_url'])
# 	except:
# 		print("URL to Book      :  None")

# 	print("Price Range      : ", restaurantJSON['restaurants'][i]['restaurant']['price_range'])

# 	avg_cost = restaurantJSON['restaurants'][i]['restaurant']['currency'] + " " + str(restaurantJSON['restaurants'][i]['restaurant']['average_cost_for_two'])
# 	print("Avg Cost for two : ", avg_cost)
# 	print('\n')
# 	print("Aggregare Rating : ", restaurantJSON['restaurants'][i]['restaurant']['user_rating']['aggregate_rating'])
# 	print("Rating Text      : ", restaurantJSON['restaurants'][i]['restaurant']['user_rating']['rating_text'])
# 	print("Votes            : ", restaurantJSON['restaurants'][i]['restaurant']['user_rating']['votes'])
# 	print ('-'*80)
# 	print('\n\n')
# 	i += 1
