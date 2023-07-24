#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import requests
import pandas as pd
from config import weather_api_key
from datetime import datetime
import matplotlib.dates as mdates



# In[3]:


city_list = ["san diego", "palm springs", "las vegas", "phoenix", "salt lake city", "san jose", "portland"]

url = "https://api.openweathermap.org/data/2.5/forecast"
units = "imperial"
dt = datetime.now() + pd.Timedelta("1 day")
start_time = dt.replace(hour=6, minute=0)
end_time = start_time+ pd.Timedelta("18 hours")

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

    
print("Processing now.........")
print("-------------------------")


# In[4]:


#NEW YORK -----------------------------------------
city_1 = url_list[0]
forecast = requests.get(city_1).json()
 
c1_hourly_temp = []
c1_rain_chance= []
c1_time_stamp = []
c1_ts = []
c1_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c1_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c1_hourly_temp.append(round(temp))
    c1_time_stamp.append(forecast['list'][hour]['dt'])
    c1_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c1_time_stamp:
    c1_ts.append(datetime.fromtimestamp(time))


#LOS ANGELES-----------------------------------------
city_2 = url_list[1]
forecast = requests.get(city_2).json()
 
c2_hourly_temp = []
c2_rain_chance= []
c2_time_stamp = []
c2_ts = []
c2_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c2_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c2_hourly_temp.append(round(temp))
    c2_time_stamp.append(forecast['list'][hour]['dt'])
    c2_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c2_time_stamp:
    c2_ts.append(datetime.fromtimestamp(time))
    
#BUFFALO -----------------------------------------
city_3 = url_list[2]
forecast = requests.get(city_3).json()
 
c3_hourly_temp = []
c3_rain_chance= []
c3_time_stamp = []
c3_ts = []
c3_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c3_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c3_hourly_temp.append(round(temp))
    c3_time_stamp.append(forecast['list'][hour]['dt'])
    c3_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c3_time_stamp:
    c3_ts.append(datetime.fromtimestamp(time))


#Philadelphia -----------------------------------------
city_4 = url_list[3]
forecast = requests.get(city_4).json()
 
c4_hourly_temp = []
c4_rain_chance= []
c4_time_stamp = []
c4_ts = []
c4_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c4_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c4_hourly_temp.append(round(temp))
    c4_time_stamp.append(forecast['list'][hour]['dt'])
    c4_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c4_time_stamp:
    c4_ts.append(datetime.fromtimestamp(time))
    
#Albany
city_5 = url_list[4]
forecast = requests.get(city_5).json()
 
c5_hourly_temp = []
c5_rain_chance= []
c5_time_stamp = []
c5_ts = []
c5_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c5_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c5_hourly_temp.append(round(temp))
    c5_time_stamp.append(forecast['list'][hour]['dt'])
    c5_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c5_time_stamp:
    c5_ts.append(datetime.fromtimestamp(time))
    
#San Diego
city_6 = url_list[5]
forecast = requests.get(city_6).json()
 
c6_hourly_temp = []
c6_rain_chance= []
c6_time_stamp = []
c6_ts = []
c6_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c6_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c6_hourly_temp.append(round(temp))
    c6_time_stamp.append(forecast['list'][hour]['dt'])
    c6_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c6_time_stamp:
    c6_ts.append(datetime.fromtimestamp(time))
    
#San Diego
city_7 = url_list[6]
forecast = requests.get(city_7).json()
 
c7_hourly_temp = []
c7_rain_chance= []
c7_time_stamp = []
c7_ts = []
c7_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c7_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c7_hourly_temp.append(round(temp))
    c7_time_stamp.append(forecast['list'][hour]['dt'])
    c7_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c7_time_stamp:
    c7_ts.append(datetime.fromtimestamp(time))


# In[5]:


df= pd.DataFrame({
    "Date": c1_ts,
    "SAN DIEGO": c1_weather,
    "C1 TEMPS": c1_hourly_temp,
  #  "NYC Rain Chance": nyc_rain_chance,
    "PALM SPRINGS": c2_weather,
    "C2 TEMPS": c2_hourly_temp,
 #   "BOS Rain Chance": bos_rain_chance,
    "LAS VEGAS": c3_weather,
    "C3 TEMPS": c3_hourly_temp,
  #  "BUF Rain Chance": buf_rain_chance,
    "PHOENIX": c4_weather,
    "C4 TEMPS": c4_hourly_temp,
  #  "PHL Rain Chance": phl_rain_chance,
    "SALT LAKE CITY": c5_weather,
    "C5 TEMPS": c5_hourly_temp,
  #  "ALB Rain Chance": alb_rain_chance,
    "SAN JOSE": c6_weather,
    "C6 TEMPS": c6_hourly_temp,
  #  "SAN Rain Chance": san_rain_chance,
    "PORTLAND": c7_weather,
    "C7 TEMPS": c7_hourly_temp,
  #  "SAN Rain Chance": san_rain_chance,
    })


