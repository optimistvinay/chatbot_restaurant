import requests
import json


base_url = "https://developers.zomato.com/api/v2.1/"
user_key = "6ce88a5ec1419e335afa1c7f92f4b739"

params = {}
params['aggregate_rating'] = 4

headers = {'Accept': 'application/json', 'user-key': user_key}
#results = (requests.get(base_url + "/search?q='aggregate_rating=4'", headers=headers).content).decode("utf-8")
results = (requests.get("https://developers.zomato.com/api/v2.1/search?entity_id=3&sort=restaurants.restaurant.average_cost_for_two&order=desc", headers=headers).content).decode("utf-8")
#rint (base_url + "/search?q='aggregate_rating<=4'", headers)

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
