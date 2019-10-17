from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from Person import Restaurant
from Utils import Utils
import zomatopy
import json
import send_email

# re module provides support for regular expressions 
import re 

class ActionSearchRestaurants(Action):
	
	def name(self):
		return 'action_restaurant'

		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		zomato = zomatopy.initialize_app(config)
		budget = tracker.get_slot('budget')
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		query = "average_cost_for_two>100"

		restaurants = Utils.getRestaurants(lat, lon, cuisines_dict.get(cuisine), budget)
		
		# for restaurant in restaurants:
		# 	print(restaurant.name + " @ " + restaurant.address + " @ " + str(restaurant.avg_cost) + " @ " + restaurant.avg_ratng)

		filter_restaurants=restaurants[:5]

		response=""
		if len(filter_restaurants) == 0:
			response= "no results"
		else:
			for restaurant in filter_restaurants:
				response=response+ "Found "+ restaurant.name + " in "+restaurant.address + " with rating " + restaurant.avg_ratng + " with avg cost is " + str(restaurant.avg_cost) + "\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]




class ActionEmailSearchResults(Action):
	def name(self):
		return 'action_email_results'

	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		zomato = zomatopy.initialize_app(config)
		budget = tracker.get_slot('budget')
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1, 'chinese':25, 'north indian':50, 'italian':55, 'mexican': 73, 'south indian':85}
		
		restaurants = Utils.getRestaurants(lat, lon, cuisines_dict.get(cuisine), budget)
		filter_restaurants=restaurants[:10]
		response=""
		ctr=1
		if len(filter_restaurants) == 0:
			response= "no results"
		else:
			for restaurant in filter_restaurants:
				# response=response+ "Found "+ restaurant.name + " in "+restaurant.address + " with avg cost is " + str(restaurant.avg_cost) + "\n"
				response=response+ str(ctr)+". "+ restaurant.name + \
				"\n\tat "+restaurant.address+ \
				"\n\twith average cost for 2 at "+ str(restaurant.avg_cost) + \
				"\n\tand an average rating of "+restaurant.avg_ratng+"\n"
				#"\n\tand an average rating of "+restaurant.avg_ratng+"\n"
				ctr+=1
	
		
		email = send_email.initialize_app(config)
		sender = "chatbotrestaurant@gmail.com"
		receiver = "optimistvinay@gmail.com, hsatam@gmail.com"
		subject = "Top 10 Restaurants"
		msg = email.CreateMessage (sender, receiver, subject, response)

		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]


class ActionValidateCity(Action):
	def name(self):
		return 'action_validate_city'


	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		msg = ""

		X = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Ahmedabad', 'Pune']
		Y = ['Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum',  \
			 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bokaro Steel City', \
			 'Chandigarh', 'Coimbatore', 'Nagpur', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Erode', \
			 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', \
			 'Hubli–Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', \
			 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Kochi', 'Kottayam', 'Kolhapur', 'Kollam', 'Kota', 'Kozhikode', \
			 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', \
			 'Mysore', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Palakkad', 'Patna', 'Pondicherry', 'Purulia Allahabad', \
			 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Siliguri', 'Solapur', 'Srinagar', \
			 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirupati', 'Tirunelveli', 'Tiruppur', 'Tiruvannamalai', \
			 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai', 'Virar', 'Vijayawada', 'Vellore', 'Warangal', 'Surat', \
			 'Visakhapatnam']


		if (any(loc.lower() in s.lower() for s in X) or any(loc.lower() in t.lower() for t in Y)):
			msg = "Location Validated..."
		else:
			msg = "We do not operate in that area yet"
			loc = "None"

		print (msg)
		return [SlotSet('location',loc)]


class ActionValidateEmail(Action):
	def name(self):
		return 'action_validate_email'


	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email')

		email_check_pass = False

		# Make a regular expression for validating an Email 
		regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

		# pass the regualar expression and the string in search() method 
		if(re.search(regex,email)):
			email_check_pass = True
		else:
			email_check_pass = False
			print("Invalid Email, please re-enter email address")

		if (email_check_pass == True):
			return [SlotSet('email',email)]
		else:
			return [SlotSet('email',"None")]


class ActionValidateCuisine(Action):
	def name(self):
		return 'action_validate_cuisine'


	def run(self, dispatcher, tracker, domain):
		cuisine = tracker.get_slot('cuisine')
		msg = ""

		cuisineList = ['american', 'chinese', 'north indian', 'italian', 'mexican', 'south indian']

		if any(cuisine.lower() in s.lower() for s in cuisineList):
			msg = "Cuisine Validated..."
		else:
			msg = "We do not offer this cuisine yet"
			cuisine = "None"

		print (msg)
		return [SlotSet('cuisine',cuisine)]
