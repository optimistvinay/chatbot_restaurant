from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from Person import Restaurant
import zomatopy
import json

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'

	#def filter_budget_data(self, restaurants):


	

		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		zomato = zomatopy.initialize_app(config)
		budget = tracker.get_slot('budget')
		print(budget)
		loc = tracker.get_slot('location')
		print("Location : ", loc)
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		query = "average_cost_for_two>100"

		restaurants = []
		for index in range(0,7):
			print("Index : ",index)
			if index == 0:
				starting_index =0
			else:
				starting_index =str(index *20)
			print(starting_index)
			restaurant=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),starting_index, 20)
			restaurantJSON = json.loads(restaurant)
			print("Length : ",len(restaurantJSON['restaurants']))
			i=0
			while i<len(restaurantJSON['restaurants']):
				print("i = ", i)
				#print(restaurantJSON['restaurants'][i])
				print ('-'*80)
				#print("Name             : ", restaurantJSON['restaurants'][i]['restaurant']['name'])
				name = restaurantJSON['restaurants'][i]['restaurant']['name']
				#print("Address          : ", restaurantJSON['restaurants'][i]['restaurant']['location']['address'])
				address = restaurantJSON['restaurants'][i]['restaurant']['location']['address']
				#print("City             : ", restaurantJSON['restaurants'][i]['restaurant']['location']['city'])
				city = restaurantJSON['restaurants'][i]['restaurant']['location']['city']
				# print("Locality         : ", restaurantJSON['restaurants'][i]['restaurant']['location']['locality_verbose'])

				# print('\n')
				# print("Cuisines         : ", restaurantJSON['restaurants'][i]['restaurant']['cuisines'])
				cuisines = restaurantJSON['restaurants'][i]['restaurant']['cuisines']
				establishments = ','.join(string for string in restaurantJSON['restaurants'][i]['restaurant']['establishment'])
				# print("Establishment    : ", establishments)
				
				avg_cost = restaurantJSON['restaurants'][i]['restaurant']['average_cost_for_two']
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
			print(rest.name + " is having " + str(rest.avg_cost))
		print ('*'*80)

		if int(budget) < 300:
			budget = "min limit"
		elif 300 < int(budget) < 700:
			budget = "mid range"
		else:
			budget="max limit"

		print("budget : ", budget)

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
		print("Sorting is done !!!")

		print(len(filter_restaurants))
		for rest in filter_restaurants:
			print(rest.name + " is having avg cost " + str(rest.avg_cost) + " & avg ratting " + str(rest.avg_ratng))
		print ('*'*80)

		#results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)
		#print(results)
		#d = json.loads(results)

		#restaurants = filter_budget_data(restaurants)
		filter_restaurants=filter_restaurants[:5]

		response=""
		if len(filter_restaurants) == 0:
			response= "no results"
		else:
			for restaurant in filter_restaurants:
				# avg_cost = restaurant['restaurant']['average_cost_for_two']
				# print(avg_cost)
				#response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
				response=response+ "Found "+ restaurant.name + " in "+restaurant.address + " with avg cost is " + str(restaurant.avg_cost) + "\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

class ActionEmailSearchResults(Action):
	def name(self):
		return 'email_results'

	def run(self, dispatcher, tracker, domain):
		return "TO BE IMPLEMENTED..."