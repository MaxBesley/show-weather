#  File   : weather.py
#  Author : Max Besley
#  Purpose: Tells you the weather through the command line

import requests
from pprint import pprint
from argparse import ArgumentParser


def main():
    # constants
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

    # handle CLI arguments
    parser = ArgumentParser()
    parser.add_argument('api_key')
    parser.add_argument('city')
    parser.add_argument('-a', '--all', action='store_true')
    parser.add_argument('-d', '--description', action='store_true')
    parser.add_argument('-f', '--fahrenheit', action='store_true')

    args = parser.parse_args()
    API_KEY   = args.api_key
    city_name = args.city

    # get weather data over the network
    FINAL_URL = BASE_URL + 'appid=' + API_KEY + '&q=' + city_name
    weather_data = requests.get(FINAL_URL).json()

    # extract from the JSON data
    temp    = weather_data['main']['temp']
    country = weather_data['sys']['country']
    if args.fahrenheit:
        temp = kelvin_to_fahrenheit(temp)
    else:
        temp = kelvin_to_celsius(temp)


    # final output
    print('----------------------------------------------')
    print(f"Place:    {city_name}")
    print(f"Country:    {country}")
    print(f"Temperature:    {temp}")

    if args.all:
        print()
        pprint(weather_data)
        print()

    print('----------------------------------------------')


def kelvin_to_fahrenheit(k):
    return 1.8 * k - 459.67

def kelvin_to_celsius(k):
    return k - 273.15


if __name__ == "__main__":
    main()
