import os

import requests

import xmltodict

op_key = os.environ.get('OPEN_WEATHER_KEY')


def get_weather(city):
    """
    Sends request to OpenWeather, transforms xml to dict.
    :param city:
    :return: dict - weather_data
    """

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={op_key}&mode=xml&units=metric"

    response = requests.get(url)
    response.raise_for_status()
    data = xmltodict.parse(response.content)['current']
    weather_data = {
        'city': data['city']['@name'],
        'temp': int(float(data['temperature']['@value'])),
        'pressure': int(float(data['pressure']['@value']) * 0.7506),
        'wind': data['wind']['speed']['@value'],
    }
    return weather_data
