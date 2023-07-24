#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


url = "https://api.tomorrow.io/v4/timelines?"
city = "New York"
fields = "temperatureMax"
timesteps = "1d"
units = "imperial"
lon = "-73.9656"
lat = "40.7826"

final_url = url + "location=" + lat + "," + lon + "&fields=" + fields + "&timesteps=" + timesteps + "&units=" + units + "&apikey=" + tomorrowio_api_key
print(final_url)


# In[3]:


forecast = requests.get(final_url).json()
forecast['data']['timelines'][0]['intervals'][0]['startTime']


# In[4]:


high_temps = []
time_stamp = []
ts = []





for day in range(1,8):
    max_temp = forecast['data']['timelines'][0]['intervals'][day]['values']['temperatureMax']
    max_temp = round(max_temp)
    high_temps.append(max_temp)
    time_stamp.append(forecast['data']['timelines'][0]['intervals'][day]['startTime'])


weekday = []

for x in range(1,8):
    dt = datetime.now() + timedelta(days=x)
    day = dt.strftime('%a')
    weekday.append(day)
    


five_day= pd.DataFrame({
    "Date": weekday,
    "High Temp": high_temps
})


# In[9]:


x = five_day["Date"]
y = five_day["High Temp"]

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i], ha="center", color="white", size="24", va="bottom")

plt.bar(x, y, color="darkblue", width=0.5, alpha=0.75)
addlabels(x,y)
# plt.ylabel("High Temperature")
plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = True, bottom = False)
plt.xticks(size=18, color="darkblue")
plt.ylim([0, five_day["High Temp"].max()+10])
plt.savefig("tomorrow.io_7day.png", format='png', transparent = True)




