import requests
import json
import csv
import datetime
import pandas as pd

call = "https://api.openweathermap.org/data/2.5/weather?q="
api_key = "4068916e2cc93f8de785229efdc8a78f"


def GetCitiesData(city_list):
    city_weather_data = {}
    tim = str(datetime.datetime.today())[:16]
    city_weather_data[tim] = {}
    for city in city_list:
        r = requests.get(url=call+city+'&units=metric' +"&appid="+ api_key)

        if r.status_code == 200:
            json_data =json.loads(r.content)
            city_weather_data[tim][city] = json_data['main']
        else:
            print(r.status_code, city)
    print(f"**** Status OK, code: {r.status_code} ****")

    with open(r'JSON\weathers.json' , 'a') as f:
        json.dump(city_weather_data, f, indent=4)
    return city_weather_data

def CityData(file, city):

    with open(file) as f:
        data = json.load(f)
        for k, v in data["2019-10-14 13:45"].items():
            if k == city:
                df = pd.Series(data=v)
                print(df)

def main():
    city_db = ["Bratislava", "Kosice", "Presov", "Zilina", "Banska Bystrica", "Nitra", "Trnava", "Trencin", "Martin", "Poprad", "Prievidza", "Zvolen",
        "Povazska Bystrica", "Michalovce", "Nove Zamky", "Spisska Nova Ves", "Komarno", "Hurbanovo", "Levice", "Bardejov", "Liptovsky Mikulas",
        "Lucenec", "Piestany", "Ruzomberok", "Trebisov", "Cadca", "Rimavska Sobota", "Dubnica nad Vahom", "Pezinok", "Dunajska Streda",
        "Vranov nad Toplou", "Partizanske", "Sala", "Hlohovec"]

    #GetCitiesData(city_db)
    CityData(file='JSON\weathers.json', city='Hurbanovo')
    # df = pd.read_json(r'\JSON\weathers.json',)


if __name__ == "__main__":
    main()