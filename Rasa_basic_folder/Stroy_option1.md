## Generated Story 2799984315579697434
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_budgetfortwo
* restaurant_search{"budget": "3455"}
    - slot{"budget": "3455"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_emailrequired
    - utter_goodbye
    - export

