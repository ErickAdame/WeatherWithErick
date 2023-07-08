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

# List of cities
city_list = ["new york", "los angeles", "grand rapids", "chicago", "charlotte", "fort lauderdale"]

# Loop through the cities
for city in city_list:
    city = city.lower()

    url = "https://api.weatherbit.io/v2.0/forecast/daily"
    key = "85a65933d3894f0d9c7194ffa8098565"
    units = "&units=I"

    final_url = f"{url}?city={city}{units}&key={key}"

    forecast = requests.get(final_url).json()

    high_temps = []
    low_temps = []
    weather = []
    weekday = []


    for day in range(1, 8):
        max_temp = forecast["data"][day]["high_temp"]
        max_temp = round(max_temp)
        high_temps.append(max_temp)
        min_temp = forecast["data"][day]["low_temp"]
        min_temp = round(min_temp)
        low_temps.append(min_temp)
        conditions = forecast["data"][day]["weather"]["description"].lower()
        weather.append(conditions)


        dt = datetime.now() + timedelta(days=day)
        day = dt.strftime('%a').upper()
        weekday.append(day)

    five_day = pd.DataFrame({
        "Date": weekday,
        "High Temp": high_temps,
        "Low Temp": low_temps,
        "condition": weather
    })

    five_day.to_csv(f'{city}_7_day_forecast.csv')

    city_list[1] = "los angeles"
    seven_day = pd.DataFrame({
        "Date": weekday,
        "High Temp": high_temps,
        "Low Temp": low_temps,
        "condition": weather
    })

    x = seven_day["Date"]
    y = seven_day["High Temp"]
    plt.rcParams['font.family'] = ['sans', 'bold']
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False
    plt.rcParams["axes.spines.left"] = False
    fig = plt.figure(figsize=(12, 5))

    def addlabels(x, y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha="center", color="white", size="35", va="bottom")

    plt.bar(x, y, color="blue", width=0.7, alpha=0.75)
    addlabels(x, y)
    plt.tick_params(left=False, right=False, labelleft=False,
                    labelbottom=True, bottom=False)
    plt.xticks(size=30, color="white")
    plt.ylim([0, five_day["High Temp"].max() + 10])
    plt.savefig(f"{city}_7_Day_Forecast.png", transparent=True)
