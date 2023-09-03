#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import requests
import pandas as pd
from config import weather_api_key
from datetime import datetime
import matplotlib.dates as mdates


# In[2]:


city_list = ["new york", "los angeles", "grand rapids", "fort lauderdale", "san diego"]


# In[3]:


url = "https://api.weatherbit.io/v2.0/forecast/hourly"
key = "85a65933d3894f0d9c7194ffa8098565"
units = "&units=I"
url_list = []

def clean_timestamp(timestamp):
    # Parse the input timestamp string into a datetime object
    dt_obj = datetime.fromisoformat(timestamp.replace('T', ' '))

    # Format the datetime object as "8/5/23 12pm"
    formatted_str = dt_obj.strftime('%-m/%-d/%y %I%p')

    return formatted_str


# In[4]:


for city in city_list:
    city = city.lower()

    url = "https://api.weatherbit.io/v2.0/forecast/hourly"
    key = "85a65933d3894f0d9c7194ffa8098565"
    units = "&units=I"

    final_url = f"{url}?city={city}{units}&key={key}"
    url_list.append(final_url)
    


# In[ ]:





# In[5]:


city_1 = url_list[0]
forecast = requests.get(city_1).json()
 
c1_hourly_temp = []
c1_rain_chance= []
c1_time_stamp = []
c1_weather = []


for hour in range(48):
    rain = forecast['data'][hour]['pop']
    c1_rain_chance.append(round(rain*100))
    temp = forecast['data'][hour]['temp']
    c1_hourly_temp.append(round(temp))
    time_stamp = clean_timestamp(forecast['data'][hour]['timestamp_local'])
    c1_time_stamp.append(time_stamp)
    c1_weather.append(forecast['data'][hour]['weather']['description'].lower())


# In[ ]:





# In[6]:


city_2 = url_list[1]
forecast = requests.get(city_2).json()
 
c2_hourly_temp = []
c2_rain_chance= []
c2_time_stamp = []
c2_weather = []


for hour in range(48):
    rain = forecast['data'][hour]['pop']
    c2_rain_chance.append(round(rain*100))
    temp = forecast['data'][hour]['temp']
    c2_hourly_temp.append(round(temp))
    time_stamp = clean_timestamp(forecast['data'][hour]['timestamp_local'])
    c2_time_stamp.append(time_stamp)
    c2_weather.append(forecast['data'][hour]['weather']['description'].lower())


# In[7]:


city_3 = url_list[2]
forecast = requests.get(city_3).json()
 
c3_hourly_temp = []
c3_rain_chance= []
c3_time_stamp = []
c3_weather = []


for hour in range(48):
    rain = forecast['data'][hour]['pop']
    c3_rain_chance.append(round(rain*100))
    temp = forecast['data'][hour]['temp']
    c3_hourly_temp.append(round(temp))
    time_stamp = clean_timestamp(forecast['data'][hour]['timestamp_local'])
    c3_time_stamp.append(time_stamp)
    c3_weather.append(forecast['data'][hour]['weather']['description'].lower())


# In[8]:


city_4 = url_list[3]
forecast = requests.get(city_4).json()
 
c4_hourly_temp = []
c4_rain_chance= []
c4_time_stamp = []
c4_weather = []


for hour in range(48):
    rain = forecast['data'][hour]['pop']
    c4_rain_chance.append(round(rain*100))
    temp = forecast['data'][hour]['temp']
    c4_hourly_temp.append(round(temp))
    time_stamp = clean_timestamp(forecast['data'][hour]['timestamp_local'])
    c4_time_stamp.append(time_stamp)
    c4_weather.append(forecast['data'][hour]['weather']['description'].lower())


# In[9]:


city_5 = url_list[4]
forecast = requests.get(city_5).json()
 
c5_hourly_temp = []
c5_rain_chance= []
c5_time_stamp = []
c5_weather = []


for hour in range(48):
    rain = forecast['data'][hour]['pop']
    c5_rain_chance.append(round(rain*100))
    temp = forecast['data'][hour]['temp']
    c5_hourly_temp.append(round(temp))
    time_stamp = clean_timestamp(forecast['data'][hour]['timestamp_local'])
    c5_time_stamp.append(time_stamp)
    c5_weather.append(forecast['data'][hour]['weather']['description'].lower())


# In[ ]:





# In[10]:


df = pd.DataFrame({
    "local time": c1_time_stamp,
    "nyc wx": c1_weather,
    "nyc temp": c1_hourly_temp,
    "grr wx": c3_weather,
    "grr temp": c3_hourly_temp,
    "fll wx": c4_weather,
    "fll temp": c4_hourly_temp,

})


# In[ ]:





# In[11]:


#df['local time'] = pd.to_datetime(df['local time'], format="%m/%d/%y %I%p")


# In[12]:


dt = datetime.now()+ pd.Timedelta("1 day")
start_time = dt.replace(hour=6, minute=0)
end_time = start_time+ pd.Timedelta("29 hours")


# In[13]:


df['local time'] = pd.to_datetime(df['local time'], format="%m/%d/%y %I%p")
mask = (df['local time'] > start_time) & (df['local time'] <= end_time)
df = df.loc[mask]




# In[ ]:





# In[ ]:





# In[14]:


df2 = pd.DataFrame({
    "local time": c2_time_stamp,
    "lax wx": c2_weather,
    "lax temp": c2_hourly_temp,
"san wx": c5_weather,
    "san temp": c5_hourly_temp
})


# In[15]:





# In[17]:


df2['local time'] = pd.to_datetime(df2['local time'], format="%m/%d/%y %I%p")
mask2 = (df2['local time'] > start_time) & (df2['local time'] <= end_time)
df2 = df2.loc[mask2]


# In[22]:


final_df = pd.merge(df, df2,
how='inner', on='local time')
final_df['local time'] = final_df['local time'].dt.strftime('%I:%M %p')


# In[23]:


times= ['07:00 AM','09:00 AM', '12:00 PM', '03:00 PM', '06:00 PM', '09:00 PM', '12:00 AM', '03:00 AM', '06:00 AM']
final_df = final_df[final_df['local time'].isin(times)]


# In[27]:


final_df = final_df.set_index("local time")

final_df = final_df.transpose()


# In[25]:


final_df = final_df.reindex(['nyc wx', 'nyc temp', 'lax wx', 'lax temp', 'grr wx', 'grr temp', 'fll wx', 'fll temp', 'san wx', 'san temp'])


# In[26]:


final_df.to_csv('day_part_data.csv')


# In[ ]:




