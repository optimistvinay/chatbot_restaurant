import zomatopy
import json

config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
zomato = zomatopy.initialize_app(config)
loc = 'Mumbai'
cuisine = 'Chinese'
location_detail=zomato.get_location(loc, 1)
d1 = json.loads(location_detail)
lat=d1["location_suggestions"][0]["latitude"]
lon=d1["location_suggestions"][0]["longitude"]
cuisines_dict={'american':1, 'chinese':25, 'north indian':50, 'italian':55, 'mexican': 73, 'south indian':85}

results=zomato.restaurant_L3("average_cost_for_two=300", lat, lon, str(cuisines_dict.get(cuisine)), 5, "desc")
d = json.loads(results)
response=""
ctr=1
if d['results_found'] == 0:
	response= "no results"
else:
	for restaurant in d['restaurants']:
		response=response+ str(ctr)+". "+ restaurant['restaurant']['name']+ \
		"\n\tin "+restaurant['restaurant']['location']['locality_verbose']+ \
		"\n\tat "+restaurant['restaurant']['location']['address']+ \
		"\n\twith average cost for 2 at "+restaurant['restaurant']['currency']+" "+str(restaurant['restaurant']['average_cost_for_two'])+ \
		"\n\tand an average rating of "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n"
		ctr+=1

print (response)