df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'] - pd.Timedelta(hours=1)
df["Date"] = pd.to_datetime(df['Date'].astype(str))

mask = (df['Date'] > start_time) & (df['Date'] <= end_time)

df = df.loc[mask]
df["Date"] = df["Date"].dt.strftime('%-I%p')
df = df.transpose()
df.to_csv('city_hourly_forecast_WEST.csv')


# In[6]:


city_list = ["jersey city", "albany", "buffalo", "syracuse, US", "rochester", "philadelphia", "boston"]
#city_list = ["long beach", "palm springs", "las vegas", "phoenix", "salt lake city", "san jose", "portland"]

url = "https://api.openweathermap.org/data/2.5/forecast"
units = "imperial"
dt = datetime.now() + pd.Timedelta("1 day")
start_time = dt.replace(hour=6, minute=0)
end_time = start_time+ pd.Timedelta("18 hours")

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


# In[7]:


#NEW YORK -----------------------------------------
city_1 = url_list[0]
forecast = requests.get(city_1).json()
 
c1_hourly_temp = []
c1_rain_chance= []
c1_time_stamp = []
c1_ts = []
c1_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c1_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c1_hourly_temp.append(round(temp))
    c1_time_stamp.append(forecast['list'][hour]['dt'])
    c1_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c1_time_stamp:
    c1_ts.append(datetime.fromtimestamp(time))


#LOS ANGELES-----------------------------------------
city_2 = url_list[1]
forecast = requests.get(city_2).json()
 
c2_hourly_temp = []
c2_rain_chance= []
c2_time_stamp = []
c2_ts = []
c2_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c2_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c2_hourly_temp.append(round(temp))
    c2_time_stamp.append(forecast['list'][hour]['dt'])
    c2_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c2_time_stamp:
    c2_ts.append(datetime.fromtimestamp(time))
    
#BUFFALO -----------------------------------------
city_3 = url_list[2]
forecast = requests.get(city_3).json()
 
c3_hourly_temp = []
c3_rain_chance= []
c3_time_stamp = []
c3_ts = []
c3_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c3_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c3_hourly_temp.append(round(temp))
    c3_time_stamp.append(forecast['list'][hour]['dt'])
    c3_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c3_time_stamp:
    c3_ts.append(datetime.fromtimestamp(time))


#Philadelphia -----------------------------------------
city_4 = url_list[3]
forecast = requests.get(city_4).json()
 
c4_hourly_temp = []
c4_rain_chance= []
c4_time_stamp = []
c4_ts = []
c4_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c4_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c4_hourly_temp.append(round(temp))
    c4_time_stamp.append(forecast['list'][hour]['dt'])
    c4_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c4_time_stamp:
    c4_ts.append(datetime.fromtimestamp(time))
    
#Albany
city_5 = url_list[4]
forecast = requests.get(city_5).json()
 
c5_hourly_temp = []
c5_rain_chance= []
c5_time_stamp = []
c5_ts = []
c5_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c5_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c5_hourly_temp.append(round(temp))
    c5_time_stamp.append(forecast['list'][hour]['dt'])
    c5_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c5_time_stamp:
    c5_ts.append(datetime.fromtimestamp(time))
    
#San Diego
city_6 = url_list[5]
forecast = requests.get(city_6).json()
 
c6_hourly_temp = []
c6_rain_chance= []
c6_time_stamp = []
c6_ts = []
c6_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c6_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c6_hourly_temp.append(round(temp))
    c6_time_stamp.append(forecast['list'][hour]['dt'])
    c6_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c6_time_stamp:
    c6_ts.append(datetime.fromtimestamp(time))
    
#San Diego
city_7 = url_list[6]
forecast = requests.get(city_7).json()
 
c7_hourly_temp = []
c7_rain_chance= []
c7_time_stamp = []
c7_ts = []
c7_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c7_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c7_hourly_temp.append(round(temp))
    c7_time_stamp.append(forecast['list'][hour]['dt'])
    c7_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c7_time_stamp:
    c7_ts.append(datetime.fromtimestamp(time))


# In[8]:


