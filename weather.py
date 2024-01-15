#  File   : weather.py
#  Author : Max Besley
#  Purpose: Tells you the weather through the command line

from argparse import ArgumentParser
from pprint import pprint
import requests
import json

# constants
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
JSON_FILENAME = 'countries.json'


def main():
    # handle CLI arguments
    parser = ArgumentParser()
    parser.add_argument('api_key')
    parser.add_argument('city')
    parser.add_argument('-a', '--all', action='store_true')
    parser.add_argument('-d', '--description', action='store_true')
    parser.add_argument('-f', '--fahrenheit', action='store_true')

    args      = parser.parse_args()
    api_key   = args.api_key
    city_name = args.city

    # get weather data over the network
    final_url    = f"{BASE_URL}appid={api_key}&q={city_name}"
    weather_data = requests.get(final_url).json()

    # extract from the JSON data
    klvn = weather_data['main']['temp']  # in kelvin
    temp = kelvin_to_fahrenheit(klvn) if args.fahrenheit else kelvin_to_celsius(klvn)
    country_code = weather_data['sys']['country']
    country_name = country_code_to_name(country_code)

    # final output
    print('----------------------------------------------')
    print(f"Place:    {city_name}")
    print(f"Country:    {country_name}")
    print(f"Temperature:    {temp}")

    if args.description:
        pass

    if args.all:
        print(); pprint(weather_data); print()

    print('----------------------------------------------')


def kelvin_to_fahrenheit(k):
    return 1.8 * k - 459.67

def kelvin_to_celsius(k):
    return k - 273.15

def country_code_to_name(country_code):
    with open(JSON_FILENAME) as json_file:
        countries = json.load(json_file)

    for country in countries:
        if country['Code'] == country_code:
            country_name = country['Name']
            break
    return country_name


# program entry point
if __name__ == "__main__":
    main()
