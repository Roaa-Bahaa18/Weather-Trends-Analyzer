import json
from unittest.mock import DEFAULT
from datetime import date
import dask.dataframe as dd
import requests
import os
import pandas as pd

def get_coordinates(city_name):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    response = requests.get(url).json()
    if "results" in response and len(response["results"]) > 0:
        lat = response["results"][0]["latitude"]
        lon = response["results"][0]["longitude"]
        country = response["results"][0]["country"]
        return lat,lon,country
    else:
        raise Exception(f'Failed to fetch coordinates for {city_name}!')


def fetch_weather_data(latitude=30.0444,longitude=31.2357,city_name='Cairo',start_date= date.today(), end_date= date.today() ):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params ={
        #latitude and longitude are precise coordinates for location.
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ["temperature_2m", "precipitation"],
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        hourly_data = data["hourly"]

        source = {
            "time": pd.to_datetime(hourly_data["time"]),
            "temperature_2m": hourly_data["temperature_2m"],
            "precipitation": hourly_data["precipitation"],
            "latitude": data["latitude"],
            "longitude": data["longitude"]
        }
        ddf = dd.from_dict(source,npartitions=2)

        os.makedirs('data/raw',exist_ok=True)

        file_path = f"data/raw/{city_name.lower()}_weather_parquet"
        ddf.to_parquet(file_path, engine='pyarrow',write_index=False)

        print(f"Successfully fetched and saved weather data for {city_name}!")
        return file_path

    else:
        raise Exception(f'Failed to Fetch: {response.status_code}: {response.text}')

