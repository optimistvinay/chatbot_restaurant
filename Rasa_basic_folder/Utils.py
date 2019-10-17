from Person import Restaurant
import zomatopy
import json
import send_email

class Utils:

	@staticmethod
	def getRestaurants(lat, lon, cuisine, budget):

		print("****** getRestaurants *******")
		config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		zomato = zomatopy.initialize_app(config)
		restaurants = []
		for index in range(0,7):
			print("Index : ",index)
			if index == 0:
				starting_index =0
			else:
				starting_index =str(index *20)
			#print(starting_index)
			restaurant=zomato.restaurant_search("", lat, lon, str(cuisine),starting_index, 20)
			restaurantJSON = json.loads(restaurant)
			#print("Length : ",len(restaurantJSON['restaurants']))
			i=0
			while i<len(restaurantJSON['restaurants']):
				
				name = restaurantJSON['restaurants'][i]['restaurant']['name']
				address = restaurantJSON['restaurants'][i]['restaurant']['location']['address']
				city = restaurantJSON['restaurants'][i]['restaurant']['location']['city']
				cuisines = restaurantJSON['restaurants'][i]['restaurant']['cuisines']
				establishments = ','.join(string for string in restaurantJSON['restaurants'][i]['restaurant']['establishment'])
				
				avg_cost = restaurantJSON['restaurants'][i]['restaurant']['average_cost_for_two']
				avg_ratng = restaurantJSON['restaurants'][i]['restaurant']['user_rating']['aggregate_rating']
				print("avg_ratng : ", str(avg_ratng))
				restaurant = Restaurant(name, address, cuisines, avg_cost, avg_ratng)
				restaurants.append(restaurant)
				i += 1
		#This needs to be removed after gettng te value
		# budget = "max limit"
		filter_restaurants =[]
		for rest in restaurants:
			if budget == "min limit":
				if rest.avg_cost < 300:
					filter_restaurants.append(rest)
			elif budget == "mid range":
				if 300 < rest.avg_cost < 700:
					filter_restaurants.append(rest)
			elif budget == "max limit":
				if 700 < rest.avg_cost:
					filter_restaurants.append(rest)

		filter_restaurants = sorted(filter_restaurants, key=lambda x: x.avg_ratng, reverse=True)

		return filter_restaurants