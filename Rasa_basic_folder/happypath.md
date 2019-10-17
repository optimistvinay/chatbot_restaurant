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

