## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - action_validate_city
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - utter_ask_emailaddress
    - slot{"email": "a@b.com"}
    - action_validate_email
    - action_email_results
    - slot{"location": "delhi"}
* goodbye
    - utter_goodbye

## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - action_validate_city
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_restaurant
    - utter_ask_emailaddress
    - slot{"email": "a@b.com"}
    - action_validate_email
    - action_email_results
* goodbye
    - utter_goodbye

## Generated Story 3320800183399695936
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - action_validate_city
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - utter_ask_emailaddress
    - slot{"email": "a@b.com"}
    - action_validate_email
    - action_email_results
* goodbye
    - utter_goodbye

## Generated Story -4639179087166749998
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - action_validate_city
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_emailaddress
    - slot{"email": "a@b.com"}
    - action_validate_email
    - action_email_results
* goodbye
    - utter_goodbye

## Generated Story 4963448062290237512
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - utter_ask_emailaddress
    - slot{"email": "a@b.com"}
    - action_validate_email
    - action_email_results
* goodbye
    - utter_goodbye

## Generated Story -1654582313191882359
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_budgetfortwo
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_emailrequired
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - utter_ask_emailaddress
* capture_email_address{"email": "hsatam@gmail.com"}
    - slot{"email": "hsatam@gmail.com"}
    - action_validate_email
    - slot{"email": "hsatam@gmail.com"}
    - action_email_results
    - slot{"location": "pune"}
    - utter_goodbye
    - export