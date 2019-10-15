import requests
import json
import csv
import datetime
import pandas as pd
from pprint import pprint

call = "https://api.openweathermap.org/data/2.5/weather?q="
api_key = "4068916e2cc93f8de785229efdc8a78f"


def GetCitiesData(city_list):
    """
    Give list of cities to get a Json file with data. 1 data report withe date & time key.
    """
    city_weather_data = dict()
    clean_list = []
    city = 'Hurbanovo'

    r = requests.get(url=call+city+'&units=metric' +"&appid="+ api_key)

    if r.status_code == 200:
        data =json.loads(r.content)
        pprint(data)
    else:
        print(f'Cannot access OpenWeatherMap.org for data. Error code: {r.statuscode}')

    # Save to JSON file: weather.json
    with open(r'JSON\weathers.json' , 'w') as f:
        json.dump(data, f, indent=4)
    return data


city_db = ["Bratislava", "Kosice", "Hurbanovo", "Nitra"]

GetCitiesData(city_db)
