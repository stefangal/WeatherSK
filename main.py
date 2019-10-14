import requests
import json
import csv
import datetime

call = "https://api.openweathermap.org/data/2.5/weather?q="
api_key = "4068916e2cc93f8de785229efdc8a78f"


def GetCitiesData(city_list):
    """
    Give list of cities to get a Json file with data. 1 data report withe date & time key.
    """
    city_weather_data = {}
    tim = str(datetime.datetime.today())[:16]
    city_weather_data[tim] = {}

    for city in city_list:
        #load city by city
        r = requests.get(url=call+city+'&units=metric' +"&appid="+ api_key)

        if r.status_code == 200:
            json_data =json.loads(r.content)
            city_weather_data[tim][city] = [json_data['main'], json_data['weather'], json_data['wind']]
        else:
            print(f"ISSUE: {r.status_code} with city: {city}")

    print(f"**** Status OK, code: {r.status_code} ****")

    # Save to JSON file: weather.json
    with open(r'JSON\weathers.json' , 'w') as f:
        json.dump(city_weather_data, f, indent=4)
    return city_weather_data


def CityData(file, city):
    with open(file) as f:
        data = json.load(f)
        # print(city)
        # print("**********")
        # for k,v in data["2019-10-14 14:10"][city].items():
        #     print(k, v)

city_db = ["Bratislava", "Kosice", "Hurbanovo", "Nitra"]

GetCitiesData(city_db)
CityData(file='JSON\weathers.json', city='Hurbanovo')