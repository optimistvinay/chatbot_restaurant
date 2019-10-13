import pprint, json
import zomatopy

# specify location and cuisine
loc = 'Bangalore'
cuisine = 'Italian'

# provide API key and initialise a 'zomato app' object
config={ "user_key": your_api_key_as_a_string_here}
zomato = zomatopy.initialize_app(config)

# get_location gets the lat-long coordinates of 'loc'
location_detail=zomato.get_location(loc, 1)

# store retrieved data as a dict
d1 = json.loads(location_detail)

# separate lat-long coordinates
lat=d1["location_suggestions"][0]["latitude"]
lon=d1["location_suggestions"][0]["longitude"]

# cuisines code (used by zomatopy)
cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}

# fetch and print results
results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
d = json.loads(results)
pprint.pprint(d)