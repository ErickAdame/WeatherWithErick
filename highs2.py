#!/usr/bin/env python
# coding: utf-8

# In[17]:


import matplotlib.pyplot as plt
import requests
from scipy import stats
import pandas as pd
from config import tomorrowio_api_key
import numpy as np
from scipy.interpolate import interp1d
from datetime import datetime
from datetime import timedelta 
import matplotlib.dates as mdates
import pytz
import calendar
from config import weather_api_key


# In[18]:
#https://api.weatherapi.com/v1/forecast.json?key=d8b2f077395849fe835230451230205&q=new%20york&days=7

city_list = ["new york", "los angeles", "grand rapids", "chicago", "charlotte", "fort lauderdale"]

city = input("Enter City: ").lower()

geo_url = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "&appid=" + weather_api_key

lat_lon = requests.get(geo_url).json()
    #print(geo_url)

lat = str(lat_lon[0]["lat"])
lon = str(lat_lon[0]["lon"])


# In[19]:


#url = "https://api.tomorrow.io/v4/timelines?"
url = "https://api.weatherapi.com/v1/forecast.json?key=d8b2f077395849fe835230451230205&days=8"
# city = "New York"
#fields = "temperatureMax"
#timesteps = "1d"
#units = "imperial"
# lon = "-73.9656"
# lat = "40.7826"

final_url = f"{url}&q={lat},{lon}"



# In[20]:


forecast = requests.get(final_url).json()
#forecast['data']['timelines'][0]['intervals'][0]['startTime']
forecast['forecast']['forecastday'][0]['day']['maxtemp_f']


# In[21]:


high_temps = []
low_temps = []
time_stamp = []
ts = []





for day in range(1,8):
    max_temp = forecast['forecast']['forecastday'][day]['day']['maxtemp_f']
    max_temp = round(max_temp)
    high_temps.append(max_temp)
    min_temp = forecast['forecast']['forecastday'][day]['day']['mintemp_f']
    min_temp = round(min_temp)
    low_temps.append(min_temp)
    

    
# for time in time_stamp:
#     ts.append(datetime.fromtimestamp(time).strftime("%a"))


# In[51]:


weekday = []

for x in range(1,8):
    dt = datetime.now() + timedelta(days=x)
    day = dt.strftime('%a').upper()
    weekday.append(day)
    
weekday


# In[52]:


five_day= pd.DataFrame({
    "Date": weekday,
     "High Temp": high_temps,
    "Low Temp": low_temps
})



# dt = datetime.now()
# x = dt.weekday()
# d = datetime.now().date()
# today = d.strftime('%w')
# today
# five_day = five_day.drop(index=0)
# five_day = five_day.reset_index()
five_day.to_csv(f'{city}_7_day_forecast.csv')


# In[65]:


x = five_day["Date"]
y = five_day["High Temp"]
plt.rcParams['font.family'] = ['sans', 'bold']
plt.rcParams["axes.spines.top"]=False
plt.rcParams["axes.spines.right"]=False
plt.rcParams["axes.spines.left"]=False
fig = plt.figure(figsize = (12, 5))


def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i,y[i],y[i], ha="center", color="white", size="35", va="bottom")

plt.bar(x, y, color="blue", width=0.7, alpha=0.75)
addlabels(x,y)
# plt.ylabel("High Temperature")
plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = True, bottom = False)
plt.xticks(size=30, color="white")
# plt.title(f"{city.upper()}", size="24", color="white")
plt.ylim([0, five_day["High Temp"].max()+10])
#plt.savefig("5_Day_Forecast.png", transparent = True)


# In[66]:


plt.savefig(f"{city}_7_Day_Forecast.png", transparent=True)

