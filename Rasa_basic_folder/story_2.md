## Generated Story 2932243098583838370
* greet
    - utter_greet
* restaurant_search{"location": "bandra"}
    - slot{"location": "bandra"}
    - action_validate_city
    - slot{"location": "None"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetfortwo
* restaurant_search{"budget": "large"}
    - slot{"budget": "large"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - utter_ask_emailaddress
* restaurant_search
    - action_email_results
    - slot{"location": "Mumbai"}
    - utter_goodbye
    - export

