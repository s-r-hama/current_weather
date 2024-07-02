# weather_check.py

import requests
import sys
import argparse


weather_api_key = 'fd1e5f2bacc46115a0da2f1ef51b9564'  # My API key

def rainy_weather_data(weather_api_key, weather_location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={weather_location}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def check_rainy_weather_data(aweather_api_key, weather_location):
    rain_data = rainy_weather_data(weather_api_key, weather_location)
    rain_percent = rain_data.get('rain', {}).get('1h', 0)
    print(f"chance of rain in percentage: {rain_percent * 100}%")
    return rain_percent > 0.05


def shiney_weather_data(weather_location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={weather_location}&appid={weather_api_key}&units=metric'
    response = requests.get(url)
    # response.raise_for_status()
    return response.json()


def get_uv_index(latitude, longtitude):
    url = f'http://api.openweathermap.org/data/2.5/uvi?lat={latitude}&lon={longtitude}&appid={weather_api_key}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    if len(sys.argv) != 3:
        print("Usage: python current_weather.py <rain|shine> <weather_location>")
        sys.exit(1)

    args_action = sys.argv[1]
    weather_location = sys.argv[2]
    weather_api_key = 'fd1e5f2bacc46115a0da2f1ef51b9564'


    parser = argparse.ArgumentParser(description='Checking Today \'s weather conditions.')
    parser.add_argument('condition', choices=['rain', 'shine'], help='The weather condition to check.')
    parser.add_argument('weather_location', help='The weather_location to check the weather for.')
    args = parser.parse_args()

    weather_data = shiney_weather_data(args.weather_location)
    latitude = weather_data['coord']['lat']
    longtitude = weather_data['coord']['lon']
    
    if args.condition == 'rain':
        if any(weather['main'] == 'Rain' for weather in weather_data['weather']):
            args_result = check_rainy_weather_data(weather_api_key, weather_location)
        else:
            print("It will not be raining today.")
    elif args.condition == 'shine':
        uv_data = get_uv_index(latitude, longtitude = weather_data['coord']['lon']
)
        uv_index = uv_data['value']
        print(f"UV Index: {uv_index}")
        if uv_index > 3:
            print(True)
        else:
            print(False)

if __name__ == "__main__":
    main()