df= pd.DataFrame({
    "Date": c1_ts,
    "JERSEY CITY": c1_weather,
    "C1 TEMPS": c1_hourly_temp,
  #  "NYC Rain Chance": nyc_rain_chance,
    "ALBANY": c2_weather,
    "C2 TEMPS": c2_hourly_temp,
 #   "BOS Rain Chance": bos_rain_chance,
    "BUFFALO": c3_weather,
    "C3 TEMPS": c3_hourly_temp,
  #  "BUF Rain Chance": buf_rain_chance,
    "SYRACUSE": c4_weather,
    "C4 TEMPS": c4_hourly_temp,
  #  "PHL Rain Chance": phl_rain_chance,
    "ROCHESTER": c5_weather,
    "C5 TEMPS": c5_hourly_temp,
  #  "ALB Rain Chance": alb_rain_chance,
    "PHILADELPHIA": c6_weather,
    "C6 TEMPS": c6_hourly_temp,
  #  "SAN Rain Chance": san_rain_chance,
    "BOSTON": c7_weather,
    "C7 TEMPS": c7_hourly_temp,
  #  "SAN Rain Chance": san_rain_chance,
    })




df["Date"] = pd.to_datetime(df['Date'].astype(str))

mask = (df['Date'] > start_time) & (df['Date'] <= end_time)

df = df.loc[mask]
df["Date"] = df["Date"].dt.strftime('%-I%p')
df = df.transpose()
df.to_csv('city_hourly_forecast.csv')


city_list = ["Columbia", "Washington dc", "Grand Rapids", "Dallas", "Nashville", "Indianapolis", "West Palm Beach"]

url = "https://api.openweathermap.org/data/2.5/forecast"
units = "imperial"
dt = datetime.now() + pd.Timedelta("1 day")
start_time = dt.replace(hour=6, minute=0)
end_time = start_time+ pd.Timedelta("18 hours")

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


# In[7]:


#NEW YORK -----------------------------------------
city_1 = url_list[0]
forecast = requests.get(city_1).json()
 
c1_hourly_temp = []
c1_rain_chance= []
c1_time_stamp = []
c1_ts = []
c1_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c1_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c1_hourly_temp.append(round(temp))
    c1_time_stamp.append(forecast['list'][hour]['dt'])
    c1_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c1_time_stamp:
    c1_ts.append(datetime.fromtimestamp(time))


#LOS ANGELES-----------------------------------------
city_2 = url_list[1]
forecast = requests.get(city_2).json()
 
c2_hourly_temp = []
c2_rain_chance= []
c2_time_stamp = []
c2_ts = []
c2_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c2_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c2_hourly_temp.append(round(temp))
    c2_time_stamp.append(forecast['list'][hour]['dt'])
    c2_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c2_time_stamp:
    c2_ts.append(datetime.fromtimestamp(time))
    
#BUFFALO -----------------------------------------
city_3 = url_list[2]
forecast = requests.get(city_3).json()
 
c3_hourly_temp = []
c3_rain_chance= []
c3_time_stamp = []
c3_ts = []
c3_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c3_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c3_hourly_temp.append(round(temp))
    c3_time_stamp.append(forecast['list'][hour]['dt'])
    c3_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c3_time_stamp:
    c3_ts.append(datetime.fromtimestamp(time))


#Philadelphia -----------------------------------------
city_4 = url_list[3]
forecast = requests.get(city_4).json()
 
c4_hourly_temp = []
c4_rain_chance= []
c4_time_stamp = []
c4_ts = []
c4_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c4_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c4_hourly_temp.append(round(temp))
    c4_time_stamp.append(forecast['list'][hour]['dt'])
    c4_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c4_time_stamp:
    c4_ts.append(datetime.fromtimestamp(time))
    
#Albany
city_5 = url_list[4]
forecast = requests.get(city_5).json()
 
c5_hourly_temp = []
c5_rain_chance= []
c5_time_stamp = []
c5_ts = []
c5_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c5_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c5_hourly_temp.append(round(temp))
    c5_time_stamp.append(forecast['list'][hour]['dt'])
    c5_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c5_time_stamp:
    c5_ts.append(datetime.fromtimestamp(time))
    
#San Diego
city_6 = url_list[5]
forecast = requests.get(city_6).json()
 
c6_hourly_temp = []
c6_rain_chance= []
c6_time_stamp = []
c6_ts = []
c6_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c6_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c6_hourly_temp.append(round(temp))
    c6_time_stamp.append(forecast['list'][hour]['dt'])
    c6_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c6_time_stamp:
    c6_ts.append(datetime.fromtimestamp(time))
    
#San Diego
city_7 = url_list[6]
forecast = requests.get(city_7).json()
 
c7_hourly_temp = []
c7_rain_chance= []
c7_time_stamp = []
c7_ts = []
c7_weather = []
    
for hour in range(15):
    rain = forecast['list'][hour]['pop']
    c7_rain_chance.append(round(rain*100))
    temp = forecast['list'][hour]['main']['temp']
    c7_hourly_temp.append(round(temp))
    c7_time_stamp.append(forecast['list'][hour]['dt'])
    c7_weather.append(forecast['list'][hour]['weather'][0]['description'])
        
for time in c7_time_stamp:
    c7_ts.append(datetime.fromtimestamp(time))


# In[8]:


df= pd.DataFrame({
    "Date": c1_ts,
    "COLUMBIA, SC": c1_weather,
    "C1 TEMPS": c1_hourly_temp,
  #  "NYC Rain Chance": nyc_rain_chance,
    "WASHINGTON, DC": c2_weather,
    "C2 TEMPS": c2_hourly_temp,
 #   "BOS Rain Chance": bos_rain_chance,
    "GRAND RAPIDS": c3_weather,
    "C3 TEMPS": c3_hourly_temp,
  #  "BUF Rain Chance": buf_rain_chance,
    "DALLAS": c4_weather,
    "C4 TEMPS": c4_hourly_temp,
  #  "PHL Rain Chance": phl_rain_chance,
    "NASHVILLE": c5_weather,
    "C5 TEMPS": c5_hourly_temp,
  #  "ALB Rain Chance": alb_rain_chance,
    "INDIANAPOLIS": c6_weather,
    "C6 TEMPS": c6_hourly_temp,
  #  "SAN Rain Chance": san_rain_chance,
    "WEST PALM BEACH": c7_weather,
    "C7 TEMPS": c7_hourly_temp,
  #  "SAN Rain Chance": san_rain_chance,
    })




df["Date"] = pd.to_datetime(df['Date'].astype(str))

mask = (df['Date'] > start_time) & (df['Date'] <= end_time)

df = df.loc[mask]
df["Date"] = df["Date"].dt.strftime('%-I%p')
df = df.transpose()
df.to_csv('city_hourly_ELSE_forecast.csv')

# In[12]:


city_list = ["new york", "buffalo, NY", "albany, NY", "boston, MA", "philadelphia", "columbus, OH", "washington dc", "los angeles, CA", "san diego, CA", "miami, FL", "dallas, TX", "atlanta, GA", "chicago, IL", "las vegas, NV", "phoenix, AZ", "sacramento, CA", "grand rapids, MI", "detroit, MI", "des moines, IA", "minneapolis, MN", "cincinnati, OH", "charlotte, NC", "savannah, GA", "tampa, FL", "new orleans, LA", "memphis, TN", "wilmington, NC", "charleston, SC", "bakersfield, CA", "oceanside, CA", "palm springs, CA", "santa barbara, CA", "syracuse, NY", "newark, NJ", "jersey city, NJ" ,"garden city, NY", "long beach, ny", "bay shore, ny", "brooklyn, ny", "parkchester, ny", "bulls head, ny", "bayside, ny" ]
url = "https://api.weatherbit.io/v2.0/forecast/daily"
key = "85a65933d3894f0d9c7194ffa8098565"
units = "&units=I"

url_list = []

for city in city_list:
    city=city

    final_url = final_url = f"{url}?city={city}{units}&key={key}"
    url_list.append(final_url)

url_zip = f"https://api.weatherbit.io/v2.0/forecast/daily?postal_code=11360&country=US{units}&key={key}"
url_list.append(url_zip)
    
city_name = []
high_temp = []
low_temp= []
weather = []
pop = []
daily_precip = []
time_stamp = []
ts = []
high2 = []
high3 = []
weather2 = []
weather3 = []
    
for url in range(len(url_list)):
    forecast = requests.get(url_list[url]).json()
    city_name.append(forecast['city_name'])
    high = forecast['data'][1]['max_temp']
    high_temp.append(round(high))
    low = forecast['data'][1]['min_temp']
    low_temp.append(round(low))    
    pop.append(forecast['data'][1]['pop'])
    daily_precip.append(forecast['data'][1]['precip'])
    weather.append((forecast['data'][1]['weather']['description']).lower())
    high2.append(round(forecast['data'][2]['max_temp']))
    high3.append(round(forecast['data'][3]['max_temp']))
    weather2.append((forecast['data'][2]['weather']['description']).lower())
    weather3.append((forecast['data'][3]['weather']['description']).lower())
    
df = pd.DataFrame({
    "City": city_name,
    "Today High": high_temp,
    "Tonight Low": low_temp,
    "Weather": weather,
    "Daily Precip": daily_precip,
    "POP": pop,
    "Tomorrow High": high2,
    "Tomorrow Weather": weather2,
    "Next Next High": high3,
    "Next Next Weather": weather3
}
)

df = df.sort_values('City')
df["Daily Precip"] = df["Daily Precip"].round(2)

df.to_csv('city_high_and Lows.csv')


# %%
