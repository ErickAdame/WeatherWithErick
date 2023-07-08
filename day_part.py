#!/usr/bin/env python
# coding: utf-8

# In[187]:


import matplotlib.pyplot as plt
import requests
import pandas as pd
from config import weather_api_key
from datetime import datetime
import matplotlib.dates as mdates


# In[188]:



# In[3]:


city_list = ["new york", "los angeles", "grand rapids", "fort lauderdale", "san diego"]

url = "https://api.openweathermap.org/data/2.5/forecast"
units = "imperial"

url_list = []

for city in city_list:
    city=city

    geo_url = "http://api.openweathermap.org/geo/1.0/direct?q=" + city + "&appid=" + weather_api_key
    lat_lon = requests.get(geo_url).json()
    #print(geo_url)

    lat = str(lat_lon[0]["lat"])
    lon = str(lat_lon[0]["lon"])
    final_url = url + "?lat=" + lat + "&lon=" + lon + "&units=" + units + "&appid=" + weather_api_key
    url_list.append(final_url)


# In[ ]:





# In[189]:


city_1 = url_list[0]
forecast = requests.get(city_1).json()
 
c1_hourly_temp = []
c1_rain_chance= []
c1_time_stamp = []
c1_weather = []

for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c1_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c1_hourly_temp.append(round(temp))
    c1_time_stamp.append(forecast['list'][hour]['dt_txt'])
    c1_weather.append(forecast['list'][hour]['weather'][0]['description'])
    
c1_dates = []
c1_times = []

for timestamp in c1_time_stamp:
    date, time = timestamp.split()
    c1_dates.append(date)
    c1_times.append(time)


# In[190]:


city_2 = url_list[1]
forecast = requests.get(city_2).json()
 
c2_hourly_temp = []
c2_rain_chance= []
c2_time_stamp = []
c2_weather = []

for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c2_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c2_hourly_temp.append(round(temp))
    c2_time_stamp.append(forecast['list'][hour]['dt_txt'])
    c2_weather.append(forecast['list'][hour]['weather'][0]['description'])
    
c2_dates = []
c2_times = []

for timestamp in c2_time_stamp:
    date, time = timestamp.split()
    c2_dates.append(date)
    c2_times.append(time)


# In[191]:


city_3 = url_list[2]
forecast = requests.get(city_3).json()
 
c3_hourly_temp = []
c3_rain_chance= []
c3_time_stamp = []
c3_weather = []

for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c3_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c3_hourly_temp.append(round(temp))
    c3_time_stamp.append(forecast['list'][hour]['dt_txt'])
    c3_weather.append(forecast['list'][hour]['weather'][0]['description'])
    
c3_dates = []
c3_times = []

for timestamp in c3_time_stamp:
    date, time = timestamp.split()
    c3_dates.append(date)
    c3_times.append(time)


# In[192]:

city_4 = url_list[3]
forecast = requests.get(city_4).json()
 
c4_hourly_temp = []
c4_rain_chance= []
c4_time_stamp = []
c4_weather = []

for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c4_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c4_hourly_temp.append(round(temp))
    c4_time_stamp.append(forecast['list'][hour]['dt_txt'])
    c4_weather.append(forecast['list'][hour]['weather'][0]['description'])
    
c4_dates = []
c4_times = []

for timestamp in c4_time_stamp:
    date, time = timestamp.split()
    c4_dates.append(date)
    c4_times.append(time)

city_5 = url_list[4]
forecast = requests.get(city_5).json()
 
c5_hourly_temp = []
c5_rain_chance= []
c5_time_stamp = []
c5_weather = []

for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c5_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c5_hourly_temp.append(round(temp))
    c5_time_stamp.append(forecast['list'][hour]['dt_txt'])
    c5_weather.append(forecast['list'][hour]['weather'][0]['description'])
    
c5_dates = []
c5_times = []

for timestamp in c5_time_stamp:
    date, time = timestamp.split()
    c5_dates.append(date)
    c5_times.append(time)


# In[193]:


df = pd.DataFrame({
    "Data Time": c1_time_stamp,
    "nyc wx": c1_weather,
    "nyc temp": c1_hourly_temp,
    "lax wx": c2_weather,
    "lax temp": c2_hourly_temp,
    "grr wx": c3_weather,
    "grr temp": c3_hourly_temp,
    "fll wx": c4_weather,
    "fll temp": c4_hourly_temp,
    "san wx": c5_weather,
    "san temp": c5_hourly_temp

})


# In[194]:


dt = datetime.now()+ pd.Timedelta("1 day")
start_time = dt.replace(hour=6, minute=0)
end_time = start_time+ pd.Timedelta("24 hours")


# In[195]:



df["Data Time"] = pd.to_datetime(df['Data Time'].astype(str))

mask = (df['Data Time'] > start_time) & (df['Data Time'] <= end_time)

df = df.loc[mask]
df = df.set_index("Data Time")
df = df.transpose()
df


# In[196]:


df.to_csv('day_part_data.csv')


# In[113]:





# In[ ]:





# In[ ]:





# In[ ]:




