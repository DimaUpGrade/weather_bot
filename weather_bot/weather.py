import requests
from config import WEATHER_API_KEY


# pop -- вероятность осадков
# max_temp -- минимальная температура за сутки, °C
# min_temp -- максимальная температура за сутки, °C
# pres -- давление, мбар
# rh -- относительная влажность, %
# wind_cdir -- направление ветра
# wind_spd -- скорость ветра, м/с


def current_weather(city):
    request = requests.get(f"https://api.weatherbit.io/v2.0/current?city={city}&key={WEATHER_API_KEY}")

    if request.status_code == 200:
        return request.json()["data"][0]
    else:
        print(f"Fail. Status code: {request.status_code}")
        return False
    

def today_weather(city):
    request = requests.get(f"https://api.weatherbit.io/v2.0/forecast/hourly?city={city}&key=a615b6f103ab48a681fe4683accbba9e")

    if request.status_code == 200:
        return request.json()["data"]
    else:
        print(f"Fail. Status code: {request.status_code}")
        return False


def daily_weather(city):
    request = requests.get(f"https://api.weatherbit.io/v2.0/forecast/daily?city={city}&key={WEATHER_API_KEY}")

    if request.status_code == 200:
        return request.json()["data"]
    else:
        print(f"Fail. Status code: {request.status_code}")
        return False
