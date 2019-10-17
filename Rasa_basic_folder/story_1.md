## Generated Story -867394963678418578
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - action_validate_city
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budgetfortwo
* restaurant_search{"budget": "large"}
    - slot{"budget": "large"}
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_emailaddress
* restaurant_search
    - action_email_results
    - slot{"location": "Bangalore"}
    - utter_goodbye
    - export

