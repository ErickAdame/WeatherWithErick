#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json

# Base URL for GET requests to retrieve number/date facts
url = "http://numbersapi.com/"

still_playing="yes"

while still_playing == "yes":
    
    adventure_type = input("Which would you like to try today: Trivia, Math, or Date? ")



    if adventure_type.lower() == "math":
        url_add = input("Ok!, Pick a number: ")
    elif adventure_type.lower() =="date":
        url_add = input("Ok!, Pick a date in this format (mm/dd): ")
    else:
        url_add = "random/trivia"
    
    final_url = url+url_add+"?json"

    response = requests.get(final_url).json()

    print("-----------------------------------------")
    print(response["text"])
    print("-----------------------------------------")
    
    still_playing =input("Would you like to play again? ").lower()


# In[ ]:





# In[ ]:





# In[ ]:




