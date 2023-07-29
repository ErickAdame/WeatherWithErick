#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import requests
from scipy import stats
import pandas as pd
from config import weather_api_key
import numpy as np
from scipy.interpolate import interp1d
from datetime import datetime
import matplotlib.dates as mdates
import pytz
import calendar


# In[4]:


#https://api.tomorrow.io/v4/timelines?location=40.7826,-73.9656&fields=temperatureMax&timesteps=1d&units=imperial&apikey=zRS3qwSdR9IB4wB0GLvTJYkeMGoehvrL
url = "https://api.openweathermap.org/data/2.5/forecast"
#city = "New York"
#cnt = "8" #number of forecast days
units = "imperial"
lon = "-73.9656"
lat = "40.7826"
#https://api.openweathermap.org/data/2.5/forecast/daily?lat=40.7826&lon=-73.9656&cnt=7&units=imperial&appid=155db15cf89682a55503d94f25dc4deb

final_url = url + "?lat=" + lat + "&lon=" + lon + "&units=" + units + "&appid=" + weather_api_key



# In[5]:


forecast = requests.get(final_url).json()


# In[6]:


dt = datetime.now()+ pd.Timedelta("1 day")
start_time = dt.replace(hour=6, minute=0)
end_time = start_time+ pd.Timedelta("1 day")


# In[45]:


rain_chance = []
time_stamp = []
ts = []





for hour in range(15):
    rain = forecast['list'][hour]['pop']
#     rain = round(rain*100)
    rain_chance.append(rain)
    time_stamp.append(forecast['list'][hour]['dt'])  

    
for time in time_stamp:
#     if datetime.fromtimestamp(time) >= start_time and datetime.fromtimestamp(time) <= end_time:
        ts.append(datetime.fromtimestamp(time))
    


# In[ ]:





# In[99]:


df= pd.DataFrame({
    "Date": ts,
    "Rain Chance": rain_chance,
})




df["Date"] = pd.to_datetime(df['Date'].astype(str))

mask = (df['Date'] > start_time) & (df['Date'] <= end_time)

df = df.loc[mask]
df["Date"] = df["Date"].dt.strftime('%-I%p')
df


# In[ ]:



    


# In[100]:



import matplotlib.ticker as mtick

x = df["Date"]
y = df["Rain Chance"]
fig = plt.figure(figsize = (12, 5))


barplot = plt.bar(x,y, color='Green')
plt.bar_label(barplot, labels=[f'{x:.0%}' for x in barplot.datavalues], label_type="edge", padding=3, color="White", size=25)
plt.ylim(0,1.2)



plt.title("TODAY'S RAIN CHANCES", color='white', size=40)
plt.xticks(color='white', size=20)
plt.yticks([])
plt.savefig("Hourly_Rain.png", transparent = True)


# In[ ]:





# In[ ]:




