## Generated Story 2365063693595693469
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_budgetfortwo
* restaurant_search{"budget": "845"}
    - slot{"budget": "845"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_goodbye
    - export

