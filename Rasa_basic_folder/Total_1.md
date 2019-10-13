## Generated Story -328171842211990278
* greet
    - utter_greet
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_budgetfortwo
* restaurant_search{"budget": "345"}
    - slot{"budget": "345"}
    - action_restaurant
    - slot{"location": "delhi"}
    - export

